from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import Hua,Huafen
from  .huatifrom import WritercontForm
from coustmer.models import ZUser,Shoucang
from django.views.generic import  View
class Addcomment(View):
    def get(self,request):
        form=WritercontForm()
        return  render(request,'huati/writer.html',{'form':form})
    def post(self,request):
        form = WritercontForm()
        fo = WritercontForm(request.POST)
        v = fo.is_valid()
        if v:
            data_clead=fo.cleaned_data
            title=data_clead['title']
            connet=data_clead['text']
            fenlei=data_clead['feilei']
            title_is=Hua.objects.filter(title=title).first()
            user=ZUser.objects.filter(username=request.session['username']).first()
            if title_is:
                return render(request, 'huati/writer.html', {'form': form,'msg':'标题不要重复哟亲！'})
            New_title=Hua()
            New_title.title=title
            New_title.connet=connet
            New_title.desc=connet[:35]
            New_title.user_id=user.id
            New_title.leibie='文章'
            try:
                New_title.save()
                New_title.fenlei.add(fenlei)
                New_title.save()
                return  HttpResponseRedirect(reverse('home'))
            except Exception as e:
                print(e)
                return render(request, 'huati/writer.html', {'form': form, 'msg': '请稍后发布！'})
        return render(request, 'huati/writer.html', {'form': form})
class Addcollection(View):
    def get(self,request,title):
        user=ZUser.objects.filter(username=request.session['username']).first()
        wenzhang=Hua.objects.filter(title=title).first()
        if user and wenzhang:
            new_collection=Shoucang()
            new_collection.shoucanguser_id=user.id
            new_collection.save()
            try:
                new_collection.shoucanghua.add(wenzhang)
                new_collection.save()
                return  redirect(('home'))
            except:
                return redirect(('home'))
        return redirect(('home'))
