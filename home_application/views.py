# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from models import HostDisk
import json
from blueking.component.shortcuts import get_client_by_user, get_client_by_request
import base64


# from django.forms.models import model_to_dict


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html', {"ssssss": "11111111",
                                                                             "AAA": [{'QQQ': "22222"}]
                                                                             })


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def host_disk(request):
    """
    主机磁盘信息
    """
    hostAll = HostDisk.objects.all()
    re_list = list()

    for item in hostAll:
        temp_dict = dict()
        temp_dict['name'] = item.name
        temp_dict['ip'] = item.ip
        temp_dict['os'] = item.os
        temp_dict['disk'] = item.disk
        temp_dict['create_time'] = item.create_time
        re_list.append(temp_dict)
        # re_list.append(model_to_dict(item))

    # print re_list
    return render_mako_context(request, '/home_application/host_disk.html', {"hostAll": re_list})


def host_create(request):
    """
    主机磁盘信息添加
    """
    body = json.loads(request.body)
    obj = HostDisk(**body)
    obj.save()

    return render_json(body)


# def fast_exec_script(request, kwargs):
def fast_exec_script(request):
    kwargs = {
        "bk_biz_id": 2,
        "script_content": base64.b64encode("echo 'This is a test.'"),

        "script_timeout": 1000,
        "account": "root",
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "10.20.10.4"
            }
        ],
    }

    print kwargs
    user = "admin"
    client = get_client_by_user(user)
    result = client.job.fast_execute_script(kwargs)
    print result
    return render_json(result)


def send_mail(request):
    client = get_client_by_request(request)

    # kwargs = {
    #     # "receiver": "Tera1996,jht1007760854",
    #     "receiver__username": "Tera1996,jht1007760854",
    #     "data": {
    #         "heading": "blueking alarm",
    #         "message": "This is a test.",
    #         "date": "2017-02-22 15:36",
    #         "remark": "This is a test!"
    #     }
    # }

    kwargs = {
        "receiver": "yanweijian_tt@163.com",
        "sender": "18332120276@163.com",
        "title": "This is a Test",
        "content": "<html>Welcome to Blueking</html>",
    }

    result = client.cmsi.send_mail(**kwargs)

    print result
    return render_json(result)


def get_user_infos(request):
    client = get_client_by_request(request)

    result = client.bk_login.get_all_users({"bk_role": 0})
    print result

    return render_json(result)

# def host_list(request):
#     """
#     主机磁盘信息查询
#     """
#     hostAll = HostDisk.objects.all()
#     # obj = HostDisk.objects.filter()
#     # data = json.loads(obj)
#     re_list = list()
#
#     for item in hostAll:
#         re_list.append(model_to_dict(item))
#         # temp_dict = dict()
#         # temp_dict['name'] = item.name
#         # temp_dict['ip'] = item.ip
#         # temp_dict['os'] = item.os
#         # temp_dict['disk'] = item.disk
#         # re_list.append(temp_dict)
#     # return render_json(obj)
#     return render_mako_context(request, 'home_application/host_disk.html', {"hostAll": re_list})
