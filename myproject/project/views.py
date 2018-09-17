from django.shortcuts import render,redirect
from .models import User, Female_IMS, History_IMS
from django.http import JsonResponse

# Create your views here.
def index(request):
    pass
    return render(request,'project/index.html')
 
def login(request):
    if request.session.get('is_login',None):
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("try login id: "+username+password)
        message = 'all fields should be filled'
        if username and password:  # make sure username not blank
            username = username.strip()
            # more validations can be added here
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.uid
                    request.session['user_name'] = user.username
                    request.session['sex'] = user.sex
                    print("login id: %d" % user.uid)
                    return redirect('/')
                else:
                    message = "password incorrect"
            except:
                message = "cannot find user"
        return render(request, 'project/login.html', {"message": message})
    return render(request, 'project/login.html')
 
def register(request):
    if request.session.get('is_login',None):
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        print("try register id: "+username+password1+gender)
        message = 'all fields should be filled'

        if password1 != password2:
            message = "Password must be same!"
            return render(request, 'project/register.html', {"message": message})
        else:
            same_name_user = User.objects.filter(username=username)
            if same_name_user:
                message = 'Username existed!'
                return render(request, 'project/register.html', {"message": message})

            new_user = User.objects.create()
            new_user.username = username
            new_user.password = password1
            new_user.sex = gender
            new_user.save()

            request.session['is_login'] = True
            request.session['user_id'] = new_user.uid
            request.session['user_name'] = new_user.username
            request.session['sex'] = new_user.sex
            return redirect('/login/')  #jump to login
    return render(request,'project/register.html')
 
def logout(request):
    if not request.session.get('is_login', None):
        # if not logged in
        return redirect("/")
    request.session.flush()
    # or use below
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/')

#---------------------------------------------------------------------------

def ims(request):
    if not request.session.get('is_login', None):
        return redirect("/login")

    if request.method == "POST":
        user = User.objects.filter(uid=request.session.get('user_id'))
        try:
            
            #print('successful transform str to int and username: '+str(user.pk))
            print(request.session.get('user_name'))
            age = int(request.POST.get('age','0'))
            gender = request.POST.get('gender','')
            gs = int(request.POST.get('gs','0')) #cannot input nothing
            apfs = int(request.POST.get('apfs','0'))
            ads = int(request.POST.get('ads','0'))
            kfs = int(request.POST.get('kfs','0'))
            kes = int(request.POST.get('kes','0'))
            has = int(request.POST.get('has','0'))
            hers = int(request.POST.get('hers','0'))
            hirs = int(request.POST.get('hirs','0'))
            efs = int(request.POST.get('efs','0'))
            ees = int(request.POST.get('ees','0'))
            sers = int(request.POST.get('sers','0'))
            sirs = int(request.POST.get('sirs','0'))

        except:
                message = 'invalid input'
                return render(request, 'project/ims.html', {"message": message})
        message = 'all fields should be filled'

        if not user:
            message = 'please login'
            return render(request, 'project/ims.html', {"message": message})

        if age > 100 or age < 3:
            message = "Invalid age!"
            return render(request, 'project/ims.html', {"message": message})
        else:
            new_history = History_IMS.objects.create()
            new_history.userid = request.session.get('user_id')
            new_history.age = age
            new_history.sex = gender

            new_history.gs = gs
            new_history.apfs = apfs
            new_history.ads = ads
            new_history.kfs = kfs
            new_history.kes = kes
            new_history.has = has
            new_history.hers = hers
            new_history.hirs = hirs
            new_history.efs = efs
            new_history.ees = ees
            new_history.sers = sers
            new_history.sirs = sirs
            
            new_history.save()

            return redirect('/ims/result')  #jump to login
    return render(request,'project/ims.html')

def ims_result(request):
    pass
    return render(request,'project/ims_result.html')

def json(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

def test_json(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)