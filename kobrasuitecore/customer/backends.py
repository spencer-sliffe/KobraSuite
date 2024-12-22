from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission
from django.db.models import Q

class RolePermissionBackend(ModelBackend):
    """
    Custom backend that merges a user's Role-based permissions with the
    permissions Django already provides (via groups or user_permissions).
    """

    def get_role_permissions(self, user_obj):
        """
        Return a set of 'app_label.codename' strings from all the Permissions
        attached to any Role that the user has.
        """
        if not hasattr(user_obj, 'roles'):
            return set()

        # Gather all Permission objects across all roles
        role_permissions_qs = Permission.objects.filter(
            role__users=user_obj  # Because Role has M2M with Permission, but also user M2M with Role
        ).distinct()

        perms = {
            f"{perm.content_type.app_label}.{perm.codename}"
            for perm in role_permissions_qs
        }
        return perms

    def get_all_permissions(self, user_obj, obj=None):
        """
        Merge the default ModelBackend permissions with the role-based perms.
        """
        if not user_obj.is_active or user_obj.is_anonymous:
            return set()

        # Start with the built-in Django perms from groups or user_permissions
        builtin_perms = super().get_all_permissions(user_obj, obj=obj)

        # Add role-based perms
        role_perms = self.get_role_permissions(user_obj)

        return builtin_perms.union(role_perms)

    def has_perm(self, user_obj, perm, obj=None):
        """
        Check membership in the full set of user + role-based permissions.
        """
        if user_obj.is_superuser:
            return True
        return perm in self.get_all_permissions(user_obj, obj=obj)
