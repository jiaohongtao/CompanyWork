# �������� API ���� SDK ʹ���ĵ�

- ��һ����: API ����ķ��ʷ�ʽ
- �ڶ�����: API ����İ汾˵��

# Ŀ¼

[TOC]

----------------------------------------------------------

# ��һ����: API ����ķ��ʷ�ʽ

�����ַ�ʽ���������shortcuts��ComponentClient��ʹ��ʾ�����£�

## 1. ʹ��shortcuts

### 1.1 get_client_by_request

```
from blueking.component.shortcuts import get_client_by_request
# �ӻ������û�ȡAPP��Ϣ����request��ȡ��ǰ�û���Ϣ
client = get_client_by_request(request)
kwargs = {'bk_biz_id': 1}
result = client.cc.get_app_host_list(kwargs)
```

### 1.2 get_client_by_user

```
from blueking.component.shortcuts import get_client_by_user
# �ӻ������û�ȡAPP��Ϣ����user��ȡ��ǰ�û���Ϣ��userΪUser�����User��username����
user = 'xxx'
client = get_client_by_user(user)
kwargs = {'bk_biz_id': 1}
result = client.cc.get_app_host_list(kwargs)
```


## 2. ʹ��ComponentClient

```
from blueking.component.client import ComponentClient
# APP��Ϣ
bk_app_code = 'xxx' 
bk_app_secret = 'xxx' 
# �û���Ϣ
common_args = {'bk_token': 'xxx'}
# APP��Ϣbk_app_code, bk_app_secret��δ�ṩ���ӻ������û�ȡ
client = ComponentClient(
    bk_app_code=bk_app_code, 
    bk_app_secret=bk_app_secret, 
    common_args=common_args
)
kwargs = {'bk_biz_id': 1}
result = client.cc.get_app_host_list(kwargs)
```


# �ڶ�����: API ����İ汾˵��

�����ٷ��ṩ�� API������ v1��v2 �����汾���Ƽ�ʹ�� v2 �汾��
Ϊ���ּ��ݣ�SDK ͬʱ֧�ַ��� v1��v2 �����汾�� API��

SDK ʹ�� settings �еı��� **DEFAULT_BK_API_VER** ���÷��ʵ�Ĭ�� API �汾����ѡֵΪ: "v2"��v2 �汾����""��v1 �汾����Ĭ��ֵΪ"v2"��

�����Ҫ���ʷ�Ĭ�ϰ汾�� API����ͨ����ȷָ���汾�ŵķ�ʽʵ�֣��磺
```
# client = get_client_by_request(request)
client = ComponentClient(xxx, xxx)
# ָ������ v1 �汾�� API
client.set_bk_api_ver("")
result = client.cc.get_app_host_list(xxx)

# ָ������ v2 �汾�� API
client.set_bk_api_ver("v2")
result = client.cc.search_host(xxx)
```
