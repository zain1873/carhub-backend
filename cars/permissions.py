from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    
    - SAFE_METHODS (GET, HEAD, OPTIONS): Allowed for everyone (authenticated or anonymous)
    - Unsafe methods (POST, PUT, PATCH, DELETE): 
        - POST: Handled by IsAuthenticatedOrReadOnly (requires authentication)
        - PUT/PATCH/DELETE: Only allowed for the owner of the object
    
    IMPORTANT: This permission class must be used together with IsAuthenticatedOrReadOnly
    to ensure that only authenticated users can create objects.
    """

    def has_permission(self, request, view):
        """
        Called for ALL requests (list, create, retrieve, update, destroy).
        Returns True to allow the request to proceed to has_object_permission
        for detail views, or to allow list/create actions.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Called ONLY for detail views (retrieve, update, partial_update, destroy).
        This is where we check object-level permissions.
        
        Note: This method is NOT called for list() or create() actions.
        """
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        # Read-only requests allowed for everyone (including anonymous users)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions: only allow the owner
        # Check if user is authenticated first to avoid comparing None with obj.owner
        if not request.user or not request.user.is_authenticated:
            return False

        # Only the owner can update or delete
        return obj.owner == request.user
