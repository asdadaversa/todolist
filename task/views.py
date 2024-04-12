from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskCreateForm, TagCreateForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 4
    template_name = "task/index.html"

    def get_queryset(self):
        queryset = Task.objects.order_by("task_done")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["list_tasks"] = context["object_list"]

        return context

class TagListView(generic.ListView):
    model = Tag
    paginate_by = 4
    template_name = "task/tag.html"

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["tags_list"] = context["object_list"]

        return context


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task/task_form.html"
    success_url = reverse_lazy("task:index")
    form_class = TaskCreateForm


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("task:tags")
    form_class = TagCreateForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task:index")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("task:tags")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tags")


def task_complete_undo(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if task.task_done is False:
        task.task_done = True
    else:
        task.task_done = False
    task.save()
    return redirect("task:index")
