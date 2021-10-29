# Airbnb Clone

Cloning Airbnb with Python, Django...

# How to activate Server

python manage.py migrate

python manage.py runserver

# How to make superuser

python manage.py createsuperuser

# 2.4 Django Migrations

맨 처음 project를 생성하면 우리의 data base는 empty상태이다.
이로인하여 경고가 빨간색 경고가 발생하고 있다.

migrate 명령을 실행하여 경고 메시지에 있던 앱들이 필요로 하는 테이블들을 생성하면된다.
=>python manage.py migrate

migrate를 통해 admin, auth, contenttypes, sessions 앱이 사용하는 테이블이 생성되었음을 알려준다. 이렇게 테이블이 생성되면 Django는 어떤 항목들을 읽어들어야 할지 알게된다.
이로인하여 오류가 해결된다.

# 2 review

Django는 framework이다. 변경하려 들지말고, 있는 그대로 받아들어야 한다.

1. admin.py는 어드민페이지에 해당 되며, 추후 model등을 등록할때 이용된다.
2. models.py는 우리가 데이터베이스를 정의 하는 곳 이다. 이렇게 SQL문을 직접 다루지 않고 파이썬 코드를 통해 간접적으로 구현하는 방식을 ORM 이라 부른다.

3. views.py는 웹서버 구동시 사용될 logic을 담당한다.
4. urls.py는 url과 view를 mapping 한다.

# 4 Room App

중복된 코드부분을 막기위해(다른 app에서도 사용가능한) core라는 app을 따로 만든다.
이 core app은 DB에 등록되기를 원하지 않는다.
이 core를 상속받은 다른 class 들이 DB에 등록되도록 해야한다.

이때 사용하는 것 이 abstract model 이다. DB상에 등록되지 않는 model이다.
=> 확장을 위한 용도로 사용된다.

class Meta:
abstract = True

# 4.1 Room App

국가 설정을 위해 choices 와 같은 구현을 해야한다.
이때 모든 나라이름을 직접 복붙 하는 것 이 아닌, django-countries 라이브러리를 이용하면된다.

1. pipenv install django-countries
2. django-countries 를 settings.py 에 app을 등록시켜 준다.

import의 추천 순서

1. python 관련
2. django
3. 제3의 라이브러리들
4. user의 custom 들

ForeignKey: 이 key는 외부의 모델과 연결을 한다.
(ps 추가 설명은 이곳을 https://blog.naver.com/zbqmgldjfh/222372147081 )

auto_now_add=True => model 처음 생성시 날짜 생성
auto_now=True => model 수정시 날짜 업데이트

# 4.4 Room App

on_delete=models.CASCASE
=> 해당 모델 삭제시 이와 연관된 모든 정보를 삭제함
예를 들어보면, 어떤 게시물을 삭제하면 여기에 달려있는 모든 댓글들 또한 삭제되는 것
