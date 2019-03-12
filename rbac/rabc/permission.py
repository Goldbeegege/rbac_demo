# -*-coding:utf-8-*-
# @author: JinFeng
# @date: 2018/10/31 21:26

from rbac import models

class GetPermission:
    def __init__(self,request):
        self.request = request
        self.user_id = request.session.get("user_id",None)

    def get_permission(self):
        role = models.User.objects.filter(id=self.user_id).values(   "role__permission__action",
                                                                     "role__permission__group_id",
                                                                     "role__permission__url",
                                                                     "id"
                                                                  ).distinct()
        print self.user_id
        permission_dict = {}
        for each in role:
            pid = each["role__permission__group_id"]
            if each["role__permission__group_id"] not in permission_dict:
                permission_dict[pid]= {}
                permission_dict[pid]["url"] = [each["role__permission__url"],]
                permission_dict[pid]["action"] = [each["role__permission__action"],]
            else:
                permission_dict[pid]["url"].append(each["role__permission__url"])
                permission_dict[pid]["action"].append(each["role__permission__action"])

        self.request.session["permission"] = permission_dict
        menu_per_dict = {}
        group = models.Role.objects.filter(user__id=self.user_id).values("permission__name",
                                                                         "permission__url",
                                                                        "permission__group__name"
                                                                         )
        for item in group:
            pid = item["permission__group__name"]
            if pid not in menu_per_dict:
                menu_per_dict[pid] =[]
                menu_per_dict[pid].append((item["permission__name"],item["permission__url"]))
            else:
                menu_per_dict[pid].append((item["permission__name"],item["permission__url"]))
        self.request.session["menu_per_dict"] = menu_per_dict
        print menu_per_dict