from django.shortcuts import render,redirect
from . models import Patinet

# Create your views here.
def home(request):
    data =Patinet.objects.all()

    return render(request,'home.html',{'data':data})
def add(request):
    if request.method=='POST':
        print('added')
        fn=request.POST.get('p_fname')
        ln=request.POST.get('p_lname')
        ph=request.POST.get('p_phone')
        em=request.POST.get('p_eamil')

        p=Patinet()
        p.fname=fn
        p.lname=ln
        p.phone=ph
        p.email=em
        p.save()
        return redirect('/')
    return render(request,'add.html')

def delete(request,id):
    p=Patinet.objects.get(id=id)
    p.delete()
    return redirect('/')
def update(request,id):
        fn=request.POST.get('p_fname')
        ln=request.POST.get('p_lname')
        ph=request.POST.get('p_phone')
        em=request.POST.get('p_Eamil')
        p=Patinet.objects.get(id=id)
        p.fname=fn
        p.lname=ln
        p.phone=ph
        p.email=em
        p.save()
        return redirect('/')
