# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rbac import models
from django.shortcuts import render,HttpResponse

# Create your views here.

class ValidatePer:

    def __init__(self,actions):
        self.actions = actions

    def add(self):
        return "add" in self.actions

    def change(self):
        return "change" in self.actions

    def view(self):
        return "view" in self.actions

    def delete(self):
        return "delete" in self.actions

def user(request):
    user_obj = models.User.objects.all()
    per =ValidatePer(request.action_list)
    menu_dict = request.session.get("menu_per_dict",None)
    print menu_dict
    return render(request,"user.html",locals())

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = models.User.objects.filter(username=username,password=password).first()
        if user_obj:
            request.session["user_id"] =user_obj.id
            return HttpResponse("登录成功")
        return HttpResponse("登录失败")
    return render(request,"login.html",locals())