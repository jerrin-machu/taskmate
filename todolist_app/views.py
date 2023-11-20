from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TodoList
from todolist_app.forms import TodoListForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
#global all_tasks
@login_required
def todolist(request):
    global all_tasks
    if request.method == "POST":
        
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,("New Task Added"))
            return redirect('todolist')
        
    else:
            print('I hamjdkfjdjslfjsjriouweoiujrojswio')
            all_tasks = TodoList.objects.filter(manage=request.user)
            paginator = Paginator(all_tasks, 5)
            page = request.GET.get('page')
            all_tasks= paginator.get_page(page)
            
    return render(request, 'todolist.html', { 'all_tasks' : all_tasks })

def about(request):
    context = {
        'about_text':"welcome from about page"
    }
    
    return render(request, 'about.html',context)
@login_required    
def contact(request):
    context = {
        'contact_text':"welcome from contact page"
    }
    return render(request, 'contact.html',context)

def delete_task(request,taskid):
    task = TodoList.objects.get(pk=taskid)
    if task.manage == request.user:
        task.delete()
    else:
        messages.error(request, ("Access Restricted! You don't have permission"))
    return redirect('todolist')

def edit_task(request,taskid):
    if request.method == "POST":
       task = TodoList.objects.get(pk=taskid)
       
       form = TodoListForm(request.POST or None, instance=task)
       if form.is_valid():
           form.save()
           messages.success(request,("Task Edited"))
           return redirect('todolist')
    else:
        task = TodoList.objects.get(pk=taskid)
        return render(request, 'edit_task.html', {'task':task})
    
def complete_task(request,taskid):
    task = TodoList.objects.get(pk=taskid)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("Access Restricted! You don't have permission"))
    return redirect('todolist')


def pending_task(request, taskid):
    task = TodoList.objects.get(pk=taskid)
    if task.manage == request.user:
        task.done = False
        task.save()
    else:
        messages.error(
            request, ("Access Restricted! You don't have permission"))
    return redirect('todolist')


def index(request):
    context = {
        'index_text': "welcome from home page"
    }
    return render(request, 'index.html', context)
    