import io

from django.core import serializers
from django.shortcuts import render,HttpResponse,redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from userapp.api import loginauth, profileauth


# Create your views here.


@csrf_exempt
def login(request):
    data={'status':404,'message':'Invalid Details'}
    error=0
    if request.session.get('userstatus') == True:
        return redirect('profile')

    if request.method == 'POST' :
        userid=request.POST.get('userID')
        userpwd=request.POST.get('password')
        if len(userid) == 0:
            error='Please Provide User Id'
        if len(userpwd) == 0:
            error='Please Provide Password'
        if not error:
            status=json.loads(loginauth(userid,userpwd))
            if status['status'] == 200:
                print(status)
                print()
                request.session['userID']=userid
                request.session['roleID'] = status['results']['roleID']
                request.session['userstatus'] = 1
                data = {'status': 200, 'message': 'Successfully Logined'}



        return JsonResponse(data,safe=False)
    else:
        return render(request,'login.html',{'error':error})


def profile(request):
    if request.session.get('userstatus') == True:
        data=json.loads(profileauth(request))
        return render(request,'profile.html',{'data':data['results']})
    return redirect('profile')


def loginpage(request):
    return redirect(login)

def logout(request):
    request.session.clear()
    return redirect(login)