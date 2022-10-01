from django.urls import path


from .views import  TaskDetialsView, TaskListView , ProjectTaskListView,ProjectsListView,ProjectUserTaskListView

urlpatterns = [
    path('tasks/', TaskListView.as_view()),
    path('task/<int:pk>/', TaskDetialsView.as_view()),
    path('projects/',ProjectsListView.as_view()),
    path('projects/<int:proj_id>/tasks',ProjectTaskListView.as_view()),
    path('projects/<int:p_id>/tasks/user/<int:u_id>', ProjectUserTaskListView.as_view()),

]
"""
required api
/account/login
/account/signup

#list of tasks in a project
/projects/<int:pk>/tasks

#list of user tasks in project
/projects/<int:pk>/<int:pk>/tasks/user/<int:pk>
"""