from django.views.generic import TemplateView
from .models import Eventos, Palavras, Informes, QuemSomos

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):

        print('passou por aqui GET!')
        context = super(IndexView, self).get_context_data(**kwargs)
        context['eventos'] = Eventos.objects.all()
        context['palavras'] = Palavras.objects.all()
        context['informes'] = Informes.objects.all()
        context['quemsomos'] = QuemSomos.objects.all()

        return context