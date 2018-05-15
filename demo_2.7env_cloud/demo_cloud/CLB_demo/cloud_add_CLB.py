#!/usr/bin/python
# -*- coding: utf-8 -*-
# 引入云API入口模块
from QcloudApi.qcloudapi import QcloudApi
from demo_cloud.CVM_demo.cloud_cvm_select import select_insid
import time
import  json
class  CLB():
    #创建负载均衡
    def  create_clb(self):
        module  = 'lb'
        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'CreateLoadBalancer'

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
            'Version': '2017-03-12',
            #公网
            'loadBalancerType':'2',
            #应用型
            'forward':'1',
            #
            'loadBalancerName':'clb_one',
            'number':'1'
        }

        try:

            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res=service.call(action, action_params)
            print(eval(res))
            print('睡眠10秒，~等待~ 负载均衡创建成功')
            time.sleep(10)
            print('创建成功')
        except Exception as e:
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())



    def  select_lb_id(self):
        '''
        查到指定负载均衡的id
        :return:
        '''
        module = 'lb'
        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'DescribeLoadBalancers'

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
            'Version': '2017-03-12',
            # 'loadBalancerType':'2'
            'forward':'-1'
        }
        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            temp = str(res).strip('b')
            import json
            tmp = json.loads(temp.replace('\'', ''))
            print(tmp)
            self.lb_id = tmp['loadBalancerSet'][0]['loadBalancerId']
            print(self.lb_id,'lbid  is  success ')

        except Exception as e:
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())


    #创建负载均衡监听器
    def create_lb_jtq(self):
        module  = 'lb'
        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'CreateForwardLBSeventhLayerListeners'

        '''
        config: 云API的公共参数
        '''
        config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        action_params = {
            'Version': '2017-03-12',
            'loadBalancerId':self.lb_id,
            #监听哪个服务的端口  这里监听80端口
            'listeners.0.loadBalancerPort': '80',
            'listeners.0.protocol':'1',
            'listeners.0.listenerName':'liyanliang'
        }
        # 接口参数

        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            print(eval(res))
            print('监听器创建成功')
        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

    #应用型负载均衡监听器id
    def  select_listenerld(self):
        module='lb'
        action = 'DescribeForwardLBListeners'
        config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        action_params = {
            'Version': '2017-03-12',
            'loadBalancerId':self.lb_id
        }
        # 接口参数

        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            res =json.loads(res.decode())
            self.listen_id= res['listenerSet'][0]['listenerId']
            print(self.listen_id,'-----------------监听id---------------')
        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())


    #负载均衡转发规则
    def  zf_rules(self):
        module = 'lb'
        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'CreateForwardLBListenerRules'

        '''
        config: 云API的公共参数
        '''
        config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }
        # import
        action_params = {
            'Version': '2017-03-12',
            # 负载均衡id
            'loadBalancerId': self.lb_id,
            # 监听器id
            'listenerId': self.listen_id,
            'rules.0.domain':'www.liyanliang.com',
            'rules.0.url':'/index.html',
            'rules.0.sessionExpire':'50'
        }
        #接口参数
        try:
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            print(eval(res))
            #开始睡眠
            print('转发路路由规则创建成功，开始等待五秒')
            time.sleep(5)
            print('创建成功')
        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

    # 查询出来云服务器
    #绑定后端服务器到负载均衡实例上

    def  bd_clb(self,instans_id):
        print(instans_id)
        self.instans_id=instans_id
        print(self.instans_id,'-----------instanceid ')
        module = 'lb'
        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''
        action = 'RegisterInstancesWithForwardLBSeventhListener'

        '''
        config: 云API的公共参数
        '''
        config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }
        # import
        action_params = {
            'Version': '2017-03-12',
            #负载均衡id
            'loadBalancerId':self.lb_id,
            #监听器id
            'listenerId':self.listen_id,
            #云主机id
            'backends.0.instanceId':self.instans_id,
            'backends.0.weight':10,
            #监听端口
            'backends.0.port':80,

        }

        # 接口参数
        try:
            print('绑定中......')
            service = QcloudApi(module, config)
            print(service.generateUrl(action, action_params))
            res = service.call(action, action_params)
            print(eval(res))
            print('负载均衡绑定云主机成功')
        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

if __name__ == '__main__':
    clb=CLB()
    # 创建负载均衡
    clb.create_clb()
    #查询实例id

    time.sleep(10)
    clb.select_lb_id()
    # 创建负载均衡监听器
    clb.create_lb_jtq()
    # #查询监听器的listen_id
    clb.select_listenerld()
    clb.zf_rules()
    time.sleep(5)
    #绑定云服务器
    instans_id =select_insid()
    clb.bd_clb(instans_id)




