from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
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


def task_complete(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if task.task_done is False:
        task.task_done = True
        task.save()
    return redirect("task:index")


def task_undo(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    if task.task_done is True:
        task.task_done = False
        task.save()
    return redirect("task:index")

# def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
#     if request.method == "POST":
#         user = request.user
#         if not user.is_authenticated:
#             raise ValidationError("User has to be authenticated!")
#         post_id = request.POST.get("post_id")
#         content = request.POST.get("content")
#         post = Post.objects.get(pk=post_id)
#         Commentary.objects.create(
#             user=user,
#             post=post,
#             content=content,
#         )
#         return redirect("blog:post-detail", pk=post_id)
#
# @login_required()
# def car_delete_driver(
#         request: HttpRequest,
#         pk: int,
# ) -> HttpResponse:
#     Car.objects.get(id=pk).drivers.remove(request.user)
#     return redirect("taxi:car-detail", pk)
