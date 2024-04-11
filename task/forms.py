from django import forms

from task.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))

    class Meta:
        model = Task
        fields = ("content", "deadline", "task_done", "tags")


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
