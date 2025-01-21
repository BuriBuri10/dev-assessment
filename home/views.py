from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='logins')
def index(request):
    # context = {'variable1': "Yo", 'variable2': "wassup"}
    #  return HttpResponse("Yo wassup...")
    return render(request, 'index.html')
def superadmin(request):
     return render(request, 'Admin.html')
def profile_page(request):
    return render(request, 'profile_page.html')
def points(request):
    return render(request, 'points.html')
def user_points(request):
    return render(request, 'user_points.html')
def tasks(request):
    return render(request, 'tasks.html')
def notifications(request):
    return render(request, 'no_notif.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            return render(request, 'password_mismatch.html')
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        # print(username, email, password, confirm_password)
    return render(request, 'sign-up.html')
def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'incorrect_password.html')
        # print(username, password)
    return render(request, 'login.html')
def log_out(request):
    logout(request)
    return render(request, 'logout.html')
    
def LinkedIn(request):
    return render(request, 'LinkedIn.html')
def Facebook(request):
    return render(request, 'facebook.html')
def Twitter(request):
    return render(request, 'Twitter.html')
def Instagram(request):
    return render(request, 'Instagram.html')
def Snapchat(request):
    return render(request, 'Snapchat.html')

class MainView(TemplateView):
    template_name = 'main.html'

def file_upload_view(request):
    print(request.FILES)
    return HttpResponse('upload')
    # if request.method == 'POST':
    #     the_file = request.FILES['file']
    #     Doc.objects.create(upload=the_file)
    #     return HttpResponseRedirect('')
    # return HttpResponse({'post':'false'})
