# 내가 입력한 댓글 좋아요를 평균이상일까?

## 크롤링

키워드 입력
크롤링 수 입력

유튜브의 제목을 상위부터 크롤링 수만큼 키워드와 관련된 내용을 크롤링해서 보여준다

크롤링할때 유튜브 영상의 토큰값으로 접근하고 댓글 토큰값으로 한번더 접근해서 영상의 정보를 가져온다

영상 정보를 클릭하면 해당 영상 댓글의 문장과 날짜 좋아요수 다음 댓글 토큰을 재귀로 넘겨주면서 모두 가져온다

댓글의 댓글도 가져온다

csv 파일로 저장을 원하면 저장을 한다

## 전처리

특수문자 영어문자 모두제거 사이드 공백제거
좋아요가 평균이상이면 1 미만이면 0을 대입

## 모델링

LSTM 모델을 사용
문장과 날짜는 X값 좋아요는 y값으로 지정해서 학습

학습이 완료된 모델을 저장한다

# 페이지 설명

* home에서는 크롤링을 할지 모델 학습을 할지 선택할 수 있다
* 모델이 없다면 크롤링을 해서 모델학습에 사용할 수 있는 데이터를 만들수 있다

![main.PNG](/img/main.PNG)

* crawling에서는 크롤링하고 싶은 키워드와 몇개 가져올지 개수를 입력한다

![crawling_search](/img/crawling_search.PNG)  

* '사이코지만 괜찮아'라는 키워드로 상위 5개의 영상 정보를 가져온다

![crawling_title_list.PNG](/img/crawling_title_list.PNG)  

![crawling_comment_list.PNG](/img/crawling_comment_list.PNG)  

![main_2.PNG](/img/main_2.PNG)  
![model_predict.PNG](/img/model_predict.PNG)  
![model_predict_2.PNG](/img/model_predict_2.PNG)  
![model_training_csv.PNG](/img/model_training_csv.PNG)  
![model_training_csv_2.PNG](/img/model_training_csv_2.PNG)  
