from curses.ascii import BS
from email.policy import default
from django.db import models
from .utils.baseModels import BaseModel
from todos.utils.enums import ProjectStatus
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):

    p_status=(
    (ProjectStatus.DRAFT.value,ProjectStatus.DRAFT.name),
    (ProjectStatus.INPROGRESS.value,ProjectStatus.INPROGRESS.name),
    (ProjectStatus.DONE.value,ProjectStatus.DONE.name),
    (ProjectStatus.ARCHIVED.value,ProjectStatus.ARCHIVED.name),
    )

    title=models.CharField(max_length=300)
    desc=models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=p_status, default=ProjectStatus.DRAFT)
    developers = models.ManyToManyField(User,related_name="developers")

    def __str__(self) -> str:
        return self.title.title()

class Task(models.Model):
    title=models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="project")
    assignee = models.ManyToManyField(User,related_name="assignees")

    desc=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False,blank=True)


    def __str__(self) -> str:
        return self.title.title()
