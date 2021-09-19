from django.shortcuts import render
from login.models import Login
# Create your views here.


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pssw = request.POST.get('password')
        obj = Login.objects.filter(username=uname,password=pssw)
        if obj:
            tp = ""
            for ob in obj:
                tp = ob.type
                uid = ob.uid
                if tp == 'admin':
                    request.session['uid']=uid
                    return render(request, 'temp/index.html')
                elif tp == 'authority':
                    request.session['uid']=uid
                    return render(request, 'temp/authority.html')
                elif tp=='camp':
                    request.session['uid']=uid
                    return render(request, 'temp/camp.html')
                elif tp=='donor':
                    request.session['uid']=uid
                    return render(request, 'temp/donor.html')
                else:
                    return render(request, 'login/LOGIN.html')
    return render(request,'login/LOGIN.html')
def ad(request):
    return render(request, 'temp/index.html')

def ath(request):
    return render(request, 'temp/authority.html')

def cmp(request):
    return render(request, 'temp/camp.html')

def dn(request):
    return render(request, 'temp/donor.html')

