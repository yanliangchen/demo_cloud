#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from QcloudApi.qcloudapi import QcloudApi

'''
module: 设置需要加载的模块
已有的模块列表：
cvm      对应   cvm.api.qcloud.com
cdb      对应   cdb.api.qcloud.com
lb       对应   lb.api.qcloud.com
trade    对应   trade.api.qcloud.com
sec      对应   csec.api.qcloud.com
image    对应   image.api.qcloud.com
monitor  对应   monitor.api.qcloud.com
cdn      对应   cdn.api.qcloud.com
'''
module = 'cvm'

'''
action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
'''
#退还实例
action = 'TerminateInstances'

'''
config: 云API的公共参数
'''
config = {
    'Region': 'ap-beijing',
    'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
    'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
}

# 接口参数
action_params = {
    #API  版本号
    'Version':'2017-03-12',
    #退还哪一台主机
    'InstanceIds.0':'d69bf457-08ef-452d-ba23-6ebc22fbbf4f',
}

try:
    service = QcloudApi(module, config)
    print(service.generateUrl(action, action_params))
    res=service.call(action, action_params)
    print(eval(res))
except Exception as e:
    import traceback
    print('traceback.format_exc():\n%s' % traceback.format_exc())