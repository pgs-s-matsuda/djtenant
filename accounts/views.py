from django.contrib.auth import views as auth_views

from myapp.models import Domain


class LoginView(auth_views.LoginView):
    def get_success_url(self):
        request = self.request
        user = request.user
        tenant = user.tenant
        url = super().get_success_url()
        if tenant:
            domain = Domain.objects.get(tenant=tenant)
            url = f'https:\\{domain}{url}'
            pass
        return url
    pass
