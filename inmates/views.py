from django.shortcuts import render
from inmates.models import Inmates
from login.models import Login
# Create your views here.

def register(request):
    if request.method=='POST':
        obj=Inmates()
        obj.name=request.POST.get('name')
        obj.age=request.POST.get('age')
        obj.gender=request.POST.get('gen')
        obj.save()

        # ob = Login()
        # ob.username = request.POST.get('name')
        # ob.password = request.POST.get('p')
        # ob.type = 'inmates'
        # ob.uid = obj.iid
        # ob.save()
    return render(request,'inmates/REGISTER_INMATES.html')