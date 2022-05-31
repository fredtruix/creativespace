from sqlite3 import paramstyle
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Room, Topic, Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

# room = [
#     {'id':1, 'name':'lets learn python'},
#     {'id':2, 'name':'design with me'},
#     {'id':3, 'name':'frontend developer'},
# ]


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q))[0:5]
    p = Paginator(rooms, 1)
    page = request.GET.get('page')
    rooms = p.get_page(page)
    topics = Topic.objects.all()[0:]
    room_count = rooms.end_index()
    # room = Room.objects.filter(participants=request.user)
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q))[0:4]
    context = {
        "rooms":rooms,
        "topics":topics,
        "room_count" : room_count,
        "room_messages": room_messages,
    }
    return render(request, 'base/home.html', context)


def rooms(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get("body")
        )
        joinedroom = room.participants.add(request.user)
        return redirect("room", pk=room.id)
    context = {
        "room":room,
        "room_messages": room_messages,
        "participants": participants,
        }
    return render(request, 'base/room.html', context)





@login_required(login_url="login")
def JoinRoomView(request, pk):
    room = Room.objects.get(id=pk)
    room.participants.add(request.user)
    return redirect("room", pk=room.id)

@login_required(login_url="login")
def LeaveRoomView(request, pk):
    room = Room.objects.get(id=pk)
    room.participants.remove(request.user)
    return redirect("room", pk=room.id)




@login_required(login_url="login")
def CreateRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('home')
    context = {
        "form":form,
        "topics":topics
        }
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def UpdateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse('You are not allowed Here!!')
    if request.method == "POST":
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get("name")
        room.topic = topic
        room.description = request.POST.get("description")
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('home')
    context = {
        "form":form,
        "topics":topics,
        "room":room
        }
    return render(request, 'base/room_form.html', context)




@login_required(login_url="login")
def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed Here!!') 

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":room})



@login_required(login_url="login")
def DeleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not allowed Here!!')

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj":message})


def UploadMessageView(request, pk):
    room = Room.objects.get(id=pk)


    if request.method == "POST":
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get("body")
        )
        return redirect("room", room.id)
    context = {
        "room":Room,
        'upload':"upload"
    }
    return render(request, 'base/room_message.html', context)



def TopicView(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    topics = Topic.objects.filter(name__icontains=q)
    
    context = {"topics":topics}
    return render(request, 'base/topics.html', context)


def ActivityView(request):
    room_messages = Message.objects.all()
    p = Paginator(room_messages, 2)
    page = request.GET.get('page')
    room_messages = p.get_page(page)
    context = {
        "room_messages":  room_messages
    }
    return render(request, 'base/activity.html', context)




 
def HelpfulView(request, pk, room):
    message = Message.objects.get(id=pk)
    message.helpful += 1
    message.save()
    room = Room.objects.get(id=room)
    return redirect('room', room.id)


def NothelpfulView(request, pk, room):
    message = Message.objects.get(id=pk)
    message.not_helpful += 1
    message.save()
    room = Room.objects.get(id=room)
    return redirect('room', room.id)