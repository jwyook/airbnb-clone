#  For Function Based View
# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import EmptyPage, Paginator
# from . import models


# For Class Based View
from typing import List
from django.views.generic import ListView
from . import models

# Create your views here.

#  Function based view
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)

#     try:
#         rooms = paginator.page(int(page))
#         return render(
#             request,
#             "rooms/home.html",
#             context={"page": rooms},
#         )
#     except EmptyPage:
#         return redirect("/")


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"
