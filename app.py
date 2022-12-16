import streamlit as st
import pandas as pd 
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def main() :
    st.title('K-Means 클러스터링')
    
    # 1. csv 파일을 업로드 할 수 있다.
 
    file = st.file_uploader('CSV파일 업로드', type=['csv'])
   
    if file is not None :
        df = pd.read_csv(file)
        st.dataframe( df )
        
        if df.isna().sum().sum() > 0 :
            df.dropna()

        # X 로 사용할 컬럼 선택하도록 만들기
        column_list = df.columns
        selected_columns = st.multiselect('X로 사용할 컬럼을 선택하세요', column_list)


        
        # 컬럼을 선택했다면
        if len(selected_columns) != 0 :
            X = df[selected_columns]
            st.dataframe(X)


            # 슬라이더로 클러스터링 갯수 선택
            st.subheader('WCSS를 위한 클러스터링 갯수를 선택')
            max_number = st.slider('최대 그룹 선택', 2, 20, value= 10)
            
            # wcss 구하기
            wcss = []
            for k in np.arange(1, max_number + 1):
                Kmeans = KMeans(n_clusters= k, random_state= 5)
                Kmeans.fit(X)
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
            y_pred = kmeans.fit_predict(X)
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