from django.shortcuts import render
from donor.models import Donor
from login.models import Login
# Create your views here.


def registertdonor(request):
    if request.method == 'POST':
        obj = Donor()
        obj.name = request.POST.get('name')
        obj.phone = request.POST.get('phone')
        obj.address = request.POST.get('address')
        obj.email = request.POST.get('email')
        obj.save()

        ob = Login()
        ob.username = request.POST.get('name')
        ob.password = request.POST.get('p')
        ob.type = 'donor'
        ob.uid = obj.doid
        ob.save()

    return render(request,'donor/REGISTER_DONOR.html')




def viewdonor(request):
    ob = Donor.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'donor/VIEW&FORWARD_DONOR.html', context)