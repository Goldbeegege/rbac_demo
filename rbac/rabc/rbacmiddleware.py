# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2018/11/1 9:02

from django.utils.deprecation import MiddlewareMixin
import re
from permission import GetPermission
from config import WHITE_LIST
from django.shortcuts import redirect,HttpResponse
from rbac import models

class PermissionMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        self.current_path = request.path_info
        print self.current_path
        if not self.get_white_list():
            if not self.is_login(request):
                return redirect("/login/")
            ret = self.get_per(request)
            return ret
        return None


    def get_per(self,request):
        """
        获取用户权限
        :param request:
        :return:
        """
        per_obj = GetPermission(request)
        per_obj.get_permission()
        permissions_dict = request.session.get("permission", [])
        for per in permissions_dict.values():
            for item in per["url"]:
                new_item = "^%s$" % item
                ret = re.match(new_item, self.current_path)
                if ret:
                    request.action_list = per["action"] if item in per["url"] else None
                    return None
        return HttpResponse("没有权限。。。")

    def get_white_list(self):
        """
        获取白名单
        :return:
        """
        for url in WHITE_LIST:
            url = "^%s$"%url
            ret = re.match(url,self.current_path)
            if ret:
                return True
        return False

    def is_login(self,request):
        """
        判断是否登录
        :param request:
        :return:
        """
        user_id = request.session.get("user_id",None)
        if user_id:
            user = models.User.objects.filter(id=user_id).first()
            request.user = user
            return True
        return False