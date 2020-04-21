from .models import theModel
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

def main(request):

    return render(request, 'application/main.html')

@csrf_exempt
def getApiKey(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            currentModel = theModel.objects.filter(name=data['name'])
            currentModelApiKey = currentModel.apiKey
            return JsonResponse({"objectApiKey": currentModelApiKey})
        else:
            return JsonResponse({"actionStatus": 'Wrong login/passwod'})
    else:
        return JsonResponse({"actionStatus": 'Wrong type of request!'})


@csrf_exempt
def setName(request):

    if request.method == 'POST':
        data = request.POST
        currentModel = theModel.objects.filter(name=data['name'])
        currentModelApiKey = currentModel.apiKey

        if currentModelApiKey == data['apiKey']:
            currentModel.update(name = data['newName'])
            return JsonResponse({"actionStatus": 'Name updated!', "currentName": data['newName']})
        else:
            return JsonResponse({"actionStatus": 'Wrong API key!'})
    else:
        return JsonResponse({"actionStatus": 'Wrong type of request!'})


@csrf_exempt
def setId(request):

    if request.method == 'POST':
        data = request.POST
        currentModel = theModel.objects.filter(name=data['name'])
        currentModelApiKey = currentModel.apiKey

        if currentModelApiKey == data['apiKey']:
            currentModel.update(objectId = data['newObjectId'])
            return JsonResponse({"actionStatus": 'ID updated!', "currentId": data['newObjectId']})
        else:
            return JsonResponse({"actionStatus": 'Wrong API key!'})
    else:
        return JsonResponse({"actionStatus": 'Wrong type of request!'})


@csrf_exempt
def getObjectInfo(request):

    if request.method == 'POST':
        data = request.POST
        currentModel = theModel.objects.filter(name=data['name'])
        currentModelApiKey = currentModel.apiKey

        if currentModelApiKey == data['apiKey']:
            currentModelName = currentModel.name
            currentModelId = currentModel.objectId
            return JsonResponse({"getObjectInfo": 'True', "currentId": currentModelId, "currentName": currentModelName, "currentApiKey": currentModelApiKey})
        else:
            return JsonResponse({"actionStatus": 'Wrong API key!'})
    else:
        return JsonResponse({"actionStatus": 'Wrong type of request!'})
