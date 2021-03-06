from django.contrib.auth.mixins import UserPassesTestMixin
from crm.models import Organisation

# ownership check can be moved to separate function in parent class


class OrganisationViewPermCheck(UserPassesTestMixin):
    """ View allows to check ownership + group on the object
        It is needed because Group can access object, but only if it 
        is owned by current user. Not to create custom backend and stay 
        free to modify each PermCheck it's put separate
    """

    def test_func(self):
        req = self.request
        user = req.user
        u_groups = [str(i) for i in user.groups.all()]
        # Ownership check
        if 'Salesman' in u_groups and 'Manager' not in u_groups:
            org_id = self.kwargs['pk']
            org = Organisation.objects.get(id=org_id)
            owner = org.owned_by
            if owner.id == user.id:
                return True
        if 'Manager' in u_groups:
            return True
        return False

# class OrganisationEditPermCheck(UserPassesTestMixin):
#     def test_func(self):
