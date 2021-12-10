from django.urls import path
from rooms import views as room_views

app_name = "core"

# For Fucntion Based View
# urlpatterns = [path("", room_views.all_rooms, name="home")]

# For Class Based view
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
