from django.views.generic import TemplateView
from .models import ConnectionModel


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['connections'] = ConnectionModel.objects.order_by('ip')
        return context
