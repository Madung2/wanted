# wanted_pre_onboarding

## 1.Code Covention

#### 코드 컨벤션
변수 : snake case
함수 : snake case
클래스 : pascal case

#### 깃허브

feat : 새로운 기능 추가/수정/삭제
enhan : 기존 코드에 기능을 추가하거나 기능을 강화할 때
refac : 코드 리팩토링,버그 수정
edit : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)




## 2. Problem Solving
### 1번 문제
#### 요구사항:
필요한 모델을 구성하고 알맞은 데이터를 담아주어서 정상적으로 데이터 저장이 이루어지도록 함


#### 구현과정:
채용 항목들이 포함된 모델을 생성
항목들을 업로드할 수 있도록 serializer와 view 생성
position과 tech_stack의 경우엔 string으로 들어온 값이 pk값으로 입력되도록 views.py 단위에서 변환해줌.

<hr>

### 2번 문제

#### 요구사항:
생성한 데이터를 수정이 되도록 구현. (모든 데이터가 들어가지 않아도 수정이 되어야함)


#### 구현과정:
views.py에 put 함수 생성.
serializer를 통과하도록 함.
특정 데이터만 넣어도 수정될 수 있도록 partial=True 지정

<hr>

### 3번 문제

#### 요구사항:
생성한 데이터가 삭제가 되도록 구현.

#### 구현과정:
views.py에서 delete() 함수로 데이터 삭제
<hr>

###  4번 문제

#### 요구사항:
생성한 전체 데이터를 볼 수 있도록 구현


#### 구현과정:

get 메소드를 사용
serializer를 통과시 SerializerMethodField()를 사용해서 회사명, 포지션명 등이 표시되도록 함.

<hr>

### 5번 문제

#### 요구사항:
채용 상세 페이지에 해당하는 데이터를 볼 수 있도록 구현


#### 구현과정:
4번과 다른 views.py를 만들어서 get 메소드를 사용함.
recruitment pk값을 지정받고 해당하는 쿼리만 get으로 받음. 


<hr>
