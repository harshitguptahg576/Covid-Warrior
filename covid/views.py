from django.shortcuts import render
from .models import Product
from .models import Center
import requests

def home(request):
    try:
        result=requests.get("https://api.covid19india.org/data.json")
        Api=requests.get("https://api.covid19india.org/state_district_wise.json")
        district=Api.json()
        
        summary=result.json()["statewise"][0]
        states=result.json()["statewise"]
        param={"summary":summary,"states":states, "district":district}
    except:
        summary={"total":0,"active":0,"recovered":0,"death":0}
        states=[{ "loc": "", "discharged": 0, "deaths": 0, "totalConfirmed": 0 }]
        district={ }
        param={"summary":summary,"states":states, "district":district}
    return render(request, 'covid/home.htm',param)

def centers(request):
 return render(request, 'covid/centers.htm')

def tracker(request):
    try:
        result=requests.get("https://api.covid19india.org/data.json")
        
        summary=result.json()["statewise"][0]
        states=result.json()["statewise"]
        tested=result.json()["tested"][-1]
        timeseries= result.json()["cases_time_series"]
        param={"summary":summary, "tested":tested, "states":states, "timeseries":timeseries}
    except:
        summary={"total":0,"active":0,"recovered":0,"death":0}
        param={"summary":summary}
    return render(request, 'covid/tracker.htm',param)

def safety(request):
    select=request.GET.get('select','blank')
    if select=="category":
        title="Products: Category-Wise"
        categorywise=[]
        products= Product.objects.values('category')
        categories={item['category'] for item in products}
        categories=sorted(categories)
        for cat in categories:
            prod=Product.objects.filter(category=cat)
            categorywise.append(prod)  
        param={"product":categorywise,"title":title}
    else:
        title="All Products"
        products= [Product.objects.all()]
        param= {"product":products, "title":title}
    return render(request, 'covid/safety.htm',param)

def tips(request):
 return render(request, 'covid/tips.htm')

def about(request):
 return render(request, 'covid/about.htm')

def login(request):
 return render(request, 'covid/login.htm')

def hathras(request):
    centers= Center.objects.filter(city="Hathras")
    param={"centers":centers, "title":"Hathras"}
    return render(request, 'covid/mathura.htm',param)

def mathura(request):
    centers= Center.objects.filter(city="Mathura")
    param={"centers":centers, "title":"Mathura"}
    return render(request, 'covid/mathura.htm',param)

def aligarh(request):
    centers= Center.objects.filter(city="Aligarh")
    param={"centers":centers, "title":"Aligarh"}
    return render(request, 'covid/mathura.htm',param)
 