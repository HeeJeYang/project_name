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
[B-010] 유저 식단 CRUD 
[B-011] 메뉴, 레시피, 재료 조회 및 검색   
[B-012] 레시피 찜 기능    
[B-013] 사용자 맞춤 메뉴 추천 알고리즘 (사용자 최근 1주일 식단)   
[B-014] 게시판 댓글 CRUD   
[B-015] 게시물 검색 (제목/유저네임&닉네임)   


<br><br>

### URL
|              기능               |                   URL                    |
| :-----------------------------: | :--------------------------------------: |
|            회원가입             |            /accounts/signup/             |
|             로그인              |             /accounts/login/             |
|      회원정보 조회 및 수정      |  /accounts/user/profile/<str:username>/  |
|     전체 식단 조회 및 생성      |         /accounts/user/history/          |
|          개별 식단 RUD          | /accounts/user/history/<int:history_pk>/ |
|         전체 메뉴 조회          |               /foods/menu/               |
|        전체 레시피 조회         |              /foods/recipe/              |
|        개별 레시피 조회         |      /foods/recipe/<int:recipe_pk>       |
|            메뉴 검색            |           /foods/menu/search/            |
|       레시피 검색 (재료)        |          /foods/recipe/search/           |
|       레시피 찜 (좋아요)        |   /foods/recipe/like/<int:recipe_pk>/    |
|            추천 메뉴            |          /foods/menu/recommend/          |
| 전체 게시물 조회 및 게시물 생성 |           /community/articles/           |
| 개별 게시물 RUD & 추천 (좋아요) |  /community/articles/<int:article_pk>/   |
| 개별 댓글 RUD |  /community/comments/<int:comment_pk>/   |
| 특정 게시물에 댓글 생성 |  /community/articles/<int:article_pk>/comments/   |
| 카테고리 별 인기 게시물 조회 |  /community/articles/popular/   |
| 게시물 검색 (제목) |  /community/articles/search/post/   |
| 게시물 검색 (유저네임/닉네임) |  /community/articles/search/user/   |

⭐식단 입력 받을 때 menuname 반드시 공백 기준으로 각각의 메뉴 나눈 하나의 문자열로 입력해주세요!!     
ex) `마라탕 꿔바로우`
