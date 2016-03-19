# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#用户组别
class UserGroup(models.Model):
    name = models.CharField(max_length=100)
    
    def  __unicode__(self):
        return self.name;

#用户
class User(models.Model):
    #唯一主键
    id = models.IntegerField(primary_key=True, db_column='id')
    #登录名
    login = models.CharField(max_length=100)
    #登录密码
    passwd = models.CharField(max_length=100)
    #所属组别
    group = models.ForeignKey(UserGroup)
    #权限值1-用户2-管理员3-财务（审批购买）4-超级管理员
    authority = models.IntegerField(default=1)
    #显示姓名
    name = models.CharField(max_length=100)

    def  __unicode__(self):
        return self.name;

#入库申请
class Apply(models.Model):
    #申请物品名称
    item_name = models.CharField(max_length=100)
    #申请人
    user = models.ForeignKey(User)
    #申请描述
    detail = models.TextField(blank = True, null = True)
    #审批状态 0-未处理 1-拒绝批准 2-审批通过
    apply_status = models.NullBooleanField(default=0)
    #处理状态 0-未购买 1-已购买
    bought_status = models.BooleanField( default=0)
    #申请提出时间
    create_time = models.DateTimeField( auto_now_add = True)
    #申请修改时间
    modify_time = models.DateTimeField( auto_now = True)

    def __unicode__(self):
        return u'%s-%s' % (self.item_name, self.user.name)
    

#物品
class Item(models.Model):
    #唯一主键
    id = models.IntegerField(primary_key=True, db_column='id')
    #名称
    name = models.CharField( max_length=100)
    #借出状态 0-未借出 1-已借出
    borrow_status = models.BooleanField( default=0)
    #借出者
    borrow_id = models.ForeignKey( User)
    #创建时间
    create_time = models.DateTimeField( auto_now_add = True)
    #修改时间
    modify_time = models.DateTimeField( auto_now = True)

    def __unicode__(self):
        return u'%s-%d' % (self.name, self.id)
    
    
