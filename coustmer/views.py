from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,render_to_response
from .models import ZUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login,logout
from django.views.generic import  View
from  coustmer.form_user import LoginForm,RegiestForm,ChangepassForm
from django.contrib.auth.hashers import make_password, check_password
class IndecView(View):
    def get(self,request):
        return  render(request,'index.html')
class LoginView(View):
    def get(self,request):
        login = LoginForm()
        return  render(request,'auth/login.html',{'obj':login})
    def post(self,request):
        login1 = LoginForm()
        fo=LoginForm(request.POST)
        v=fo.is_valid()
        if v:
            user=ZUser.objects.get(username=fo.cleaned_data['user'])
            password2=user.password
            if user:
                if check_password(fo.cleaned_data['password'],password2,'utf-8') and user.is_active:
                    request.session['username'] = fo.cleaned_data['user']
                    login(request, user)
                    return HttpResponseRedirect('/user/home/')
                return render(request, 'auth/login.html',{'obj': login1,'msg':'登录失败！请确认密码'})
            return render(request, 'auth/login.html', {'obj': login1,'msg': '用户不存在！请确认用户输入是否正确'})
        return render(request, 'auth/login.html', {'obj': login1})
def logoutview(request):
    try:
        del request.session['username']
        logout(request)
        return  HttpResponseRedirect('/user/login/')
    except: return HttpResponseRedirect('/user/home/')
class RegiestView(View):
    def get(self,request):
        fom=RegiestForm()
        return  render(request,'auth/register.html',{'form':fom})
    def post(self,request):
        fom=RegiestForm()
        f = RegiestForm(request.POST)
        v = f.is_valid()
        if v:
            data=f.cleaned_data
            if data['password']!=data['commpassword']:
                return render(request, 'auth/register.html', {'form': fom,'msg':'密码输入格式不正确!'})
            email=ZUser.objects.filter(email=data['email']).first()
            if email:
                return render(request, 'auth/register.html', {'form': fom, 'msg': '邮箱已经存在!'})
            username=ZUser.objects.filter(username=data['username']).first()
            if username:

                return render(request, 'auth/register.html', {'form': fom, 'msg': '用户已经被抢先注册!'})
            try:
                new_user=ZUser(email=data['email'],username=data['username'])
                new_user.password=make_password(data['password'])
                new_user.save()
                return HttpResponseRedirect('/user/login/')
            except:
                return render(request, 'auth/register.html', {'form': fom, 'msg': '注册出现情况，请稍后注册!'})
        return  render(request,'auth/register.html',{'form':fom})
def pageNofoud(request):
    return render_to_response('404.html')
def permission_denied(request):
    return render_to_response('403.html')
def indeter(request):
    return render_to_response('500.html')
class ChangepassView(View):
    def get(self,request):
        changeform=ChangepassForm()
        return  render(request,'auth/change_password.html',{'form':changeform})
    def post(self,request):
        user1 = request.session['username']
        changeform = ChangepassForm()
        f=ChangepassForm(request.POST)
        if f.is_valid():
            data=f.cleaned_data
            if data['password']!=data['commpassword']:
                return render(request, 'auth/change_password.html', {'form': changeform, 'msg': '新密码和确认密码不一致！'})
            user=ZUser.objects.filter(username=user1).first()
            if not user:
                return render(request, 'auth/change_password.html', {'form': changeform,'msg':'用户不存在！'})
            if check_password(data['yuapassword'],user.password,'utf-8') is False:
                return render(request, 'auth/change_password.html', {'form': changeform, 'msg': '原密码输入有误！'})
            if check_password(user.password,data['password'],'utf-8'):
                return render(request, 'auth/change_password.html', {'form': changeform, 'msg': '新密码与最近一次密码一致！请重新输入'})
            try:
                user.password=make_password(data['commpassword'])
                user.save()
                del request.session['username']
                logout(request)
                return HttpResponseRedirect('/user/login/')
            except:
                return render(request, 'auth/change_password.html', {'form': changeform, 'msg': '修改密码失败！请重新输入'})
            return render(request, 'auth/change_password.html', {'form': changeform,'msg': '确认你的提交！'})
        return render(request, 'auth/change_password.html', {'form': changeform})