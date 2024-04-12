from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    task_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return self.content
