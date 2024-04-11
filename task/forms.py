from django import forms

from task.models import Task, Tag


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"


class TagCreateForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
