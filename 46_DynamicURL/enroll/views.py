from django.shortcuts import render

# Create your views here.
def home(request, check):
    print(check)
    return render(request, 'enroll/home.html', {'ch':check})

# def show_details(request, my_id):
    # student = {'id':my_id}
#     return render(request, 'enroll/show.html', student)

def show_details(request, my_id=1):
    if my_id == 1:
        student = {'id': my_id, 'name':'Rohan'}
    if my_id == 2:
        student = {'id': my_id, 'name':'SonamAli'}
    if my_id == 3:
        student = {'id': my_id, 'name':'Rohan'}
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id=1, my_subid=5):
    if my_id == 1 and my_subid == 5:
        student = {'id': my_id, 'name':'Rohan', 'info':'Sub Details'}
    if my_id == 2 and my_subid == 6:
        student = {'id': my_id, 'name':'SonamAli', 'info':'Sub Details'}
    if my_id == 3 and my_subid == 7:
        student = {'id': my_id, 'name':'Rohan', 'info':'Sub Details'}
    return render(request, 'enroll/show.html', student)