from django.shortcuts import render
from camp.models import Camp
from login.models import Login
# Create your views here.


def managecamp(request):
    ob = Camp.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'camp/MANAGE_CAMP.html', context)


def registercamp(request):
    if request.method=="POST":
        obj=Camp()
        obj.details=request.POST.get('details')
        obj.service=request.POST.get('services')
        obj.place=request.POST.get('place')
        obj.location=request.POST.get('location')
        obj.date=request.POST.get('date')
        obj.name=request.POST.get('name')
        obj.save()

        ob = Login()
        ob.username = request.POST.get('name')
        ob.password = request.POST.get('p')
        ob.type = 'camp'
        ob.uid = obj.cid
        ob.save()
    return render(request,'camp/REGISTER_CAMP.HTML')



def viewcamp(request):
    ob=Camp.objects.all()
    context={
        'objval':ob,
    }
    return render(request,'camp/VIEW_CAMP.html',context)

def approve(request,idd):
    obj=Camp.objects.get(cid=idd)
    obj.status='ápprove'
    obj.save()
    return managecamp(request)


def reject(request,idd):
    obj=Camp.objects.get(cid=idd)
    obj.status='reject'
    obj.save()
    return managecamp(request)


