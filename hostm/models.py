from django.db import models


class UserInfo(models.Model):
    '''
    用户表
    默认创建id列，自增，主键
    '''
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    def __repr__(self):
        '''''使查询结果中显示具体信息，不是内存地址'''
        return self.username


class HostInfo(models.Model):
    '''主机信息表'''
    hostname = models.CharField(max_length=32,unique=True,null=False)   #主机名
    ip = models.GenericIPAddressField(unique=True,null=False) #ip
    ssh_port = models.PositiveIntegerField(null=False)  #ssh端口
    last_check = models.DateTimeField(auto_now=True)  #最近一次巡检日期
    desc = models.CharField(max_length=32, null=False)  # 业务描述，运行的应用
    project_choices = (
        ('1', '开发'),
        ('2', '运维'),
        ('3', '测试'),
    )
    project = models.CharField(choices=project_choices,max_length=32,null=False,default='3') #所属项目组
    option_choices = (
        ('1', '生产'),
        ('2', '测试'),
    )
    option = models.CharField(choices=option_choices,max_length=32,null=False,default='2' ) #功能划分
    status_choices = (
        ('1', '使用中'),
        ('2', '闲置'),
        ('3', '损坏'),
    )
    status = models.CharField(choices=status_choices,max_length=32,null=False,default='2' ) #主机状态

    def __str__(self):
        '''''使查询结果中显示具体信息，不是内存地址'''
        return self.hostname