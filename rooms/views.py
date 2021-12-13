#  For Function Based View
# from math import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import EmptyPage, Paginator
# from . import models


# For Class Based View
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
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


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
