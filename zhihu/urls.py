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
from coustmer.views import IndecView,LoginView,logoutview,RegiestView,pageNofoud,indeter,permission_denied,ChangepassView,UserView,UserdataView,AddforView,ResetforView,ReadMessage,DeteMessage,ReadMessagey,Onemessage
from huati.views import AddpostView,Addcollection,AddquestinsView,PostdetileView,QuestionView,DetilehuatiView,DetitleOneView,EditPostView
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
    url(r'^user/user/(?P<username>\w+)/$', login_required(UserView.as_view()), name='user'),
    url(r'^user/userdata/$', login_required(UserdataView.as_view()), name='userdata'),
    url(r'^user/addfor/(?P<name>\w+)/$', login_required(AddforView.as_view()), name='addfor'),
    url(r'^user/retfor/(?P<name>\w+)/$', login_required(ResetforView.as_view()), name='retfor'),
    url(r'^huati/addpost/$', login_required(AddpostView.as_view()), name='addpost'),
    url(r'^huati/addcollection/(?P<id>\d+)/$',login_required(Addcollection.as_view()),name='addcollection'),
    url(r'^huati/addquest/$',login_required(AddquestinsView.as_view()),name='addquest'),
    url(r'^huati/postdetile/(?P<id>\d+)/$',login_required(PostdetileView.as_view()),name='postdetile'),
    url(r'^huati/questiondetile/(?P<id>\d+)/$',login_required(QuestionView.as_view()),name='questiondetile'),
    url(r'^huati/huatidetile/$',login_required(DetilehuatiView.as_view()),name='huatidetile'),
    url(r'^huati/onedetiale/(?P<name>\w+)$', login_required(DetitleOneView.as_view()), name='onedetaile'),
    url(r'^huati/editpost/(?P<id>\d+)/$',login_required(EditPostView.as_view()),name='editpost'),
    url(r'^user/readmessage/$',login_required(ReadMessage.as_view()),name='readmessage'),
    url(r'^user/detemessage/(?P<id>\d+)/$',login_required(DeteMessage.as_view()),name='detemessage'),
    url(r'^user/readyimess/(?P<id>\d+)/$',login_required(ReadMessagey.as_view()),name='readyimess'),
    url(r'^user/onemessage/(?P<id>\d+)/$',login_required(Onemessage.as_view()),name='onemessage'),
]
handler404=pageNofoud
handler403=permission_denied
handler500=indeter