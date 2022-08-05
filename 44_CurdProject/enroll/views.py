from django.shortcuts import redirect, render, HttpResponseRedirect
from enroll.forms import StudetRegistration
from enroll.models import User


# SuperUser ID & Password - (admin, admin)

# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
    if request.method == 'POST':
        form = StudetRegistration(request.POST)
        if form.is_valid():
            # first method to save data...
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            form = StudetRegistration()

            # Second Method to save data...
            # form.save()
    else:
        form = StudetRegistration()

    stu = User.objects.all()
    template = 'enroll/addandshow.html'
    return render(request, template, {'form': form, 'stu':stu})

# This Function will update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudetRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudetRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': form})

# This Function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
