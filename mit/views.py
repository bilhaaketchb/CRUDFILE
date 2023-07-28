from django.shortcuts import render


# Create your views here.
from .models import Student
def home(request):
    d = Student.objects.all()
    return render(request, 'homepage.html',{"d":d})


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')
        # print(name,school,email)
        data = Student(name=name,school=school,email=email)
        data.save()
    return render(request, 'homepage.html')
