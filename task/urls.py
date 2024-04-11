from django.urls import path

from task.views import index, tags, TaskCreateView, TagCreateView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", tags, name="tags"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="task-create"),
]

app_name = "task"
