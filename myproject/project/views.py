from django.shortcuts import render,redirect
from .models import User, IMS, History_IMS
from django.http import JsonResponse
import json, simplejson

# Create your views here.
def index(request):
    pass
    return render(request,'project/index.html')


# Login/logout/register
 
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

def ims_submit(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        
        userid = request.session.get('user_id')
        user = User.objects.filter(uid=userid)
        if not user:
            message = {'message':'Please login!','err_type':'login'}
            return JsonResponse(message)

        message = {'message':'Invalid age!','err_type':'invalid_input'}
        try:
            age = int(data['age'])
        except:
            return JsonResponse(message)
        if age > 100 or age < 3:
            return JsonResponse(message)

        gender = data['gender']
        message = {'message':'Invalid sex!','err_type':'invalid_input'}
        try:
            if gender != 'male' and gender != 'female':
                return JsonResponse(message)
        except:
            return JsonResponse(message)

        del data['gender']
        del data['age']

        #print("after del gender&age: "+str(data))

        age_group = get_age_group(age)

        compare_model = IMS.objects.filter(age_group = age_group).filter( sex = gender).values()[0]
        del compare_model['id']
        print("get compare model: ")
        print(compare_model)

        keys = data.keys()
        insert_data = {}
        z_value = 1.96
        for k in keys:
            #print(k)
            try:
                if data[k] == '':
                    insert_data[k] = 0
                else:
                    insert_data[k] = int(data[k])

                lb = compare_model[k + '_mean'] - z_value*compare_model[k + '_sd']
                ub = compare_model[k + '_mean'] + z_value*compare_model[k + '_sd']
                if insert_data[k] < lb:
                    insert_data[k+'_eval'] = 'Weak'
                elif insert_data[k] > ub:
                    insert_data[k+'_eval'] = 'Strong'
                else:
                    insert_data[k+'_eval'] = 'Normal'
            except:
                message = {'message':'Invalid input type!','err_type':'invalid_input'}
                return JsonResponse(message)

        #print('insert_data:')
        #print(insert_data)


        #new_history = History_IMS.objects.create()
        #new_history.userid = request.session.get('user_id')
        new_history = History_IMS(userid = userid, sex = gender, age = age, **insert_data)
        new_history.save()
        new_history = History_IMS.objects.filter(id = new_history.id).values()[0]
        del new_history['id']
        del new_history['userid']
        print('print new history:')
        print(new_history)
        print('data saved!')

        response_data = {'user_raw_data':new_history, 'compare_model':compare_model}
        #print(post_key)
        #name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
        return JsonResponse(response_data)
    return render(request,'project/ims.html')

def get_age_group(age):
    return age
