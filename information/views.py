from django.shortcuts import render
from information.models import Information
# Create your views here.


def postinformation(request):
    if request.method=='POST':
        obj=Information()
        obj.information=request.POST.get('information')
        obj.date=request.POST.get('date')
        obj.save()
    return render(request,'information/POST INFORMATION.html')




def viewinformation(request):
    ob=Information.objects.all()
    context={
        'objval':ob,
    }
    return render(request,'information/VIEW_INFORMATION.HTML', context)