from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from LoginInfo.models import UserInfo
# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):
    return render(request,"register.html")


def registercheck(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    phone = request.POST.get("phone")
    email=request.POST.get("email")
    try:
        if UserInfo.objects.get(username=username):
            return redirect("/register")
    except UserInfo.DoesNotExist:
        user=UserInfo()
        user.username = username
        user.password = password
        user.phone = phone
        user.email=email
        user.save()
        return redirect("/login")


# def login(request):
#     if request.session.has_key("islogin"):
#         return redirect("/index")
#     else:
#         if "username" in request.COOKIES:
#             username=request.COOKIES["username"]
#         else:
#             username=""
#         return render(request,"login.html",{"username":username})



def loginrequire(view_func):
    def wrapper(request,*args,**kwargs):
        if request.session.has_key("islogin"):
            return redirect("/index")
        else:
            return view_func(request,*args,**kwargs)
    return wrapper


def logincheck(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")
    u=UserInfo.objects.filter(username=username,password=password)[0]
    if u:
        print (u.username)
        response=render(request,"index.html",{"u":u})
        if remember=="on":
            response.set_cookie("username",username,max_age=10)

        request.session["islogin"]=True
        request.session.set_expiry(10)
        return response
    else:
        return redirect("/login")



