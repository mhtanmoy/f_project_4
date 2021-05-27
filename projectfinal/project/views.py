from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from .models import *
from .forms import *

# Create your views here.
def index(request):
    count= courses.objects.all().filter(archive=False).count()
    User = get_user_model()
    users = User.objects.all().count()
    return render(request, 'project/index.html',{'courses':count,'users':users})


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
    var_1 = courses.objects.all().filter(archive=False)
    return render(request, 'project/courses.html', {'var_1': var_1})



def controlpanel(request):
    form= courses.objects.all().filter(archive=False)
    return render(request, 'control_panel/control_project.html',{'form':form})

def allarchive(request):
    form= courses.objects.all().filter(archive=True)
    return render(request, 'control_panel/allarchive.html',{'form':form})


def editproject(request, pk):
    projects = courses.objects.get(id=pk)
    form = Projectform(instance=projects)
    if request.method == 'POST':
        form = Projectform(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('controlpanel')
    return render(request,'control_panel/editproject.html', {'form':form})

def archiveproject(request, pk):
    projects = courses.objects.get(id=pk)
    form = Archiveform(instance=projects)
    if request.method == 'POST':
        form = Archiveform(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('controlpanel')
    return render(request,'control_panel/archiveproject.html', {'form':form})


def deleteproject(request,pk):
    obj=get_object_or_404(courses,id=pk)
    if request.method =='GET':
        obj.delete()
        return redirect('controlpanel')

def createproject(request):
    form = Projectform()
    if request.method == 'POST':
        form = Projectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('controlpanel')
    return render(request,'control_panel/createproject.html', {'form':form})