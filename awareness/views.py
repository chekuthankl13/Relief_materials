from django.shortcuts import render
from awareness.models import Awareness
# Create your views here.


def postawareness(request):
    if request.method=='POST':
        obj=Awareness()
        obj.awareness = request.POST.get('awareness')
        obj.date = request.POST.get('date')
        obj.save()

    return render(request,'awareness/POST AWARENESS.html')


def viewawareness(request):
    ob = Awareness.objects.all()
    context = {
        'objval': ob,
    }
    return render(request,'awareness/VIEW_AWARENESS.HTML',context)





