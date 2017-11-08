"""zhihu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from lib.xadmin.plugins import xversion
from lib import xadmin
from coustmer.views import IndecView,LoginView,logoutview,RegiestView,pageNofoud,indeter,permission_denied,ChangepassView
from django.contrib.auth.decorators import login_required
xversion.register_models()
xadmin.autodiscover()
urlpatterns = [
   url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^user/home/$',login_required(IndecView.as_view()),name='home'),
    url(r'^user/login/$',LoginView.as_view(),name='login'),
    url(r'^user/logout/$',logoutview,name='logout'),
    url(r'^user/regiest/$', RegiestView.as_view(), name='regiest'),
    url(r'^user/change_password/$', login_required(ChangepassView.as_view()), name='change_password'),

]
handler404=pageNofoud
handler403=permission_denied
handler500=indeter