from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from core.forms import SignUpForm
from core.forms import UpdateForm

# Create your views here.

#=========================== user home ===========================

@login_required(login_url='sign-in')
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def home(request):
    user = User.objects.get(username =request.user.username)

    users = User.objects.all()

    context = {
        'home_or_not': True,
        'user': user,
        'users': users,
        'range': range(5),
    }
    return render(request, 'home.html',context)

#=========================== user signin ===========================


@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_user_exists = User.objects.filter(username=username).exists()
        if is_user_exists:
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect password")
                return render(request,'login.html')

        else:
            messages.error(request, "Invalid username")
            return render(request,'login.html')

    return render(request,'login.html')


#=========================== user signout ===========================

def sign_out(request):
    logout(request)
    return redirect('welcome')


#=========================== user signup ===========================

def sign_up(request):
      
      form = SignUpForm()

      if request.method == 'POST':
        
            form = SignUpForm(request.POST)
            if form.is_valid():
                username    = form.cleaned_data['username']
                first_name  = form.cleaned_data['first_name']
                last_name   = form.cleaned_data['last_name']
                email       = form.cleaned_data['email']
                password    = form.cleaned_data['password']

                user = User.objects.create(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email
                )
                user.set_password(password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('welcome')


      context = {'form': form}
      return render(request,'signup.html',context)

#=========================== welcome ===========================

def welcome(request):
    return render(request,'welcome.html')

# =========================admin actions==================

# =========================admin signin==================

def admin_signin(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin-home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_user_exists = User.objects.filter(username=username).exists()

        if is_user_exists:
            user= authenticate(username=username,password=password)

            if user.is_superuser and user.is_staff:
                login(request,user)
                return redirect('admin-home') 
            else:
                messages.error(request, "Not a superuser")
                return redirect('admin-signin') 
            
        else:
            messages.error(request, "Invalid username")
            return redirect('admin-signin') 

        
    return render(request,'admin-control/admin-signin.html')

# =========================admin home ==================

@login_required(login_url='admin-signin')
@cache_control(no_cache = True, must_revalidate = True, no_store = True)
def admin_home(request):
    users = User.objects.all()
    context={
        'home_or_not': True,
        'users' : users,
    }

    return render(request, 'admin-control/admin-home.html', context)



def user_control(request, id):
    user = User.objects.get(id = id)
    user.is_active = not user.is_active
    user.save()
    return redirect('admin-home')



def user_update(request, id):
    user = User.objects.get(id=id)
    form = UpdateForm(instance=user)
      

    if request.method == 'POST':
    
        form = UpdateForm(request.POST,instance = user)
        if form.is_valid():

            form.save()
            # username    = form.cleaned_data['username']
            # first_name  = form.cleaned_data['first_name']
            # last_name   = form.cleaned_data['last_name']
            # email       = form.cleaned_data['email']


            # user = User.objects.create(
            #     username = username,
            #     first_name = first_name,
            #     last_name = last_name,
            #     email = email
            # )
            # user.set_password(password)
            # user.save()
            messages.success(request, 'Account edited successfully')
            return redirect('admin-home')
        else:
            messages.error(request,form.errors)
            return redirect('user_update')



    context = {
        'form': form,
        'user': user,
        }
    return render(request,'admin-control/admin-update.html',context)


def user_create(request):
    

      if request.method == 'POST':
        
            form = UpdateForm(request.POST)
            if form.is_valid():
                password    = request.POST.get('password')
                user = form.save(commit=False)

                user.set_password(password)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('admin-home')
            else:
                messages.error(request, form.errors)
                return redirect('admin-home')


def user_delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return redirect('admin-home')
    except Exception as e:
        print(e)
        return redirect('admin-home')
    

