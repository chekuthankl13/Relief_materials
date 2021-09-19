from django.shortcuts import render
from donation_request.models import DonationRequest
from donation.models import Donation

from .models import Bchain
from django.db.models import Max
from django.http import HttpResponse
import hashlib
import pyaes
import base64
from datetime import datetime





def genblock(dat):

    hash = hashlib.md5(dat.encode())
    hash = hash.hexdigest()

    fsl = Bchain.objects.all().aggregate(Max('id'))
    pvhash = 0
    fid = list(fsl.values())[0]
    if not (fid is None):
        print(str(fid))
        obj = Bchain.objects.get(id=fid)
        pvhash = obj.hashv
        # print("pvh")
        # print(str(pvhash))

    else:
        pvhash = 0
        fid = 0

    key = "12345"
    key = key.rjust(32, 'a')
    key = key.encode('utf-8')

    aes1 = pyaes.AESModeOfOperationCTR(key)
    ciphertext = aes1.encrypt(dat)
    basestr = base64.b64encode(ciphertext)
    print(basestr)
    ts=datetime.today()
    print(str(ts))

    sobj=Bchain()
    sobj.hashv=hash
    sobj.phashv=pvhash
    sobj.chdata=basestr
    sobj.tstamp=ts
    sobj.save()

    # except:
    #     fsl=0




# Create your views here.



def managedonationrequest(request):
    ob = DonationRequest.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'donation_request/MANAGE_DONATION_REQUEST.html', context)



def requestdonationrequest(request):
    if request.method=='POST':
        obj=DonationRequest()
        obj.request=request.POST.get('request')
        obj.date=request.POST.get('date')
        obj.cid=request.session["uid"]
        obj.status="pending"
        obj.save()
    return render(request,'donation_request/REQUEST DONATION_REQUEST.HTML')


def viewdonationrequest(request):
    ob = DonationRequest.objects.filter(status="approve")
    context = {
        'objval': ob,
    }
    return render(request, 'donation_request/VIEW&FORWARD_DONOR.html', context)


def donorforward(request, iff):
    obj = DonationRequest.objects.get(id=iff)
    obj.status = 'forward'
    obj.save()
    return viewdonationrequest(request)


def viewstatusdonationrequest(request):
    ob = DonationRequest.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'donation_request/VIEW_STATUS_DONATION_REQUEST.html', context)



def viewdonationrequestbydonor(request):
    ob = DonationRequest.objects.filter(status="forward")
    context = {
        'objval': ob,
    }
    return render(request,'donation_request/VIEW_DONATIONREQUEST_BYDONOR.HTML', context)


def approve(request, idd):
    obj = DonationRequest.objects.get(id=idd)
    obj.status = 'approve'
    obj.save()

    # ob = Donation()
    # ob.time = datetime.datetime.now()
    # ob.date = datetime.datetime.today()
    # ob.detail = obj.id
    # ob.doid = request.session["uid"]
    # ob.save()
    # genblock(obj.donation_request + "+ad" + str(obj.id))

    return managedonationrequest(request)
#viewdonationrequestbydonor(request)


def reject(request, icc):
    obj=DonationRequest.objects.get(id=icc)
    obj.status = 'reject'
    obj.save()
    return managedonationrequest(request)
#viewdonationrequestbydonor(request)


##############                   my work -- donor-approve and reject  ################

def doapprove(request, doidd):
    obj = DonationRequest.objects.get(id=doidd)
    obj.status = 'approved by donor'
    obj.save()
    ob = Donation()
    import datetime
    ob.time = datetime.datetime.now().time()
    ob.date = datetime.datetime.today()
    ob.detail = obj.cid
    ob.amount = obj.request
    ob.do_id = request.session["uid"]
    ob.save()
    genblock(obj.request + "+ad" + str(obj.id))
    return viewdonationrequestbydonor(request)


def doreject(request, doicc):
    obj = DonationRequest.objects.get(id=doicc)
    obj.status = 'rejected by donor'
    obj.save()
    return viewdonationrequestbydonor(request)

#
# def doapprove(request, bdd):
#     obj = DonationRequest.objects.get(id=bdd)
#     obj.status = 'ápprove'
#     obj.save()
#
#     ob = Donation()
#     ob.time = datetime.datetime.now()
#     ob.date = datetime.datetime.today()
#     ob.detail = obj.id
#     ob.doid = request.session["uid"]
#     ob.save()
#
#
#     return viewdonationrequestbydonor(request)
#
#
#
# def doreject(request,bcc):
#     obj=DonationRequest.objects.get(id=bcc)
#     obj.save()
#
#     return viewdonationrequestbydonor(request)

