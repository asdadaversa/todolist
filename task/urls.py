from django.urls import path

from task.views import TaskListView, tags, TaskCreateView, TagCreateView, TaskUpdateView, TagUpdateView, TaskDeleteView, \
    TagDeleteView, task_complete, task_undo

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", tags, name="tags"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/complete", task_complete, name="task-complete"),
    path("task/<int:pk>/undo", task_undo, name="task-undo"),

    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),


]

app_name = "task"
