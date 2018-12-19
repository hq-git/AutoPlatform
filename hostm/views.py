from django.shortcuts import render,redirect,HttpResponse
from hostm import models
# Create your views here.

user_obj = None

def login(request):
    # print(request.method)
    errormsg = ''
    if request.method == "POST":
        # print(request.POST)
        u = request.POST.get('username',None)
        p = request.POST.get('password',None)
        global user_obj
        user_obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if user_obj:    #查到符合要求用户信息
            return redirect('/index')
        errormsg = '用户名/密码错误'
    return render(request,"login.html",{'errormsg':errormsg})

def index(request):
    if not user_obj:
        return redirect('/login')

    return render(request,"index.html",{'user_obj':user_obj})
