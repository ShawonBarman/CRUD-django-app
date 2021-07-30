from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

#This function will add new student info and show all students info
def add_show_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            register = User(name=name, email=email, password=password)
            register.save()
            return redirect("home")
    else:
        form = StudentRegistration()
    student = User.objects.all()
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'crud/index.html', context)

#This function is for update/edit a particular student info
def update_info(request,id):
    if request.method == "POST":
        stud = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=stud)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        stud = User.objects.get(pk=id)
        form = StudentRegistration(instance=stud)
    return render(request,"crud/update_student_data.html",{'form':form})

#This function will delete a particular student info
def delete_info(request, id):
    if request.method == "POST":
        stud = User.objects.get(pk=id)
        stud.delete()
        return redirect("home")