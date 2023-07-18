from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'homepage.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')
        # print(name,school,email)
    return render(request, 'homepage.html')
