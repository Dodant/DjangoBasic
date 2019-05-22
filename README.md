# Django Guide
## MVC & MVT - Design Pattern
* M : Model
	* 안전하게 데이터를 저장
* V : View
	* 데이터를 적절하게 유저에게 보여줌
* C : Control, T : Template(Django)
	* 사용자의 입력과 이벤트에 반응하여 Model과 View를 업데이트

<img width="617" alt="Screen Shot 2019-05-18 at 3 13 33 PM" src="https://user-images.githubusercontent.com/20153952/58165174-31a66980-7cc2-11e9-8f84-24561c4f0cab.png">
ref) WSGI - Web Service Gateway Interface

## Project와 App
* 프로젝트 생성
$ django-admin startproject 프로젝트명
* App 생성
$ ./manage.py startapp App명

## settings.py
* DEBUG
	* 디버그 모드 설정
	* SECURITY WARNING: don't run with debug turned on in production!
* INSTALLED_APPS
	* pip로 설치한 앱 또는 본인이 만든 app 추가
* MIDDLEWARE
	* request와 response 사이의 주요기능 레이어
* TEMPLATE
	* django template 관령 설정, 실제 뷰(html, 변수)
* DATABASES
	* DB엔진의 연결 설정
* STATIC_URL
	* 정적 파일의 URL(CSS, JavaScript, Images, etc.)

## manage.py
* 프로젝트 관리 명령어 모음
* 주요 명령어
	* startapp - 앱 생성
	* runserver - 서버 실행
	* createsuperuser - 관리자 생성
	* makemigrations app - app의 모델 변경사항 체크
	* migrate - 변경사함을 DB에 반영
	* shell - 쉘을 통해 데이터를 확인
	* collectstatic - static파일을 한 곳에 모음
* ex )  ./manage.py runserver 0.0.0.0:8080
