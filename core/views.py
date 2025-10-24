from django.shortcuts import render, redirect
from .forms import XodimForm
from .models import Xodim
from decimal import Decimal
from django.db.models import Avg,Count,Min,Max


def index(request):
        xodimlar = Xodim.objects.all()
        return render(request,"core/index.html",{"xodimlar":xodimlar})


def create_xodim(request):
        form = XodimForm()
        print(form)

        if request.method =="POST":
            form = XodimForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("index")
        return render(request,"core/create.html", {"form": form})

def search(request):
        pos = request.GET.get("position")
        min = request.GET.get('min')
        max = request.GET.get('max')
        city = request.GET.get('city')
        
        params = {
            "min" : min,
            "max" : max,
            "pos" : pos,
            "city" : city
            
        }

        if not pos and not min and not max and not city :
                return render (request,"core/search.html", {"xodimlar" : []})


        xodimlar = Xodim.objects.all()

        if pos :
            xodimlar = xodimlar.filter(position__contains = pos)

        if min :
            xodimlar = xodimlar.filter(salary__gt = min)

        if max :
            xodimlar = xodimlar .filter(salary__lt = max)

        if city :
            xodimlar = xodimlar.filter(city__contains = city)
            
        print(params)


        return render (request,"core/search.html", {"xodimlar" : xodimlar,"params":params, 'saved': request.GET})

def stat(request):
    ortacha_salary = Xodim.objects.aggregate(Avg("salary"))["salary__avg"]
    soni = Xodim.objects.aggregate(Count("id"))["id__count"]
    min = Xodim.objects.aggregate(Min("salary"))["salary__min"]
    max = Xodim.objects.aggregate(Max("salary"))["salary__max"]
    
    
    stat = {
        "avg" : ortacha_salary,
        "soni" : soni,
        "min" : min,
        "max" : max,
        
    }
    return render(request,"core/stats.html",{"stat": stat})


     
     