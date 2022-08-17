from urllib import request
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from school.forms import ContactForm

# Create your views here.
def homefun(request):
    return render(request, 'school/home.html')


class HomeClassView(View):
    def get(sef, request):
        return render(request, 'school/home.html')

########################################################

def aboutfun(request):
    context = {'msg': 'Welcone to Himanshu Learning World!...'}
    return render(request, 'school/about.html', context)


class AboutClassView(View):
    def get(self, request):
        context = {'msg': 'Welcone to Himanshu Learning World!...'}
        return render(request, 'school/about.html', context)

########################################################

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return HttpResponse('Thankyou for submitted !!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return HttpResponse('Thankyou for submitted !!')

########################################################

def newsfun(request, template):
    template = template
    context = {'info':'CBI enquery why GreekyShows earn less money'}
    return render(request, template, context)


class NewsClassView(View):
    template = ''
    def get(self, request):
        context = {'info':'CBI enquery why GreekyShows earn less money'}
        return render(request, self.template, context)

########################################################