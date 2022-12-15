# project_name

프로젝트 파이팅!!


### Back 커밋 순서

[B-001] 기본 세팅   
[B-002] foods 앱 모델   
[B-003] accounts 앱 모델    
[B-004] community 앱 모델   
[B-005~7] selializers 작성    
[B-008] 회원가입, 로그인, 로그아웃    
[B-009] 회원정보 조회 및 수정     


<br><br>

### URL
|          기능          |                   URL                    |
| :--------------------: | :--------------------------------------: |
|        회원가입        |            /accounts/signup/             |
|         로그인         |             /accounts/login/             |
| 회원정보 조회 및 수정  |  /accounts/user/profile/<str:username>/  |
| 전체 식단 조회 및 생성 |         /accounts/user/history/          |
|     개별 식단 CRUD     | /accounts/user/history/<int:history_pk>/ |
|     전체 메뉴 조회     |               /foods/menu/               |
|    전체 레시피 조회    |              /foods/recipe/              |


⭐식단 입력 받을 때 menuname 반드시 공백 기준으로 각각의 메뉴 나눈 하나의 문자열로 입력해주세요!!     
ex) `마라탕 꿔바로우`
