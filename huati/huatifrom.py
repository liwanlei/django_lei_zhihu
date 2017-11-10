# encoding: utf-8
"""
@author: lileilei
@file: huatifrom.py
@time: 2017/11/10 11:25
"""
from django import  forms
from  django.forms import fields,widgets
from  .models import Huafen
class WritercontForm(forms.Form):
    title = fields.CharField(min_length=2, max_length=30, error_messages={
        'required': '标题不能为空！',
        'max_length': '标题输入太长了',
        'min_length': '标题输入太短了'
    }, widget=widgets.Input(attrs={'class': 'form-control'}))
    feilei=forms.ModelChoiceField(queryset=Huafen.objects.filter(status=False),required=True)
    text=fields.CharField(widget=widgets.Textarea(attrs={'class': 'form-control'}))
