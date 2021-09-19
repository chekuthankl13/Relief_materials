from django.shortcuts import render
from camp_requirement.models import CampRequirement
# Create your views here.




def requestcamprequirement(request):
    if request.method=='POST':
        obj=CampRequirement()
        obj.date=request.POST.get('date')
        obj.requirements=request.POST.get('requirement')
        obj.status = 'pending'
        obj.save()
    return render(request,'camp_requirement/REQUEST_CAMP_REQUIREMENT.html')




def viewcamprequirement(request):
    ob = CampRequirement.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'camp_requirement/VIEW_STAUS_CAMP_REQUIREMENT.html', context)



def managecamprequest(request):
    ob = CampRequirement.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'camp_requirement/MANGE CAMP_REQUEST.HTML', context)


def capprove(request,idd):
    obj=CampRequirement.objects.get(crid=idd)
    obj.status='ápprove'
    obj.save()
    return managecamprequest(request)



def creject(request,idd):
    obj=CampRequirement.objects.get(crid=idd)
    obj.status='reject'
    obj.save()
    return managecamprequest(request)
