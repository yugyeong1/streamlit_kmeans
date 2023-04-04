<br/>
<div align="center">

## K-means 클러스터링 알고리즘을 이용하여서, 데이터를 Gruoping 해주는 대시보드 개발   

</div>  
<br/>
<div align="cecnter">

### 🌟 Platfroms & languages 🌟

</div>

<div>
  <img src="https://img.shields.io/badge/Python-007396?style=flat&logo=Python&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter Notebook-E34F26?style=flat&logo=Jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat&logo=Amazon AWS&logoColor=white" />
  <img src="https://img.shields.io/badge/EC2-FF9900?style=flat&logo=Amazon EC2&logoColor=white" />
</div>  

<br/>

<div align="left">

### 🛠 Tools 🛠

</div>  

<div>
<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat&logo=Visual Studio Code&logoColor=white"/> 
<img src="https://img.shields.io/badge/Github-000000?style=flat&logo=Github&logoColor=white"/>
</div>

<br/> 






#### 📌 사용한 라이브러리

<div>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white"/> 
<img src="https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/matplotlib-EBAF00?style=flat&logo=matplotlib&logoColor=white"/>
<img src="https://img.shields.io/badge/scikit-learn-F7931E?style=flat&logo=scikit-learn&logoColor=white"/> 
<img src="https://img.shields.io/badge/Numpy-013243?style=flat&logo=Numpy&logoColor=white"/> 

</div>

<br/>

### 📌 알고리즘 설명

이 앱은 K-Means Clustering 을 알고리즘을 이용하여서,  
주어진 데이터를 k 개의 클러스터로 묶어서 나타내는 알고리즘 앱 입니다.  
  
Nan 데이터가 존재할 경우 dropna() 로 데이터를 제거하였고,  
가장 적합한 기준점을 찾기 위해 wcss 를 이용하였습니다.  
문자열 데이터가 존재할 경우 처리하기 위해서, Label-Encoding 과 One-Hot Encoding 을 이용하였습니다.  
클러스터링 후 사용자가 원하는 그룹 데이터를 선택하여서 확인할 수 있습니다.  



<br/>


### 📌 AWS EC2 배포, Github Actions 이용

AWS 의 EC2 서버를 이용하여서, 웹 대시보드를 서버에 배포 하였고,
  
Github Actions 기능을 이용하여서, 코드 수정사항을 Github 에 push 할 때마다  
putty 에 접속하지 않아도, 자동으로 배포할 수 있도록 하였습니다.  


<br/>

<div align="left">

### 📌 Link


http://ec2-3-36-60-118.ap-northeast-2.compute.amazonaws.com:8503/


</div>  

<br/>
<br/>


### 📷 앱 대시보드 화면

<br/>

#### (1) 대시보드에 클러스터링 하고자 하는 csv 파일을 업로드 한다.  

![image](https://user-images.githubusercontent.com/104052659/208858334-5d10ec83-80e5-4fa3-87c1-005f4d14736b.png)

<br/>

#### (2) 그룹핑 할 때 이용하고자 하는 컬럼( X )을 선택한다.  

![image](https://user-images.githubusercontent.com/104052659/208858673-400aeb5e-16c1-481b-9034-0483b29a4170.png)

<br/>

#### (3) 최적의 기준점을 찾기 위한 WCSS 차트를 그려서, 클러스터링 갯수를 선택한다.  

![image](https://user-images.githubusercontent.com/104052659/208859449-1ad49c0a-7018-404c-8af2-4709f6032b78.png)


#### (4) 그룹핑할 갯수를 선택한다.

<br/>

![image](https://user-images.githubusercontent.com/104052659/208859736-496e279c-f204-46fa-8d71-7bb9e4c86691.png)


#### (5) Gruoping 숫자를 입력하면, 그 숫자의 그룹 데이터프레임만 나타낸다.

<br/>


![image](https://user-images.githubusercontent.com/104052659/208859901-d79551bd-6714-4dc0-a17a-548f12b9c9cf.png)


