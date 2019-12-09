from django.shortcuts import render,redirect,get_object_or_404
from .models import Project
# Create your views here.


def project_list(request):
    projects = Project.objects
    return render(request, 'project_list.html', {'projects': projects})


def detail(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    return render(request, 'detail.html', {'project': project})


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

        project.owner = request.user
        
        project.save()
        return redirect('项目列表')
