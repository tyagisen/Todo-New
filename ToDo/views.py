from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *


def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, "ToDo/index.html", context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {"form": form}

    return render(request, 'ToDo/update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'ToDo/delete.html', context)
