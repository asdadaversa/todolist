from django.urls import path

from task.views import TaskListView, tags, TaskCreateView, TagCreateView, TaskUpdateView, TagUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", tags, name="tags"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "task"
