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

        ## the owner only can modified

        return True
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        
        # if self.has_permission(request, view)
        # # Write permissions are only allowed to the owner of the snippet.
        # return obj.user == request.user