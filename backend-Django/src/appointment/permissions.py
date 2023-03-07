

from rest_framework.permissions import IsAdminUser



class IsStaff(BasePermission):

    def has_permission(self, request, view):

        return True