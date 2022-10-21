# 프로젝트 주간 페어 프로그래밍 - 영화 리뷰 + 댓글 + 회원 관리 커뮤니티 개발 프로젝트

## 과정

- [목표](#목표)
- [준비 사항](#준비-사항)
- [요구사항](#요구-사항)
- [프로젝트 결과 완성본](#프로젝트-결과-완성본)
- [프로젝트 후기](#프로젝트-후기)

## 목표

- 페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다.
- 아래 조건을 만족해야합니다.
  - CRUD 구현
  - Staticfiles 활용 정적 파일(이미지, CSS, JS) 다루기
  - Django Auth 활용 회원 관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)
  - Media 활용 동적 파일 다루기
  - 모델간 1 : N 관계 매핑 코드 작성 및 활용
    - 유저 - 리뷰
    - 리뷰 - 댓글
    - 유저 - 댓글

## 준비 사항

### ▶ 페어프로그래밍 가이드

- 개발 환경 설정을 제외한 모든 토픽 개발은 아래 순서에 따라 진행합니다.
1. [로컬/드라이버] main 브랜치에서 개발 토픽에 해당하는 브랜치 생성 및 브랜치 전환
   
   ```bash
   # 브랜치 생성 & 전환
   $ git checkout -b [토픽 브랜치명]
   
   # git checkout [브랜치명] : 브랜치를 전환합니다.
   # git checkout -b [브랜치명] : 브랜치를 생성하고 전환합니다. 동일한 브랜치가 있으면 오류가 발생합니다.
   ```

2. [로컬/드라이버] 토픽 개발

3. [로컬/드라이버] 토픽 개발 후 동일한 이름의 원격 저장소 브랜치에 Commit & Push
   
   ```bash
   $ git add .
   
   $ git commit -m '커밋 메세지'
   
   $ git push origin [토픽 브랜치명]
   ```

4. [원격/드라이버] 토픽 브랜치 병합
   
   - 깃허브 PR 생성(토픽 브랜치 → main 브랜치)
   
   - 브랜치 병합(토픽 브랜치 → main 브랜치)

   - 토픽 브랜치 삭제

5. [로컬/전체] main 브랜치 전환 후 Pull
   
   ```bash
   # main 브랜치로 전환
   $ git checkout main
   
   # main 브랜치 Pull
   $ git pull origin main
   ```

6. [로컬/드라이버] 토픽 브랜치 삭제
   
   ```bash
   # 토픽 브랜치 삭제
   $ git branch -d [토픽 브랜치명]
   ```

7. 드라이버 변경 후 1번 부터 시작

### ▶ 깃 브랜치 명령어

```bash
# 브랜치 생성 & 전환
$ git checkout -b [브랜치명]

# 브랜치 전환
$ git checkout [브랜치명]

# 브랜치 삭제
$ git branch -d [브랜치명]

# 브랜치 이름 변경
$ git branch -m [기존 브랜치명] [변경할 브랜치명]
```

## 요구 사항

### 1. Git 설정

> branch `main`

- 원격 저장소 생성

- 콜라보레이터 초대

- 로컬 저장소 깃 초기화
  
  ```bash
  $ git init
  ```

- 로컬 저장소 `.gitignore` 생성 
  
  ```bash
  $ touch .gitignore
  ```

- `.gitignore` 작성
  
  - 아래 사이트 입력창에 필요한 언어 & 프레임워크 & 환경 입력 후 생성
  - `https://www.toptal.com/developers/gitignore/`

## 2. 장고 개발환경 설정

> branch `setup-django`

- Django 프로젝트 생성
  
  - 가상환경 생성 & 실행
  - 필요한 패키지 설치

- 패키지 목록 저장
  
  ```bash
  $ pip freeze > requirements.txt
  ```

- Django 프로젝트 생성 
  
  ```bash
  $ django-admin startproject config .
  ```

## 3. 회원가입

> branch `accounts/signup`

> 앱 App

- 앱 이름 : accounts

> 모델 Model

- 모델 이름 : User
- Django `AbstractUser` 모델 상속

> 폼 Form

- Django 내장 회원가입 폼 `UserCreationForm`을 상속 받아서 `CustomUserCreationForm` 작성
- 해당 폼은 아래 필드만 출력합니다.
  - username
  - password1
  - password2

> 기능 View

- 회원가입
  - `POST` `http://127.0.0.1:8000/accounts/signup/`
  - `CustomUserCreationForm`을 활용해서 회원가입 구현

> 화면 Template

- 회원가입 페이지
  
  - `GET` `http://127.0.0.1:8000/accounts/signup/`
  - 회원가입 폼

## 4. 로그인

> branch `accounts/login`

> 폼 Form

- 로그인
  - Django 내장 로그인 폼 `AuthenticationForm` 활용

> 기능 View

- 로그인
  - `POST` `http://127.0.0.1:8000/accounts/login/`
  - `AuthenticationForm`를 활용해서 로그인 구현

> 화면 Template

- 로그인 페이지
  
  - `GET` `http://127.0.0.1:8000/accounts/login/`
  - 로그인 폼
  - 회원가입 페이지 이동 버튼


## 5. 로그아웃

> branch `accounts/logout`

> 기능 View

- 로그아웃
  
  - `POST` `http://127.0.0.1:8000/accounts/logout/`


## 6. 리뷰 생성

> branch `reviews/create`

> 앱 App

- 앱 이름 : reviews

> 모델 Model

- 모델 이름 : Review
- 모델 필드

  | 이름         | 역할      | 필드         | 속성                |
  | ---------- | ------- | ---------- | ----------------- |
  | title      | 리뷰 제목   | Char       | max_length=80     |
  | content    | 리뷰 내용   | Text       |                   |
  | movie_name | 영화 이름   | Char       | max_length=80     |
  | grade      | 영화 평점   | Integer    |                   |
  | created_at | 리뷰 생성시간 | DateTime   | auto_now_add=True |
  | Updated_at | 리뷰 수정시간 | DateTime   | auto_now=True     |
  | writer     | 리쥬 작성자  | ForeignKey |                   |

> 기능 View

- 데이터 생성
  - `POST` `http://127.0.0.1:8000/reviews/create/`

> 화면 Template

- 리뷰 작성 페이지
  
  - `GET` `http://127.0.0.1:8000/reviews/create/`
  - 리뷰 작성 폼


## 7. 리뷰 목록 조회

> branch `reviews/index`

> 기능 View

- 데이터 목록 조회
  - `POST` `http://127.0.0.1:8000/reviews/`

> 화면 Template

- 리뷰 목록 페이지 
  
  - `GET` `http://127.0.0.1:8000/reviews/`
  - 리뷰 목록 출력
  - 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동


## 8. 리뷰 정보 조회

> branch `reviews/detail`

> 기능 View

- 데이터 정보 조회
  - `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/`

> 화면 Template

- 리뷰 정보 페이지
  
  - `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/`

- 해당 리뷰 정보 출력

- 수정 / 삭제 버튼
  - 수정 / 삭제 버튼은 해당 리뷰 작성자에게만 출력합니다.

- 댓글 작성 폼
  - 댓글 작성 폼은 로그인 사용자에게만 출력합니다.

- 댓글 목록


## 9. 리뷰 정보 수정

> branch `reviews/update`

> 기능 View

- 데이터 수정
  - `POST` `http://127.0.0.1:8000/reviews/<int:review_pk>/update/`

- 데이터를 생성한 사용자만 수정할 수 있습니다.

> 화면 Template

- 리뷰 수정 페이지
  
  - `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/update/` 
  - 리뷰 수정 폼


## 10. 리뷰 삭제

> branch `reviews/delete`

> 기능 View

- 데이터 삭제
  
  - `POST` `http://127.0.0.1:8000/reviews/<int:review_pk>/delete/`

- 데이터를 생성한 사용자만 삭제할 수 있습니다.


## 11. 댓글 작성
 
> branch `comments/create`

> 앱 App

- reviews 앱에 구현

> 모델 Model

- 모델 이름 : Comment
- 모델 필드

  | 이름         | 역할     | 필드         | 속성            |
  | ---------- | ------ | ---------- | ------------- |
  | review     | 참조 리뷰  | ForeignKey |               |
  | writer     | 댓글 작성자 | ForeignKey |               |
  | content    | 댓글 내용  | Char       | max_length=80 |
  | created_at | 작성일    | DateTime   | auto_now_add  |

> 기능 View

- 데이터 생성
  - `POST` `http://127.0.0.1:8000/reviews/<int:review_pk>/comments/`

- 로그인한 사용자만 댓글을 생성할 수 있습니다.

> 화면 Template

- 리뷰 작성 페이지
  
  - `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/`
  - 리뷰 작성 폼

- 리뷰 정보 조회 페이지 하단에 댓글 작성 폼 출력

## 12. 댓글 목록 조회
 
> branch `comments/index`

> 기능 View

- `POST` `http://127.0.0.1:8000/reviwes/<int:review_pk>/`


> 화면 Template
  
- `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/`
  
- 리뷰 정보 조회 페이지 하단에 댓글 목록 출력


## 13. 댓글 삭제
 
> branch `comments/delete`

> 기능 View

- `POST` `http://127.0.0.1:8000/reviews/<int:review_pk>/comments/<int:comment_pk>/delete/`

- 데이터를 생성한 사용자만 삭제할 수 있습니다.

> 화면 Template
  
- `GET` `http://127.0.0.1:8000/reviews/<int:review_pk>/`
  
- 각 댓글에 리뷰 삭제 버튼 추가
  - 삭제 버튼은 해당 댓글 작성자에게만 출력합니다.




## 프로젝트 결과 완성본

> 영화 리뷰 + 회원 관리 페이지

![](gif/django_project_1021_animation.gif)

## 프로젝트 후기

오늘도 두 분과 함께 페어 프로그래밍을 진행하였다. 한 명씩 번갈아가며 드라이버를 맡아 코드를 짰다. 회원가입/로그인/로그아웃/리뷰글/댓글을 차례대로 먼저 구현을 한 후, [Notefolio](https://notefolio.net/) 사이트를 참고하여 디자인을 입혔다. 

오늘 새롭게 하나 배운 것은 articles/index.html 에서 썸네일 위에 마우스를 올렸을 때 이미지가 동일 범위 내에서 살짝 커지는 것을 구현해 보았다. 또한 articles/detail.html 에서 제목 뒷 배경에 업로드한 이미지를 넣었는데, 이 과정에서 상당히 난항을 겪었다. 글 제목을 `position:absolute;`로 배경 위에 올린 후, 부트스트랩 container를 먹이려고 했으나 적용되지 않아 차선책으로 left 스타일을 px이 아닌 `left:30%;`로 변경해서 해결했다.