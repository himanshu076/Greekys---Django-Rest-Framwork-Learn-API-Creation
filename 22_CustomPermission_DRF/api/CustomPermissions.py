from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            # return super().has_permission(request, view)
            return True
        return False