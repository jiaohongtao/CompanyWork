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


class HostDisk(models.Model):
    name = models.CharField(u"主机名", max_length=64, unique=True)
    ip = models.CharField(u"主机ip", max_length=64)
    os = models.CharField(u"系统", max_length=64)
    disk = models.CharField(u"磁盘分区", max_length=64)
    create_time = models.DateTimeField(u'创建日期', auto_now=True)
    # description = models.TextField(u"描述", max_length=100, default='')

    class Meta:
        db_table = 'host_disk'
