from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
  
def tasks(request):
  return render(request, 'draw/tasks.html', {})

def largeboard(request):
  return render(request, 'draw/largeboard.html', {})

def largeboarddragon(request):
  return render(request, 'draw/largeboarddragon.html', {})

def tasksdragon(request):
  return render(request, 'draw/tasksdragon.html', {})