# Airbnb Clone

Cloning Airbnb with Python, Django...

# How to activate Server

python manage.py migrate

python manage.py runserver

# How to make superuser

python manage.py createsuperuser

# How to make New Folder

1. Kill the Server
2. django-admin startapp NAME

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

# 7.0 Models And Querysets

1. dir VS vars
   => https://www.geeksforgeeks.org/difference-between-dir-and-vars-in-python/

2. Django shell을 통하여 query set(객체의 list)을 이용하여 DB의 객체들에 접근할 수 있음

예를 들어 from users.models import User 을 한후,
User.object 에 접근하면 model class의 Manager를 확인할 수 있는데, 이를 통해
우리가 DB에 접근 가능하도록 도와줌

(ps. 메니저는 model class를 통하여 접근하는 것 이지, model의 인스턴스를 통하여 접근하는 것 이 아님. table과 record의 차이를 생각할 것

3. SET
   q라는 Question model(1) 에 ForeignKey로 연결된 a라는 Answer model(N) 이 있다고 해보자.
   a를 통하여 Question을 얻고 싶다면 다음과 같이 쉽게 얻을 수 있다.
   => a.question

Answer 모델 객체인 a에는 question 속성이 있으므로 a를 통해 질문을 찾는 것은 매우 쉽다. 그렇다면 반대로 질문을 통해 답변을 찾을 수 있을까? Question 모델에는 답변 속성이 없어서 불가능할 것 같지만 실제로는 가능하다.

answer_set 을 사용하면 된다.
=> q.answer_set.all()

Question 모델과 Answer 모델처럼 서로 연결되어 있으면
연결모델명\_set과 같은 방법으로 연결된 데이터를 조회할 수 있다.

4. related_name
   related_name 을 통하여 user(1) 입장에서 room(N)을 찾을수도 있음.
   room models에서 related_name 을 적어주면 그 이름을 통하여
   user에서 room을 역참조 할 수 있음

5. ManyToMany의 관계에서는 그냥 갖어오면 됨
   room.amenities.all() 처럼

6. query_set manager
   메니저 로부터 all(), filter(), count() 등을 사용할 수 있다.

7. rooms 와 amenities 는 ManyToMany의 관계로 구성되 있다.
   따라서 a라는 amenity 객체를 하나 얻으면.
   a.room_set.all() 과 같은 방식으로
   a 입장에서 a라는 amenity를 포함하고 있는 rooms의 정보를 얻을 수 있다.

8. related_name은 가리키고 있는 대상을 위한 용도 임을 기억하자!

9. count_photos 함수를 만드는 것이 목표
   count_photos() 의 parameter를 보면 obj가 있음.
   이는 우리가 count_photos함수에 넘겨주는 Room 객체를 의미함.

Room(1) 객체는 Photo(N)와 ForeignKey 관계를 갖고 있음
또한 related_name="photos"를 설정했기에, Room의 입장에서 photo에 접근하기 용이함

return obj.photos.count()를 통하여 사진의 수를 반환함
=> Room.photos를 연 후 메니저를 통하여 count() 기능을 이용한다 생각

10. 모든 Item들에 적용하기
    RoomType, Facility, Amenity, 등등 모두 ItemAdmin class를 상속받아 확장시킨 class들 임.
    따라서 ItemAdmin에서 list_display 에 관한 코드 작성시 전체에 적용됨
