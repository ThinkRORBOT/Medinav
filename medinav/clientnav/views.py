from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import usrCredentials, mixedDrugs, ingrediantList, drugIngrediant 
from django.views.decorators.csrf import csrf_exempt
import logging


logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def reset_pwd(request):
    if request.method == 'POST':
        response_dict = request.POST.dict()
        password = response_dict['pwd']
        username = response_dict['u_name']        
        
        usr_credentials = usrCredentials()
        status = usrCredentials.objects.filter(u_name=username).update(u_pwd=password)
        print(status)

        usr_credentials.save()        
        
        usr_credentials = usrCredentials()
        # status = 1 if successful, 0 if username not found
        if (status == 1):
            return JsonResponse({'status':'200'})
        elif (status == 0):
            return JsonResponse({'status':'401'})
        
    return render(request, 'clientnav/forgotpwd.html')

@csrf_exempt
def index(request):
    if request.method == 'POST':
        response_dict = request.POST.dict()
        password = response_dict['pwd']
        username = response_dict['u_name']
        
        usr_credentials = usrCredentials();
        num = usrCredentials.objects.filter(u_name=username, u_pwd=password)
        print(num.count())
        if (num.count() == 1):
            return JsonResponse({'status':'200'})
        elif (num.count() == 0):
            return JsonResponse({'status':'401'})
    return render(request, 'clientnav/index.html')

@csrf_exempt
def get_index(request):

    return render(request, 'clientnav/index.html')

def get_help(request):
    return render(request, 'clientnav/help.html')

@csrf_exempt
def get_selectmix(request):
    if request.method == 'POST':
        response_dict = request.POST.dict()
        drug_id = response_dict['drug_id']
        request.session['drug_id'] = drug_id
        if (True):
            # maybe test for something later on like if it's available
            return JsonResponse({'status':'200'})
    selectmix = mixedDrugs.objects.all()
    data = {
        "mixedDrugs": selectmix,
    }
    return render(request, 'clientnav/selectmix.html', data)

@csrf_exempt
def get_showmix(request):
    showmix = drugIngrediant.objects.filter(d_id=request.session['drug_id'])
    drug_name = mixedDrugs.objects.filter(d_id = request.session['drug_id'])[0].d_name
    if request.method == 'POST':
        response_dict = request.POST.dict()
        action = response_dict['action']
        
        # response of 1 = return, 0 = reset
        print(showmix)
        
        for item in showmix:
            item_id = item.i_id
            status = 0
            if (action == '1'):
                status = ingrediantList.objects.filter(i_id=item_id).update(required='T')
            elif (action == '0'):
                status = ingrediantList.objects.filter(i_id=item_id).update(required='F')
            if (status == 0):
                return JsonResponse({'status':'401'})
        return JsonResponse({'status':'200'})

    if showmix.count() == 0:
        print("show an error page here")
    print(showmix)
    ingrediantlist = ingrediantList.objects.all()
    data = {
        "drug_name": drug_name,
        "drugIngrediants": showmix,
        "ingrediantList": ingrediantlist
    }
    return render(request, 'clientnav/showmix.html', data)
