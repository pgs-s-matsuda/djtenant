from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'myapp/index.html'


class App1IndexView(generic.TemplateView):
    template_name = 'app1/index.html'


class App2IndexView(generic.TemplateView):
    template_name = 'app2/index.html'
