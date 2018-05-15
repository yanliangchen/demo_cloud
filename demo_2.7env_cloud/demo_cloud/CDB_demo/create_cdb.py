#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入云API入口模块


from QcloudApi.qcloudapi import QcloudApi

#云数据库类
class   cdb():
    def  safe_group(self):
        '''

         给加一个安全组
        :return:
        '''

        self.module = 'dfw'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''

        self.action = 'CreateSecurityGroup'

        '''
        config: 云API的公共参数
        '''
        self.config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        # 接口参数
        self.action_params = {
                    'Version' : '2017-03-12',
                    'sgName' : 'safe_group_one'
        }#
        try:
            service = QcloudApi(self.module, self.config)
            print(service.generateUrl(self.action, self.action_params))
            res=service.call(self.action, self.action_params)
            print(eval(res))

        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

    #创建
    def  create_cdb(self):

        self.module = 'cdb'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''

        self.action = 'CreateDBInstanceHour'

        '''
        config: 云API的公共参数
        '''
        self.config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        # 接口参数
        self.action_params = {
                    'Version' : '2017-03-12',
                    'cdbType' :'CUSTOM ',
                    'engineVersion':'5.6',
                    'goodsNum':'1',
                    'memory':'2000',
                    'volume':'100'
        }#
        try:
            service = QcloudApi(self.module, self.config)
            print(service.generateUrl(self.action, self.action_params))
            res=service.call(self.action, self.action_params)
            res1=eval(res)
            print(res1)
            self.in_ids=res1['data']['instanceIds']

        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())
    #初始化
    def chush_cdb(self):
        self.module = 'cdb'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''

        self.action = 'InitDBInstances'

        '''
        config: 云API的公共参数
        '''
        self.config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        # 接口参数
        self.action_params = {
            'action':'InitDBInstances',
            'Version': '2017-03-12',
            'instanceIds': self.in_ids,
            'newPassword': 'liyanliang@bih888',
            'parameters': [{'name': 'character_set_server', 'value': 'utf8'}],
        }
        try:
            service = QcloudApi(self.module, self.config)
            print(type(service.generateUrl(self.action, self.action_params)))
            res = service.call(self.action, self.action_params)
            print(eval(res))
        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())


    def  select_id(self):
        '''
        获取instance_id  来给数据库开通实例外网访问
        :return:
        '''
        self.module = 'cdb'

        '''
        action: 对应接口的接口名，请参考产品 API 文档上对应接口的接口名
        '''

        self.action = 'DescribeDBInstances'

        '''
        config: 云API的公共参数
        '''
        self.config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }

        # 接口参数
        self.action_params = {
            'Version': '2017-03-12',
            'InstanceIds.0' : 'cdb-c3sa3yg3'
        }  #
        try:
            service = QcloudApi(self.module, self.config)
            print(service.generateUrl(self.action, self.action_params))
            res = service.call(self.action, self.action_params)
            print(res)
            temp = str(res).strip('b')
            import  json
            tmp = json.loads(temp.replace('\'', ''))
            self.instance_id = tmp['data']['items'][0]['instanceId']
            print(self.instance_id)

        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())


    def  gw_ip(self):
        '''
        给数据库指定公网ip
        :return:
        '''
        # 给加一个安全组

        self.module = 'cdb'

        '''
        action: 对应接口的接口名，请参考产品
        API
        文档上对应接口的接口名
        '''

        self.action = 'OpenWanService'

        self.config = {
            'Region': 'ap-beijing',
            'secretId': 'AKIDTp13vccxugHgv0QjOsBJG2d2HMH0Lv79',
            'secretKey': '2vfFetxqZ7UghWBfy51nZROK5f5KOIBt',
        }
        '''
        config: 云API的公共参数
        '''

        # 接口参数
        self.action_params = {
                    'Version' : '2017-03-12',
                    'instanceId' :self.instance_id

        }
        print(self.action_params['instanceId'])
        try:
            service = QcloudApi(self.module, self.config)
            print(service.generateUrl(self.action, self.action_params))
            res=service.call(self.action, self.action_params)
            print(eval(res))

        except Exception as e:
            print(e)
            import traceback
            print('traceback.format_exc():\n%s' % traceback.format_exc())

if __name__ == '__main__':
    c=cdb()
    c.safe_group()
    c.create_cdb()
    import  time
    time.sleep(150)
    c.chush_cdb()
    time.sleep(50)
    c.select_id()
    time.sleep(50)
    c.gw_ip()