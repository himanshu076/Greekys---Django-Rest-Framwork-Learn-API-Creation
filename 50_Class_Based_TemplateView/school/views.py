from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

# class HomeTemplateView(TemplateView):
#     template_name = 'school/home.html'

class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # first way to show context data
        context['name'] = 'Sonam'
        context['roll'] = 101

        print(kwargs)

        # Second way to show context data
        # context = {'name':'Sonam', 'roll':101}
        return context
