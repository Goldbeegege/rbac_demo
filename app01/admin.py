# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rbac import models

# Register your models here.

admin.site.register(models.PermissionGroup)
admin.site.register(models.Role)
admin.site.register(models.User)
admin.site.register(models.Permission)