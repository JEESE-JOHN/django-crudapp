from django.shortcuts import render, redirect
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age']
        )
        return redirect('/')
    return render(request, 'add.html')

def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()
        return redirect('/')
    return render(request, 'edit.html', {'student': student})

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')
