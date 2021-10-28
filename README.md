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
