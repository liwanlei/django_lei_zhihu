from lib import xadmin
from huati.models import Hua,Huafen,Commenthuati
from django.contrib import admin
xadmin.site.register(Hua)
xadmin.site.register(Huafen)
xadmin.site.register(Commenthuati)


