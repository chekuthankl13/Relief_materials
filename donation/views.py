from django.shortcuts import render
from donation.models import Donation

# Create your views here.


''''
def managedonation(request):
    ob = Donation.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'donation/MANGE_DONATION.html', context)
'''



from donation_request.models import Bchain
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
    print('hello')
    if not (fid is None):
        # print(str(fid))
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
    # print(basestr)
    ts=datetime.today()
    # print(str(ts))

    sobj=Bchain()
    sobj.hashv=hash
    sobj.phash=pvhash
    # sobj.phashv = 'hhhh'
    sobj.chdata=basestr
    sobj.tstamp=ts
    sobj.save()


    print('-------------')
    print(pvhash)

    # except:
    #     fsl=0


def viewdonation(request):
    ob = Donation.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'donation/VIEW_DONATION.html', context)


def forward(request, idd):
    obj = Donation.objects.get(did=idd)
    obj.status = "forward"
    obj.save()

    # print(obj.detail + "-ad" + str(obj.id))

    genblock(obj.detail + "-ad" + str(obj.did))
    #
    return viewdonation(request)


def vdauthority(request):
    ob = Donation.objects.filter(status='forward')
    contex = {
        'objval':ob,
    }
    return render(request, 'donation/VIEW_DONATION_BY_AUTHORITHY.html', contex)

def acamp(request, icc):
    obj = Donation.objects.get(did=icc)
    obj.status = 'allocate to camp'
    obj.save()

    genblock(obj.detail + "+ad" + str(obj.did))
    return vdauthority(request)