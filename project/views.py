from django.shortcuts import render,redirect
from .models import Project
# Create your views here.


def project_list(request):
    projects = Project.objects
    return render(request, 'project_list.html', {'projects': projects})


def add(request):
    if request.method == 'GET':
        return render(request, "add.html")
    elif request.method == 'POST':
        name = request.POST['项目名称']
        describe = request.POST['项目描述']
        price = request.POST['金额']
        
        project = Project()
        project.name = name
        project.describe = describe
        project.price = price
        
        project.save()
        return redirect('项目列表')
