from django.shortcuts import render,get_object_or_404,redirect
from .forms import BoardForm,CommentForm
from .models import Board
from django.utils import timezone
from .forms import SigninForm, SignupForm 
from django.urls.base import reverse
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout 



# Create your views here.
def post(request):
    if request.method == "POST":
        form=BoardForm(request.POST)
        if form.is_valid():
            board=form.save(commit=False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    
    else:
        form=BoardForm()
        return render(request,'post.html',{'form':form})

def show(request):
    boards=Board.objects.order_by('-id')
    return render(request,'show.html',{'boards':boards})

def detail(request,board_id):
    board_detail=get_object_or_404(Board,pk=board_id)
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        comment_form.instance.board_id=board_id
        if comment_form.is_valid():
            comment=comment_form.save()
    
    comment_form=CommentForm()
    comments=board_detail.comments.all()
    return render(request,'detail.html',{'board':board_detail,'comments':comments,'comment_form':comment_form})


def edit(request,pk):
    board=get_object_or_404(Board,pk=pk)
    if request.method == "POST":
        form=BoardForm(request.POST,instance=board)
        if form.is_valid():
            board=form.save(commit=False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    
    else:
        form=BoardForm(instance=board)
        return render(request,'edit.html',{'form':form})

def delete(request,pk):
    board=Board.objects.get(id=pk)
    board.delete()
    return redirect('show')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html', {'form':SignupForm()} )
    
    
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['password_check']:

                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])

                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']

                new_user.save()
                
                return redirect('show')      
            else:
                return render(request, 'signup.html',{'form':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})

        else: 
            return render(request, 'signup.html',{'form':form})

def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html', {'form':SigninForm()} )
    
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST.get('username')
        pw = request.POST.get('password')
        u = authenticate(username=id, password=pw)

        if u: 
            login(request, user=u) 
            return redirect('show')
        else:
            return render(request, 'signin.html',{'form':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
    


def signout(request): 
    logout(request) 
    return redirect('show')

