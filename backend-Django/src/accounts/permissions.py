from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    ## the first method called
    def has_permission(self, request, view):

        # check if the user is an admin
        #
        return True


    ## the second method called if object passed
    def has_object_permission(self, request, view, obj):

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # # Write permissions are only allowed to the owner of the snippet.
        return (obj.user == request.user or request.user.is_superuser)

class IsCustomAdmin(permissions.BasePermission):

    ## the first method called
    def has_permission(self, request, view):

        # check if the user is an admin
        #
        print("Hellloo")
        return bool(request.user and request.user.is_superuser)

class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_superuser)