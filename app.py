from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import streamlit as st
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler


def main() :
    st.title('π K-Means ν΄λ¬μ€ν°λ§ μ± ')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    with st.expander('π λμλ³΄λ μ€λͺ') :
        st.text('μ΄ μ±μ K-Means Clustering μ μ΄μ©νμ¬μ, ')
        st.text('μ£Όμ΄μ§ λ°μ΄ν°λ₯Ό kκ°μ ν΄λ¬μ€ν°λ‘ λ¬Άμ΄μ λ°μ΄ν°λ₯Ό λνλ΄λ μκ³ λ¦¬μ¦ μ± μλλ€.')
        st.text('κ°μ₯ μ ν©ν κΈ°μ€μ μ μ°ΎκΈ° μν΄ wcss λ₯Ό μ΄μ©νμκ³ ,')
        st.text('λ¬Έμμ΄ λ°μ΄ν°λ₯Ό μ²λ¦¬νκΈ° μν΄μ, Label-Encoding κ³Ό One-Hot Encoding μ μ΄μ©νμμ΅λλ€. ')
        st.text('ν΄λ¬μ€ν°λ§ ν μ¬μ©μκ° μνλ κ·Έλ£Ή λ°μ΄ν°λ₯Ό μ ννμ¬μ νμΈν  μ μμ΅λλ€. ')


    # 1. csv νμΌμ μλ‘λ ν μ μλ€.
    st.text('')
    file = st.file_uploader(' csv νμΌμ μλ‘λ', type=['csv'])

    if file is not None :
        # csv νμΌμ, νλ€μ€λ‘ μ½μ΄μ νλ©΄μ λ³΄μ¬μ€λ€.
        df = pd.read_csv(file)
        st.dataframe( df )

        # κ²°μΈ‘κ° μ²λ¦¬νλ€.
        df = df.dropna()
        st.text('')
        st.text('')
        column_list = df.columns
        selected_columns = st.multiselect('Xλ‘ μ¬μ©ν  μ»¬λΌμ μ ννμΈμ', column_list)

        if len(selected_columns) != 0 : 
            X = df[selected_columns]
            st.dataframe(X)

            # λ¬Έμμ΄μ΄ λ€μ΄μμΌλ©΄ μ²λ¦¬ν νμ νλ©΄μ λ³΄μ¬μ£Όμ.
            X_new = pd.DataFrame()

            for name in X.columns :
                print(name)    
                # κ° μ»¬λΌ λ°μ΄ν°λ₯Ό κ°μ Έμ¨λ€.
                data = X[name]
                data.reset_index(inplace=True, drop=True)  
                
                # λ¬Έμμ΄μΈμ§ μλμ§ λλ μ μ²λ¦¬νλ©΄ λλ€. 
                if data.dtype == object :
                    
                    # λ¬Έμμ΄μ΄λκΉ, κ°―μκ° 2κ°μΈμ§ μλμ§ νμν΄μ
                    # 2κ°μ΄λ©΄ λ μ΄λΈ μΈμ½λ© νκ³ ,
                    # κ·Έλ μ§ μμΌλ©΄ μν«μΈμ½λ© νλλ‘ μ½λ μμ±
                    
                    if data.nunique() <= 2 :
                        # λ μ΄λΈ μΈμ½λ©
                        label_encoder = LabelEncoder()
                        
                        
                        X_new[name] = label_encoder.fit_transform(data)            
                        
                    else :
                        # μν«μΈμ½λ©
                        ct = ColumnTransformer( [ ('encoder', OneHotEncoder(), [0] ) ] , 
                                remainder='passthrough' )
                        
                        col_names = sorted(data.unique())
                        
                        X_new[ col_names ] = pd.get_dummies(  data.to_frame())  
                       # X_new[ col_names ] = ct.fit_transform(  data.to_frame()  )

                else :
                    # μ«μ λ°μ΄ν° μ²λ¦¬
                    
                    X_new[name] = data

            scaler = MinMaxScaler()
            X_new = scaler.fit_transform(X_new)

            st.dataframe(X_new)
            st.text('')
            st.text('')
            st.subheader('WCSSλ₯Ό μν ν΄λ¬μ€ν°λ§ κ°―μλ₯Ό μ ν')

            if X_new.shape[0] < 10 :
                default_value = X_new.shape[0]
            else :
                default_value = 10

            max_number = st.slider('μ΅λ κ·Έλ£Ή μ ν', 2, 20, value=default_value)
            wcss = []
            for k in np.arange(1, max_number+1) :
                kmeans = KMeans(n_clusters= k, random_state=5)
                kmeans.fit(X_new)
                wcss.append( kmeans.inertia_ )

            # st.write(wcss)

            fig1 = plt.figure()
            x = np.arange(1, max_number+1)
            plt.plot( x, wcss )
            plt.title('The Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig1)


            # μ€μ λ‘ κ·Έλ£Ήνν  κ°―μ μ ν!
            # k = st.slider('κ·Έλ£Ή κ°―μ κ²°μ ', 1, max_number)

            k = st.number_input('κ·Έλ£Ή κ°―μ κ²°μ ', 1, max_number)

            kmeans = KMeans(n_clusters= k, random_state=5)

            y_pred = kmeans.fit_predict(X_new)

            df['Group'] = y_pred

            st.dataframe( df.sort_values('Group')  )


            df.to_csv('result.csv')
            st.text('')
            st.text('')
            # μΈν°λν°λΈνκ² λ§λ€κΈ°
            # μ«μλ₯Ό μλ ₯νλ©΄ κ·Έ μ«μμ κ·Έλ£Ή λ°μ΄ν°νλ μλ§ λνλΈλ€
            st.markdown('##### Gruoping μ«μλ₯Ό μλ ₯νλ©΄, κ·Έ μ«μμ κ·Έλ£Ή λ°μ΄ν°νλ μλ§ λ³΄μ¬μ€λλ€')
            num = st.number_input('μ«μλ₯Ό μλ ₯νμΈμ', 1, k - 1, value= 1)
            st.dataframe(df[df['Group'] == num])
            


if __name__ == '__main__' :
    main()