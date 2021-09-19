from django.shortcuts import render
from allocate_inmates.models import AllocateInmates
from  donation.models import Donation
###
from inmates.models import Inmates

# Create your views here.
def allocatedonation(request):
    eid=str(request.session["uid"])
    ob = Donation.objects.filter(status='allocate to camp',detail=eid)


    oc = Inmates.objects.all()
    context = {
        'objval': ob,
        'obval': oc
    }

    if request.method=='POST':
        obj=AllocateInmates()
        obj.date=request.POST.get('date')
        obj.donation=request.POST.get('donation')
        obj.iid=request.POST.get('select')
        obj.cid=eid
        obj.save()


    return render(request,'allocate_inmates/ALLOCATE_DONATION_INMATES.html', context)


