from lib import xadmin
from .models import Book,Bookcomment,Bookfenlei
from django.contrib import admin
xadmin.site.register(Book)
xadmin.site.register(Bookcomment)
xadmin.site.register(Bookfenlei)

