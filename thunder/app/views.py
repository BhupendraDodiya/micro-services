from django.shortcuts import render
import requests

def index(request):
    return render(request,'index.html')

def showall(request):
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
    data = data.json()
    return render(request,'showdata.html',{'data':data})

def showone(request):
    if request.method =="POST":
        id = request.POST['id']
        data = requests.get('http://tanveerpp.pythonanywhere.com/product/'+id)
        data = data.json()
        return render(request,'showdata.html',{'data':[data]})
    
def add(request):
    if request.method =="POST":
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        company = request.POST['company']
        details = {'name':name,'price':price,'cat':category,'cmp':company}
        requests.post('http://tanveerpp.pythonanywhere.com/product/',details)
        data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
        data = data.json()
        return render(request,'showdata.html',{'data':data})
    
def delete(request):
    id = request.GET['id']
    requests.delete('http://tanveerpp.pythonanywhere.com/product/'+id)
    data=requests.get('http://tanveerpp.pythonanywhere.com/product/')
    data=data.json()
    return render(request,'showdata.html',{'data':data})

def update(request):
    if request.method =='POST':
        id = request.POST['hide']
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        company = request.POST['company']
        data = {'name':name,'price':price,'cat':category,'cmp':company}
        requests.put('http://tanveerpp.pythonanywhere.com/product/'+id+'/',data)
        data=requests.get('http://tanveerpp.pythonanywhere.com/product/')
        data=data.json()
        return render(request,'showdata.html',{'data':data})




        