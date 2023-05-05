# from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect

from todo_app.models import Todo

def todo_create(request):
    print(request.method)
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
        print(request.POST)
        title = request.POST["title"]
        Todo.objects.create(title=title)
        return HttpResponseRedirect("/")


def todo_list(request):
    todos = Todo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos},
    )

def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "GET":
            return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo}, #context dictionary
        )
        
    else:
        todo.title=request.POST["title"]
        todo.save()
        return HttpResponseRedirect("/")


def todo_delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return HttpResponseRedirect("/")


