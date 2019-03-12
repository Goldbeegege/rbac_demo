# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    #用户信息表
    username = models.CharField(max_length=64,verbose_name=u"用户名")
    password = models.CharField(max_length=32)
    role = models.ManyToManyField(to="Role",verbose_name=u"权限")

    def __str__(self):
        return self.username


class Role(models.Model):
    #角色表
    name = models.CharField(max_length=32,verbose_name=u"角色名称")
    permission = models.ManyToManyField(to="Permission")

    def __str__(self):
        return self.name

class Permission(models.Model):
    #权限表
    name = models.CharField(max_length=32,verbose_name=u"权限名称")
    url = models.CharField(max_length=32)
    action = models.CharField(max_length=32,default="")
    group = models.ForeignKey(to="PermissionGroup")

    def __str__(self):
        return self.name

class PermissionGroup(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
