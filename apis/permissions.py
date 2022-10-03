from rest_framework import permissions


class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='Developer'):
            return True
        return False


class IsProjectManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='ProjectManager'):
            return True
        return False

