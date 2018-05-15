#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块
from QcloudApi.qcloudapi import QcloudApi

import json


class cvm():
    def create_cvm(self):

        module = 'cvm'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'RunInstances'

        '''
        config: 云API的公共参数

        # region = input('请输入您想要建立的地域:\n例如：beijing \n')
        # print(region)
        # print('------------------------')
        # num=input('请输入可用区:\n例如您想选择北京1区 您只需要输入数字 "1" \n')
        # print('------------------------')
        '''

        config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        '''
        print('地域和地区选择成功')
        print('------------------------')
        charge_type = input('请输入您所需要的计费模式:\n例如:按量计费则请输入：POSTPAID_BY_HOUR\n按年计费则输入：PREPAID\n')
        print('------------------------')
        system_type = input('请选择您所需要/系统盘,类型如下:\n本地硬盘 : LOCAL_BASIC \n本地SSD硬盘 : LOCAL_SSD\n普通云硬盘 : CLOUD_BASIC\n云硬盘 : CLOUD_SSD\n')
        system_size =  input('请选择您所需要的系统盘大小\n')
        print('系统盘大小和类型填写成功')
        print('------------------------')
        data_type = input('请选择您要的数据盘,类型如下:\n本地硬盘 : LOCAL_BASIC\n本地SSD硬盘 : LOCAL_SSD\n普通云硬盘 : CLOUD_BASIC\n高性能云硬盘 : CLOUD_PREMIUMSSD\n云硬盘 : CLOUD_SSD\n')
        data_size = input('请选择您所需要的数据盘大小\n')
        print('数据盘大小和类型填写成功')
        print('------------------------')
        cvm_name = input('请给您的实例进行命名\n')
        print('命名成功')
        print('------------------------')
        gongwang_ip = int(input('是否分配公网ip,如需分配请输入1 ,不分配则输入0\n'))
        print('分配成功')
        print('------------------------')
        '''

        # 接口参数
        action_params = {
            # API  版本号
            'Version': '2017-03-12',
            # 计费类型 按量计费
            'InstanceChargeType': 'POSTPAID_BY_HOUR',
            # 选择地域和可用区
            'Placement.Zone': 'ap-beijing-3',
            # 镜像
            'ImageId': 'img-8toqc6s3',
            # 镜像机型1C1G 标准型
            'InstanceType': 'S2.SMALL1',
            # 系统盘的类型
            'SystemDisk.DiskType': 'CLOUD_BASIC',
            # 'SystemDisk.DiskType':'CLOUD_BASIC',
            # 系统盘的大小
            'SystemDisk.DiskSize': '60',
            # 数据盘类型
            'DataDisks.0.DiskType': 'CLOUD_BASIC',
            # 数据盘大小  50
            'DataDisks.0.DiskSize': '60',
            # 外网带宽上限10
            'InternetAccessible.InternetMaxBandwidthOut': 10,
            # 分配公网ip
            'InternetAccessible.PublicIpAssigned': True,
            # 实例命名
            'InstanceName': 'liyanliang',

        }

        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            print(eval(res))
            res = json.loads(res.decode())
            print(res)
            self.res = res['Response']['InstanceIdSet'][0]
            print('云主机创建成功')

        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

# if __name__ == '__main__':
#     c=cvm()
#     c.create_cvm()

