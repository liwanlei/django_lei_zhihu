from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import Hua,Huafen,Commenthuati
from  .huatifrom import WritercontForm,AskquestionForm
from coustmer.models import ZUser,Shoucang
from django.views.generic import  View
class AddpostView(View):
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
                return render(request, 'huati/writer.html', {'form': form, 'msg': '请稍后发布！'})
        return render(request, 'huati/writer.html', {'form': form})
class Addcollection(View):
    def get(self,request,id):
        user=ZUser.objects.filter(username=request.session['username']).first()
        wenzhang=Hua.objects.filter(id=id).first()
        if user and wenzhang:
            new_collection=Shoucang()
            new_collection.shoucanguser_id=user.id
            try:
                if wenzhang in new_collection.shoucanghua:
                    return redirect(('home'))
                new_collection.shoucanghua.add(wenzhang)
                new_collection.save()
                return  redirect(('home'))
            except:
                return redirect(('home'))
        return redirect(('home'))
class AddquestinsView(View):
    def get(self,request):
        form=AskquestionForm()
        return  render(request,'huati/addquestion.html',{'form':form})
    def post(self,request):
        user=ZUser.objects.filter(username=request.session['username']).first()
        form = AskquestionForm()
        fo = AskquestionForm(request.POST)
        v = fo.is_valid()
        if v:
            data=fo.cleaned_data
            New_title=Hua()
            New_title.title=data['title']
            New_title.desc=data['connet'][:25]
            New_title.connet=data['connet']
            New_title.is_shi=data['is_shi']
            New_title.user=user
            try:
                New_title.save()
                New_title.fenlei.add(data['feilei'])
                New_title.save()
            except Exception as e:
                return render(request, 'huati/addquestion.html', {'form': form,'msg':'请再次输入您的提问'})
            return redirect('home')
        return render(request, 'huati/addquestion.html', {'form': form})
class PostdetileView(View):
    def get(self,request,id):
        title=Hua.objects.filter(id=id).first()
        comment=Commenthuati.objects.filter(huati=title).all()
        return  render(request,'huati/post.html',{'title':title,'comment':comment})
    def post(self,request,id):
        user=ZUser.objects.filter(username=request.session['username']).first()
        title = Hua.objects.filter(id=id).first()
        comment = Commenthuati.objects.filter(commenthuati__huati__title=title.title)
        data =request.POST.get('comment')
        if not data:
            return  render(request,'huati/post.html',{'title':title,'comment':comment})
        if data:
            new_comment=Commenthuati()
            new_comment.huati=title
            new_comment.user=user
            new_comment.comment=data
            new_comment.save()
            return redirect('postdetile',id=title.id)
        return render(request, 'huati/post.html', {'title': title, 'comment': comment})
class QuestionView(View):
    def get(self,request,id):
        question=Hua.objects.filter(id=id).first()
        commnet=Commenthuati.objects.filter(huati=question).all()
        return  render(request,'huati/question.html',{'question':question,'comment':commnet})
    def post(self,request,id):
        user = ZUser.objects.filter(username=request.session['username']).first()
        question = Hua.objects.filter(id=id).first()
        comment =Commenthuati.objects.filter(commenthuati__huati__title=question.title).all()
        data = request.POST.get('comment')
        if data:
            new_comment = Commenthuati()
            new_comment.huati = question
            new_comment.user = user
            new_comment.comment = data
            print(new_comment)
            try:
                new_comment.save()
                return redirect('questiondetile', id=question.id)
            except Exception as e:
                return render(request, 'huati/question.html', {'title': question, 'comment': comment,'msg':'请再次评论'})
        return render(request, 'huati/question.html', {'title': question, 'comment': comment})
class DetilehuatiView(View):
    def get(self,request):
        user=ZUser.objects.filter(username=request.session['username']).first()
        guanzhu=user.get_guanzhu()
        huati_list=[]
        for huati in guanzhu:
            hu=Hua.objects.filter(fenlei=huati[0]).first()
            huati_list.append(hu)
        return  render(request, 'huati/guanzhuhuati.html', {'guanhzu':guanzhu, 'huati_list':huati_list})
class DetitleOneView(View):
    def get(self,request,name):
        fenlei=Huafen.objects.filter(name=name).first()
        huati=Hua.objects.filter(fenlei=fenlei).all()
        return  render(request,'huati/onedetail.html',{'huati':huati,'name':name})
class EditPostView(View):
    def get(self,request,id):
        editpost=Hua.objects.filter(id=id).first()
        fenlei=Huafen.objects.all()
        if not  editpost:
            return render(request, 'huati/editpost.html',{'msg':'文章不存在'})
        return  render(request,'huati/editpost.html',{'editpost':editpost,'fenlei':fenlei})
    def post(self,request,id):
        editpost = Hua.objects.filter(id=id).first()
        fenlei = Huafen.objects.all()
        title=request.POST.get("title")
        connent=request.POST['content']
        fen=request.POST['fenlei']
        user = ZUser.objects.filter(username=request.session['username']).first()
        editpost.title = title
        editpost.connet = connent
        editpost.desc = connent[:35]
        editpost.user_id = user
        editpost.leibie = '文章'
        try:
            for fe in (editpost.fenlei.all()):
                editpost.fenlei.remove(fe)
            editpost.fenlei.add(Huafen.objects.filter(name=fen).first())
            editpost.save()
            return redirect('postdetile',id=id)
        except Exception as e:
            return render(request, 'huati/editpost.html', {'editpost': editpost, 'msg': u'请稍后编辑！','fenlei':fenlei})