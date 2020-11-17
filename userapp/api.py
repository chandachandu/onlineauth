import requests,io
from django.http import JsonResponse,HttpResponse
import json

def loginauth(userID,password):

    url = "http://140.238.229.203:8080/littlekirana/user/login"

    query={"roleID":"1","userID":userID,"password":password,"tokenID":"SAN/147JAY@258PIJ$369NIK&741SUBH-852LITTLE%963KIRANA"}
    query=json.dumps(query)
    headers = {'Content-type':"application/json"}

    response = requests.request("POST", url,headers=headers, data =query)
    return response.text

def profileauth(request):

    url = "http://140.238.229.203:8080/littlekirana/user/profileview"

    query={"roleID":request.session.get('roleID'),"userID":request.session.get('userID'),"tokenID":"SAN/147JAY@258PIJ$369NIK&741SUBH-852LITTLE%963KIRANA"}
    query=json.dumps(query)
    headers = {'Content-type':"application/json"}

    response = requests.request("POST", url,headers=headers, data =query)
    return response.text