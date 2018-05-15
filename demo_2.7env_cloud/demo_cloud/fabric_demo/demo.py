#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from fabric.api  import env
from fabric.api import run
from fabric.api  import  cd
from  demo_cloud.CVM_demo.cloud_cvm_czpassword import cz_mima
from demo_cloud.CVM_demo.cloud_cvm_gwip import select_cvm_gwip

def  test():
    g_ip = select_cvm_gwip()
    print(g_ip)
    c = cz_mima()
    c.cz_cvm_password()
    c = c.new_mima()[0]
    import time
    time.sleep(100)
    env.host=g_ip
    env.user= 'root'
    env.password=c
    try:
        run('yum list | grep httpd')
        run(' yum -y install httpd')
        with cd('/var/www/html'):
            try:
                # run("sed -i 's/\/var\/www\/html/\/root\/test/g' /etc/httpd/conf/httpd.conf")
                run('cd /var/www/html')
                run('echo  "晚上好，刘公伯先生" > /var/www/html/index.html')
                run('service httpd start')
            except Exception as e :
                print (e)
    except Exception as e :
        print(e)
        print('部署异常')
# test()
















'''
from fabric.api import *
import time

TOMCAT_HOME = "/xxxx/apache-tomcat-8.0.29"
WAR_DIR = "/home/jenkins/.jenkins/xxxx/target/"

# 要远程部署的几个服务器
servers = [
    '192.144.153.252',
]

# 这几个服务器有统一的用户名访问
env.user = "root"

# 服务器用户密码
env.password = "asdw123456"


def deploy(projectname):
    for server in servers:
        print("正在部署服务器：" + server + " 项目名：" + projectname)
        with settings(host_string=server):
            deploy_one_server(projectname)
            print("部署服务器 " + server + " 项目" + projectname + " 完成!")
            print(
            "休息60秒")
            time.sleep(60)

            # 部署一个服务器


def deploy_one_server(projectname):
    warfilename = projectname + ".war"
    local('mkdir  1111')

    # # 1，上传文件到tomcat根目录
    # print("1，上传文件到tomcat根目录")
    # with lcd(WAR_DIR):
    #     with cd(TOMCAT_HOME):
    #         put(warfilename, warfilename)
    #         run("ls")

            # 2，关服务器
    print(
    "2，关闭服务器")
    close_tomcat()

    # 3，删除原有的部署文件
    print("3，删除原有的部署文件")
    with cd(TOMCAT_HOME + "/webapps/"):
        run("rm -rf " + projectname + "/")
        run("rm -rfv " + warfilename)

        # 4，将已上传的文件放到tomcat项目目录
    print
    "4，将已上传的文件放到tomcat项目目录"
    with cd(TOMCAT_HOME):
        run("mv " + warfilename + " ./webapps/")

        # 5，启动服务器
    print("5，启动服务器")
    run(TOMCAT_HOME + "/bin/startup.sh", pty=False)


# 关闭tomcat服务器
def close_tomcat():
    # kill可能会因为没有tomcat线程，导致关闭命令失败，所以需要在产生异常时继续执行
    with settings(
            hide('warnings', 'running', 'stdout', 'stderr'),
            warn_only=True
    ):
        run("ps -ef |grep tomcat |grep -v grep   |awk -F \" \" '{print $2}' | xargs kill -9")

deploy('ceshi')

'''