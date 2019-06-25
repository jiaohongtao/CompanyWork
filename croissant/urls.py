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

from django.conf.urls import patterns

urlpatterns = patterns(
    'croissant.views',
    (r'^croissantOne/$', 'croissantOne'),
    (r'^get_business/$', 'get_business'),
    (r'^get_hosts/$', 'get_hosts'),
    (r'^execute_script/$', 'execute_script'),
    (r'^execute_record/$', 'execute_record'),
    (r'^get_execute_details/$', 'get_execute_details'),
    (r'^get_execute_log/$', 'get_execute_log'),
)
