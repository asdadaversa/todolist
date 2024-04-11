from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskCreateForm, TagCreateForm
from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:

    list_tasks = Task.objects.all()

    context = {
        "list_tasks": list_tasks,
       }

    return render(request, "task/index.html", context=context)


def tags(request: HttpRequest) -> HttpResponse:

    tags_list = Tag.objects.all()

    context = {
        "tags_list": tags_list,
       }

    return render(request, "task/tags.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'task/task_form.html'
    success_url = reverse_lazy("task:index")
    form_class = TaskCreateForm


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy("tag:index")
    form_class = TagCreateForm
