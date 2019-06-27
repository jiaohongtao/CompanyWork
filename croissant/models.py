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

from django.db import models
from django.utils import timezone
import datetime
import uuid


class TaskDetail(models.Model):
    job_instance_name = models.CharField(u"执行名称", max_length=255, unique=True)
    script_name = models.CharField(u"脚本名称", max_length=64)
    script_param = models.CharField(u"参数名称", max_length=64)
    script_content = models.CharField(u"脚本内容", max_length=255)
    ip = models.CharField(u"ip", max_length=255)
    # task_type = models.CharField(u"任务类型", max_length=64)
    bk_biz_id = models.SmallIntegerField(u"业务id")
    job_instance_id = models.SmallIntegerField(u"执行id")
    execute_time = models.DateTimeField(u"执行开始时间", auto_now=True)

    # execute_time = models.DateTimeField(u"执行开始时间", default=datetime.datetime.now())

    class Meta:
        db_table = "task_detail"


def get_uuid():
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    s_uuid = ''.join(l_uuid)
    return s_uuid


class TaskTwo(models.Model):
    bk_biz_id = models.SmallIntegerField(u"业务id")
    bk_biz_name = models.CharField(u"业务名称", max_length=64)

    id = models.CharField(u"主键", primary_key=True, default=get_uuid(), max_length=64)
    template_name = models.CharField(u"模板名称", max_length=255)
    option_num = models.CharField(u"操作识别号", max_length=64)
    template_type = models.CharField(u"模板类型", max_length=64)
    optioner = models.CharField(u"可操作者", max_length=64)
    creator = models.CharField(u"创建者", max_length=64)
    create_time = models.DateTimeField(u"创建时间", default=str(datetime.datetime.now()))
    status = models.CharField(u"状态", max_length=20, default="待操作")

    class Meta:
        db_table = "task_two"
        verbose_name = "模拟二任务"


class TaskDetailTwo(models.Model):

    id = models.CharField(u"主键", default=get_uuid(), max_length=64, primary_key=True)
    father_id = models.CharField(u"外键", max_length=64)
    index = models.CharField(u"序号", max_length=10)
    options = models.CharField(u"操作事项", max_length=255)
    description = models.CharField(u"备注", max_length=255)
    finish_time = models.CharField(u"完成时间", max_length=64)
    creator = models.CharField(u"负责人", max_length=20)
    ok_user = models.CharField(u"确认人", max_length=20)
    status = models.CharField(u"状态", max_length=20)
    handle = models.BooleanField(u"操作状态")

    class Meta:
        db_table = "task_detail_two"
        verbose_name = "模拟二任务详情"
