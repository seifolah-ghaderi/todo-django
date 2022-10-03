from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsDeveloper, IsProjectManager
from .serializers import *
from rest_framework.views import APIView
from todos.models import Task, Project
from .serializers import TaskUpdateSerializer

from rest_framework.decorators import permission_classes
# Create your views here.
class TaskListView(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, IsDeveloper)


class TaskDetialsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskDetailSerializer

class TaskAssignView(generics.UpdateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TaskUpdateSerializer

class ProjectsListView(generics.ListCreateAPIView):
    queryset = models.Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = (IsAuthenticated, IsProjectManager)


class ProjectTaskListView(ListAPIView):
    # permission_classes = [IsAnonymousForPost]
    """
     An endpoint for get list G center (models)
     """
    serializer_class = UserTasksSerializer
    lookup_url_kwarg = "proj_id"

    def get_queryset(self):
        pid = self.kwargs.get(self.lookup_url_kwarg)
        return Task.objects.filter(project_id=pid)


class ProjectUserTaskListView(ListAPIView):
    # permission_classes = [IsAnonymousForPost]
    """
     An endpoint for get list G center (models)
     """
    serializer_class = UserTasksSerializer
    lookup_url_proj = "p_id"
    lookup_url_userid = "u_id"

    def get_queryset(self):
        pid = self.kwargs.get(self.lookup_url_proj)
        uid = self.kwargs.get(self.lookup_url_userid)
        print(f"user id:{uid}")
        tasks = Task.objects.filter(project_id=pid, assignee__id=uid)
        print(f"count of list:{tasks.count()}")
        return tasks

@api_view(['PUT'])
@permission_classes((IsProjectManager, ))

def update_task(request, pk=None):
    
    task = models.Task.objects.get(id=pk)
    serializer = TaskUpdateSerializer(task, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    
    asignees = []

    for assigne_id in request.data.get('users'):
        try:
            asignee = User.objects.get(id=assigne_id)
            asignees.append(asignee)
        except:
            raise NotFound()
    
    task.assignee.set(asignees)
    return Response(data=serializer.data, status=status.HTTP_200_OK)