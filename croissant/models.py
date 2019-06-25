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

