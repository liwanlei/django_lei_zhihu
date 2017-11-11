from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import Hua,Huafen,Commenthuati
from  .huatifrom import WritercontForm,AskquestionForm
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
            except:
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
        print(comment)
        data = request.POST.get('comment')
        if data:
            new_comment = Commenthuati()
            new_comment.huati = question
            new_comment.user = user
            new_comment.comment = data
            try:
                new_comment.save()
                return redirect('questiondetile', id=question.id)
            except Exception as e:
                return render(request, 'huati/question.html', {'title': question, 'comment': comment,'msg':'请再次评论'})
        return render(request, 'huati/question.html', {'title': question, 'comment': comment})
