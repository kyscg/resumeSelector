from django.contrib import auth
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage


from .forms import  LoginForm, SignUpForm, UploadResumeForm, EditUserProfileForm, QueryForm
from .models import Document, User


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
    msg = ""
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
    msg = ""
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
    msg = ""

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
                msg = 'Invalid credential entered'

        else:
            msg = 'Error valadating form'

    return render(request, 'account/login.html', {'form':form, 'msg':msg})



def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
    # pass
    msg = ""

    print("In register method")
    
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid() and form.cleaned_data.get("is_applicant") and form.cleaned_data.get("is_recruiter"):
            msg = 'Invalid credentials'
            print("HI")
        
        elif form.is_valid() and (not form.cleaned_data.get("accept_t_n_c")) :
            msg = "Invalid credentials"
            print("In terms section.")
        
        elif form.is_valid():
            print("bye")
            print("is applicant")
            print(form.cleaned_data.get("is_applicant"))
            print("is recruiter")
            print(form.cleaned_data.get("is_recruiter"))
            user = form.save()
            msg = 'Invalid Credentials'
            return redirect('login_view')
        else:
            if form.cleaned_data.get("password1") != form.cleaned_data.get("password2"):
                # print("Password mismatch")
                msg = "Invalid credentials."
            else:
                print("in else")
                msg = 'Invalid Credentials.'
    else:
        form = SignUpForm()
    
    return render(request, 'account/register.html', {'form': form, 'msg': msg})


def rec_query(request):
    msg = ""
    if request.method == "POST":
        form = QueryForm(request.POST, request.FILES)
        print(form)

        if(form.is_valid()):
            query = form.cleaned_data.get("query")
            query1 = query.split(',')
            print(query1)
            
            l1 = len(query1)
            context = []
            for i in range (0,l1):
                q = 'SELECT id,username,email,pdf_resume FROM account_user WHERE skills LIKE "%%'
                q += str(query1[i])
                q += '%%";'

                data = User.objects.raw(q)
                context.append(data)
        
            args = {}

            database = User.objects.all()
            l2 = len(database)
            print(l2)
            count = [0]*l2
            for i in range (0, l2):
                for j in range (0,l1):
                    for k in range (0,len(context[j])):
                       if database[i].id == context[j][k].id:
                           count[i] += 1
            # sort in values
            sorted =[]

            for i in range(l2):
                sorted.append([count[i],i])
            sorted.sort(reverse=True)
            sort_index=[]
            for x in sorted:
                if x[0]!=0:
                    sort_index.append(x[1])

            # finally write into data 
            final_data =[]
            l3 = len(sort_index)
            for i in range(0,l3):
                final_data.append(database[sort_index[i]])
            if(len(data) > 0):
                args["data"] = final_data
                print(args)
            else:
                args["data"] = ""
                pass
            
        return render(request, 'account/query_results.html', args)
    else:
        form = QueryForm()
        return render(request, 'account/query.html', {'form': form, 'msg': msg})

def rec_results(request):
    pass
