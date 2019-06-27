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

from common.mymako import render_json, render_mako_context
from blueking.component.shortcuts import get_client_by_request
import base64
from models import *
import json
import xlrd


def croissantOne(request):
    """
    模拟一首页
    """
    return render_mako_context(request, "/croissant/croissantOne.html")


def execute_record(request):
    """
    执行记录页面
    """
    return render_mako_context(request, "/croissant/executeRecord.html")


def get_business(request):
    """
    获取业务
    """
    client = get_client_by_request(request)
    result = client.cc.search_business()
    return render_json(result)


def get_hosts(request):
    """
    获取主机列表
    """
    client = get_client_by_request(request)
    result = client.cc.search_host()

    # print result
    return render_json(result)


def execute_script(request):
    """
    执行脚本
    """
    # 接收并处理数据
    post = request.POST
    files = request.FILES

    ip_data = post["ipList"].split(',')
    ip_list = list()
    for item_ip in ip_data:
        ip_list.append(dict(ip=item_ip, bk_cloud_id=0))

    script_param = post["scriptWord"]
    bk_biz_id = post["businessId"]

    re_list = list()
    temp_dict = dict()
    for key in files:
        _file = files.get(key)
        temp_dict["filename"] = _file.name
        temp_dict['file_content'] = _file.file.read()
        re_list.append(dict(filename=temp_dict["filename"]))

    # 执行数据
    client = get_client_by_request(request)

    encode_param = base64.b64encode(script_param)
    encode_content = base64.b64encode(temp_dict['file_content'])
    kwargs = {
        "bk_biz_id": bk_biz_id,
        "script_param": encode_param,
        "script_content": encode_content,
        "account": "root",
        "ip_list": ip_list
    }
    result = client.job.fast_execute_script(kwargs)

    result_data = result["data"]
    job_instance_name = result_data["job_instance_name"]
    job_instance_id = result_data["job_instance_id"]

    # 保存数据
    task_val = dict()
    task_val["job_instance_name"] = job_instance_name
    task_val["job_instance_id"] = job_instance_id
    task_val["script_name"] = temp_dict["filename"]
    task_val["bk_biz_id"] = bk_biz_id
    task_val["ip"] = ip_list
    task_val["script_param"] = encode_param
    task_val["script_content"] = encode_content
    TaskDetail(**task_val).save()

    return render_json({"result": u"已启动作业：%s (%s)" % (job_instance_name, job_instance_id)})


def get_execute_details(request):
    execute_details = TaskDetail.objects.all()
    print execute_details

    re_list = list()
    for item in execute_details:
        temp_dict = dict()
        temp_dict["job_instance_name"] = item.job_instance_name
        temp_dict["job_instance_id"] = item.job_instance_id
        temp_dict["bk_biz_id"] = item.bk_biz_id
        temp_dict["script_name"] = item.script_name
        temp_dict["execute_time"] = str(item.execute_time)
        re_list.append(temp_dict)

    return render_json({"result": re_list})


def get_execute_log(request, **kwargs):
    """
    获取日志
    """
    client = get_client_by_request(request)
    result = client.job.get_job_instance_log(request.GET)

    if result['data'][0]['is_finished']:
        log_content = result['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
    else:
        log_content = "作业未执行完！"

    print log_content
    # return render_json({"result": log_content})
    return render_json(log_content)


def croissant_two(request):
    """
    模拟二首页
    """
    return render_mako_context(request, "/croissant/croissantTwo.html")


def get_all_users(request):
    """
    获取所有用户
    """
    client = get_client_by_request(request)
    result = client.bk_login.get_all_users()

    data = result["data"]
    re_list = list()
    for item in data:
        re_dict = dict()
        re_dict["name"] = item["bk_username"]
        re_list.append(re_dict)

    return render_json(re_list)


def create_work_two(request):
    """
    创建待办任务和关联内容
    """
    post = request.POST
    bk_biz_id = post["bk_biz_id"]
    bk_biz_name = post["bk_biz_name"]
    template_type = post["template_type"]
    template_name = post["template_name"]
    option_num = post["dialog_option"]

    files = request.FILES
    for key in files:
        temp_dict = dict()
        _file = files.get(key)
        temp_dict["bk_biz_id"] = bk_biz_id
        temp_dict["bk_biz_name"] = bk_biz_name
        temp_dict["template_type"] = template_type
        temp_dict["template_name"] = template_name
        temp_dict["option_num"] = option_num
        temp_dict["creator"] = request.user.username
        # temp_dict["status"] = "待操作"
        task_two = TaskTwo(**temp_dict)
        task_two.save()

        # 读取excel
        data_excel = xlrd.open_workbook(file_contents=_file.file.read())
        table = data_excel.sheets()[0]
        rows = table.nrows
        for i in range(1, rows):
            _row = table.row_values(i)
            excel_temp_dict = dict()
            excel_temp_dict["father_id"] = task_two.id
            excel_temp_dict["index"] = _row[0]
            excel_temp_dict["options"] = _row[1]
            excel_temp_dict["description"] = _row[2]
            excel_temp_dict["creator"] = _row[3]
            excel_temp_dict["finish_time"] = "-"
            excel_temp_dict["ok_user"] = "-"
            excel_temp_dict["status"] = "未完成"
            excel_temp_dict["handle"] = 0  # 默认为待处理
            task_excel_two = TaskDetailTwo(**excel_temp_dict)
            task_excel_two.save()

    return render_json({"OK": "创建成功", "NO": "创建失败"})


def resolve_work(request):
    """
    处理页面
    """
    return render_mako_context(request, "/croissant/resolveWork.html")
