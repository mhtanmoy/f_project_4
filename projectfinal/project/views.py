from .models import Contact, courses

from django.shortcuts import render

from .models import regester

# Create your views here.
def index(request):
    return render(request, 'project/index.html')


def index2(request):
    return render(request, 'project/test.html')


def index3(request):
    return render(request, 'project/test2.html')


def index4(request):
    if request.method == 'POST':
        your_name = request.POST.get('name')
        your_email = request.POST.get('email')
        subject = request.POST.get('subject')
        your_message = request.POST.get('message')

        var_contact = Contact(name=your_name, email=your_email, subject=subject, message=your_message)
        var_contact.save()
        return render(request, 'project/thanks.html')
    else:
        return render(request, 'project/contact.html')


def index5(request):
    return render(request, 'project/about.html')


def index6(request):
    var_1 = courses.objects.all()
    return render(request, 'project/courses.html', {'var_1': var_1})



