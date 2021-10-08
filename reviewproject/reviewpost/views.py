from django.shortcuts import(
    render,
    redirect
)
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import(
    authenticate,
    login,
    logout
)
from .models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            user = User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザはすでに登録されています'})
        print('POST method')
    else:
        print(User.objects.all())
        print('Get method probably...')
    return render(request, 'signup.html',{})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        
        user = authenticate(request,username=username_data, password=password_data)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request, 'login.html')

@login_required
def listview(request):
    object_list = ReviewModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

@login_required
def detailview(request,pk):
    object = ReviewModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object':object})

class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('title','content','author','images','evaluation')
    success_url = reverse_lazy('list')

def logoutview(request):
    logout(request)
    return redirect('login')