from lib import xadmin
from coustmer.models import *
from django.contrib import admin
#xadmin.site.unregister(ZUser)
#xadmin.site.register(ZUser)
xadmin.site.register(Shoucang)
xadmin.site.register(Message)
xadmin.site.register(Guanzhu)


