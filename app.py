import streamlit as st
import pandas as pd 
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler

def main() :
    st.title('K-Means 클러스터링 대시보드 앱')
    
    # 1. csv 파일을 업로드 할 수 있다.
 
    file = st.file_uploader('CSV파일 업로드', type=['csv'])
   
    if file is not None :
        df = pd.read_csv(file)
        st.dataframe( df )
        
        # 결측값 처리한다.
        
        df.dropna()

        # X 로 사용할 컬럼 선택하도록 만들기
        column_list = df.columns
        selected_columns = st.multiselect('X로 사용할 컬럼을 선택하세요', column_list)
        
        
        # 컬럼을 선택했다면
        if len(selected_columns) != 0 :
            X = df[selected_columns]
            st.dataframe(X)

            # 문자열이 들어있으면 처리한 후에 화면에 보여준다.
            # 비어있는 데이터프레임 생성
            X_new = pd.DataFrame()

            for name in X.columns :
                
                # 각 컬럼 데이터를 가져온다.
                data = X[name]
                
                # 문자열인지 아닌지 나눠서 처리하면 된다
                if data.dtype == object :
                    
                    # 문자열이니까, 갯수가 2개인지 아닌지 파악해서 
                    # 2개이면, 레이블 인코딩하고, 
                    # 그렇지 않으면 원핫인코딩 하도록 코드 작성
                    if data.nunique() <= 2:
                        # 레이블 인코딩
                        label_encoder = LabelEncoder()
                        X_new[name] = label_encoder.fit_transform(data)
                        
                        
                    else:
                        # 원핫인코딩
                        ct = ColumnTransformer( [ ('encoder', OneHotEncoder(), [0] ) ] ,
                                remainder= 'passthrough' )
                        
                        col_names = sorted(data.unique())
                        
                        X_new[col_names] = ct.fit_transform(data.to_frame())
                        
                else:
                    # 숫자 데이터 처리
                    X_new[name] = data  

            scaler = MinMaxScaler()
            X_new = scaler.fit_transform(X_new)

            st.dataframe(X_new)

            # 슬라이더로 클러스터링 갯수 선택
            st.subheader('WCSS를 위한 클러스터링 갯수를 선택')
            max_number = st.slider('최대 그룹 선택', 2, 10, value= 5)
            
            # wcss 구하기
            wcss = []
            for k in np.arange(1, max_number + 1):
                Kmeans = KMeans(n_clusters= k, random_state= 5)
                Kmeans.fit(X_new)
                wcss.append(Kmeans.inertia_)


            # st.write(wcss)
            # wcss 값을, 차트로 나타낸다. => 엘보우 메소드
            x = np.arange(1, max_number + 1)
            
            fig1 = plt.figure()
            plt.plot( x, wcss )
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)


            # 실제로 그룹핑 할 갯수 선택

            k = st.number_input('그룹 갯수 결정', 1, max_number)

            kmeans = KMeans(n_clusters= k, random_state= 5)

            # 그룹핑한 데이터를 데이터프레임에 저장
            y_pred = kmeans.fit_predict(X_new)
            df['Group'] = y_pred
            st.dataframe(df.sort_values('Group'))

            df.to_csv('result.csv')

            # 인터랙티브하게 만들기
            # 숫자를 입력하면 그 숫자의 그룹 데이터프레임만 나타낸다
            st.text('숫자를 선택하시면, 그 숫자의 특정 그룹 데이터프레임만 보여줍니다')
            num = st.number_input('숫자를 입력하세요', 1, k - 1, value= 1)
            st.dataframe(df[df['Group'] == num])
            




if __name__ == '__main__' :
    main()