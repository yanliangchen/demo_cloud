# !/usr/bin/python
# -*- coding: utf-8 -*-
from demo_cloud.CVM_demo.cloud_cvm_select import select_insid
from QcloudApi.qcloudapi import QcloudApi
from demo_cloud.CVM_demo.cloud_cvm_gwip import select_cvm_gwip
class  cz_mima():
    mima=[]
    def  cz_cvm_password(self):
        in_id=select_insid()
        module = 'cvm'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        #重置密码
        action = 'ResetInstancesPassword'

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
            # API  版本号
            'Version': '2017-03-12',
            'InstanceIds.0':in_id,
            'Password': 'wasd123456',
            'ForceStop': True
        }

        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            print(eval(res))
            cz_mima.mima.append(action_params['Password'])
        except Exception as e:
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

    def  new_mima(self):
        res=cz_mima.mima
        return  res


if __name__ == '__main__':
    c=cz_mima()
    c.cz_cvm_password()
    c=c.new_mima()
    print(c)