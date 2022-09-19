from multiprocessing import context
from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Let\'s Learn Python'},
    {'id':2, 'name':'AI Room'},
    {'id':3, 'name':'Design with me'}
]

# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, "base/home.html", context)

def room(request,pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {'room': room}
    return  render(request, "base/room.html", context)