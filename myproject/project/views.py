from django.shortcuts import render,redirect
from .models import User, IMS, History_IMS, JF, History_JF, FP, History_FP
from django.http import JsonResponse
#from django.core import serializers
import json

# Create your views here.
def index(request):
    pass
    return render(request,'project/index.html')


#--------------------------Login/logout/register--------------------------
 
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

#---------------data API via JSON---------------

def ims(request):
    if not request.session.get('is_login', None):
        return redirect("/login")
    return render(request,'project/ims.html')

def ims_submit(request):
    if request.method == 'POST':
        return insert_and_response(request, IMS, History_IMS)
    message = {'message':'Request method must be POST','err_type':'invalid_request'}
    return JsonResponse(message)

def jf(request):
    if not request.session.get('is_login', None):
        return redirect("/login")
    return render(request,'project/jf.html')

def jf_submit(request):
    if request.method == 'POST':
        return insert_and_response(request, JF, History_JF)
    message = {'message':'Request method must be POST','err_type':'invalid_request'}
    return JsonResponse(message)

def fp(request):
    if not request.session.get('is_login', None):
        return redirect("/login")
    return render(request,'project/fp.html')

def fp_submit(request):
    if request.method == 'POST':
        return insert_and_response(request, FP, History_FP)
    message = {'message':'Request method must be POST','err_type':'invalid_request'}
    return JsonResponse(message)

def history(request):
    if not request.session.get('is_login', None):
        return redirect("/login")
    return render(request,'project/history.html')

def history_get(request):
    if request.method == 'GET':
        userid = request.session.get('user_id')
        ims_h =retrieve_history(userid, IMS, History_IMS)
        jf_h = retrieve_history(userid, JF, History_JF)
        fp_h = retrieve_history(userid, FP, History_FP)
        integrated_data = {'ims_test_history':ims_h, 'jf_test_history':jf_h, 'fp_test_history':fp_h}
        return JsonResponse(integrated_data, safe=False)
    message = {'message':'Request method must be POST','err_type':'invalid_request'}
    return JsonResponse(message)


#-------------------useful functions--------------------

def retrieve_history(userid, test_model, history_obj):
    #data = history_obj.objects.filter(userid = userid).values()
    raw_data = list(history_obj.objects.filter(userid = userid).values())
    history_list = []
    for item in raw_data:
        compare_model = test_model.objects.filter(age_group = get_age_group(item['age'])).filter( sex = item['sex']).values()[0]
        del compare_model['id']
        history_item = {'history_item':item, 'compare_model':compare_model}
        history_list.append(history_item)
    return history_list

def insert_and_response(request, test_model, history_obj):
    if not request.session.get('is_login', None):
        message = {'message':'Please login!','err_type':'login'}
        return JsonResponse(message)

    data = json.loads(request.body)    
    userid = request.session.get('user_id')

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

    age_group = get_age_group(age)
    try:
        compare_model = test_model.objects.filter(age_group = age_group).filter( sex = gender).values()[0]
    except:
        message = {'message':'Invalid compare model!','err_type':'invalid_compare_model'}
        return JsonResponse(message)
    del compare_model['id']
    print("get compare model: ")
    print(compare_model)

    keys = data.keys()
    insert_data = {}
    z_value = 1.96
    for k in keys:
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

    new_history = history_obj(userid = userid, sex = gender, age = age, **insert_data)
    new_history.save()

    new_history = history_obj.objects.filter(id = new_history.id).values()[0]
    del new_history['id']
    del new_history['userid']
    print('print new history:')
    print(new_history)
    print('data saved!')
    response_data = {'user_raw_data':new_history, 'compare_model':compare_model}
    return JsonResponse(response_data)

def get_age_group(age):
    if int(age) < 21:
        return age
    return (age-1)//10*10+1
