from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
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


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task:index")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreateForm
    success_url = reverse_lazy("tag:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tag:index")
