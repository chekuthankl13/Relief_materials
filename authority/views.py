

from django.shortcuts import render
from authority.models import Authority
from login.models import Login
# Create your views here.


def manageauthority(request):
    ob = Authority.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'authority/MANAGE_AUTHORITY.html',context)


def registerauthority(request):
    if request.method =='POST':
        obj=Authority()
        obj.name = request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.email=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.status="pending"
        obj.save()

        ob = Login()
        ob.username = request.POST.get('name')
        ob.password = request.POST.get('p')
        ob.type = 'authority'
        ob.uid = obj.id
        ob.save()
    return render(request, 'authority/REGISTER_AUTHORITY.html')

def approve(request,idd):
    obj=Authority.objects.get(id=idd)
    obj.status='ápprove'
    obj.save()
    return manageauthority(request)



def reject(request,icc):
    obj=Authority.objects.get(id=icc)
    obj.status='reject'
    obj.save()
    return manageauthority(request)
