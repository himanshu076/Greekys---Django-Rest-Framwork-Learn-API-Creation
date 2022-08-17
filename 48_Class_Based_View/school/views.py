from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
# Function Based View
def myview(request):
    return HttpResponse('<h1>Function Based View</h1>')

# Class Based View
class MyView(View):
    name = 'Sonam'
    # name = ''       # it mandatrey to writ because we gave this variable value in URL.
    def get(self, request):
        return HttpResponse('<h1>Class Based View- GET</h1>')
        # return HttpResponse(self.name)

class MyViewChildClass(MyView):
    def get(self, request):
        return HttpResponse(self.name)
