# !/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys


from demo_cloud.CVM_demo.cloud_cvm_select import select_insid

#创建云主机
def  first_step():
    from demo_cloud.CVM_demo.cloud_cvm_create import cvm
    c = cvm()
    c.create_cvm()

def  second_step():
    from demo_cloud.CVM_demo.cloud_cvm_select import select_insid
    from  demo_cloud.CLB_demo.cloud_add_CLB import CLB
    # 建负载均衡
    clb = CLB()
    clb.create_clb()
    # 查询负载均衡id
    clb.select_lb_id()
    #创建负载均衡监听器
    clb.create_lb_jtq()
    #查询监听器的listen_id
    clb.select_listenerld()
    #转发规则
    clb.zf_rules()
    #查询负载均衡id
    instans_id =select_insid()
    #绑定云服务器
    clb.bd_clb(instans_id)

def  three_step():
    #重置密码
    from demo_cloud.fabric_demo.demo import test
    #搭http服务
    test()

first_step()
second_step()
three_step()
