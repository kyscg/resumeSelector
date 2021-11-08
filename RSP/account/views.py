from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


from .forms import  LoginForm, SignUpForm, UploadResumeForm, EditUserProfileForm
# from .models import Document


# Create your views here.
def index(request):
    print(request.user.is_anonymous)
    print(request.user.is_authenticated)
    return render(request, 'index.html')

def profile(request):
    # print(request.user.is_anonymous)
    # print(request.user.is_authenticated)
    return render(request, 'account/profile.html')

def edit_profile(request):
    # print(request.user.is_anonymous)
    # print(request.user.is_authenticated)
    msg = None
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            
            form.save()
            return redirect('profile')
        else:
            msg = "resume upload failed"
    else:
        form = EditUserProfileForm(instance=request.user)
        
        return render(request, 'account/edit_profile.html', {'form': form})

def upload_resume(request):
    # print(request.user.is_anonymous)
    # print(request.user.is_authenticated)
    msg = None
    if request.method == 'POST':
        form = UploadResumeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            uploaded_file = request.FILES['pdf_resume']
            print(uploaded_file.name)
            print(uploaded_file.size)
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)

            # if a unique name is generated
            url = fs.url(name)
            print(url)
            form.save()
            return redirect('profile')
        else:
            msg = "resume upload failed"
    else:
        form = UploadResumeForm(instance=request.user)
        
        return render(request, 'account/upload_resume.html', {'form': form})

def login_view(request):
    # pass
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(username, password)
            print(user)
            if user is not None and user.is_applicant and user.is_recruiter:
                msg = 'invalid role permissions'

            if user is not None and user.is_admin:
                login(request, user)
                # return redirect('adminpage')
            if user is not None and user.is_recruiter:
                login(request, user)
                return redirect('profile')
            if user is not None and user.is_applicant:
                login(request, user)
                return redirect('profile')
            
            else:
                msg = 'invalid credential entered'

        else:
            msg = 'eroor valadating mfrom'

    return render(request, 'account/login.html', {'form':form, 'msg':msg})



def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    # pass
    msg = None

    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        
        if form.is_valid() and form.cleaned_data.get("is_applicant") and form.cleaned_data.get("is_recruiter"):
            
            msg = 'Please select only one role'
        elif form.is_valid():
            # uploaded_file = request.FILES['pdf_resume']
            # print(uploaded_file.name)
            # print(uploaded_file.size)

            print("is applicant")
            print(form.cleaned_data.get("is_applicant"))
            print("is recruiter")
            print(form.cleaned_data.get("is_recruiter"))
            user = form.save()
            msg = 'user created successfully'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    
    return render(request, 'account/register.html', {'form': form, 'msg': msg})

