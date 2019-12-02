from django.shortcuts import render,redirect
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_word = request.POST['密码']
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is None:
            return render(request, 'login.html', {'错误':'用户名或密码错误'})
        else:
            auth.login(request, user)
            return redirect('项目列表')