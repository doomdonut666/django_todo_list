from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.
# Task list render func
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# Task create func
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'todo/task.form.html', {'form': form, 'title': 'Create task'})
