# encoding: utf-8
"""
@author: lileilei
@file: form_user.py
@time: 2017/11/8 13:07
"""
from django import  forms
from  django.forms import fields,widgets
class LoginForm(forms.Form):
    user=fields.CharField(label='用户名',help_text='注册的平台账号',max_length=16,min_length=6,strip=True,error_messages={
        'required': '用户输入为空',
        'max_length': '用户输入太长了',
        'min_length': '用户输入太短了'
    },widget=forms.TextInput(attrs={'class':'form-control'}))
    password=fields.CharField(min_length=6,max_length=16,error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    },widget=widgets.PasswordInput(attrs={'class':'form-control'}))
class RegiestForm(forms.Form):
    username=fields.CharField(label='用户名',help_text='注册的平台账号',max_length=16,min_length=6,strip=True,error_messages={
        'required': '用户输入为空',
        'max_length': '用户输入太长了',
        'min_length': '用户输入太短了'
    },widget=forms.TextInput(attrs={'class':'form-control'}))
    password = fields.CharField(min_length=6, max_length=16, error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    commpassword=fields.CharField(min_length=6,max_length=16,error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    },widget=widgets.PasswordInput(attrs={'class':'form-control'}))
    email=fields.EmailField(label='邮箱',help_text='注册邮箱',required=True, error_messages={
                                  'invalid':"用户输入格式错误"
                              },widget=widgets.EmailInput(attrs={'class':'form-control'}))
class ChangepassForm(forms.Form):
    yuapassword = fields.CharField(min_length=6, max_length=16, error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    password = fields.CharField(min_length=6, max_length=16, error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
    commpassword = fields.CharField(min_length=6, max_length=16, error_messages={
        'required': '不能为空',
        'max_length': '密码输入太长了',
        'min_length': '密码输入太短了'
    }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))

