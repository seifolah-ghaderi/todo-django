from django.contrib import admin

# Register your models here.
from .models import Task , Project

#admin.site.register(Task)
#admin.site.register(Project)

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title","project", "get_assignees"]

    def get_assignees(self, obj):
        return ",".join([p.username for p in obj.assignee.all()])

admin.site.register(Task,TaskAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "get_developers"]

    def get_developers(self, obj):
        return ",".join([p.username for p in obj.developers.all()])


admin.site.register(Project,ProjectAdmin)