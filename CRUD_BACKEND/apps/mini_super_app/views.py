from django.shortcuts import render, redirect
from .models import miniSuperModel
import requests
import json
from .objects import sortAlphabetically, sortNumerically


from api.serializers import miniSuperSerializer

api_url = 'http://localhost:8000/mini_super/api/'


# Vista para hacer get via api y renderizar tabla de usuarios.
def list_users(request):

    req = requests.get(api_url).json()
    req = miniSuperSerializer(req, many=True)
    users = req.data
    return render(request, 'mini_super.html', {'users':users})


# Vista para hacer post via api y renderizar lista de usuarios.
def  add_user(request):

    if request.method == 'POST':                                        
        data = {
                'name':request.POST['name'],
                'paternal_surname':request.POST['p_surname'],
                'maternal_surname':request.POST['m_surname'],
                'age':request.POST['age'],
                'email':request.POST['email'],
                'phone':request.POST['phone'],
            }
        req = requests.post(api_url, json=data)
        response_dict = json.loads(req.text)

                                                                       
        errors = []                                                         
        try:                                                                 
            for key in response_dict:                                    
                errors.append(response_dict[key][0])                     
        except:                                                             
            errors = []                                                     
        if errors:                                                           
            return render(request, 'mini_super_add.html', {'errors':errors})  

        return redirect('list_users')                                      
    return render(request, 'mini_super_add.html')                            


# Vista para hacer put via api a usuario solicitado.
def  edit_user(request, pk):
    
    if request.method == 'POST':
        data = {
                'name':request.POST['name'],
                'paternal_surname':request.POST['p_surname'],
                'maternal_surname':request.POST['m_surname'],
                'age':request.POST['age'],
                'email':request.POST['email'],
                'phone':request.POST['phone'],
            }
        req = requests.put(api_url + str(pk), json=data)
        return redirect('list_users')

    if request.method == 'GET':
        user = miniSuperModel.objects.get(pk=pk)
    return render(request, 'mini_super_edit.html', {'user':user})


# Vista para hacer delete via api a usuario solicitado.
def  delete_user(request,pk):
    req = requests.delete(api_url + str(pk))
    return redirect('list_users')


# Vista para hacer get via api y renderizar tabla de usuarios ordenados alfabeticamente segun su apellido paterno.
def sort_alphabetically(request):
    req = requests.get(api_url).json()
    objects_sorted = sortAlphabetically(list_of_objects=req, field='paternal_surname')
    users = objects_sorted.sort()
    return render(request, 'mini_super.html', {'users':users})


# Vista para hacer get via api y renderizar tabla de usuarios ordenados numerocamente segun su edad de menor a mayor.
def sort_numerically(request):
    req = requests.get(api_url).json()
    objects_sorted = sortNumerically(list_of_objects=req, field='age')
    users = objects_sorted.sort()
    return render(request, 'mini_super.html', {'users':users})

