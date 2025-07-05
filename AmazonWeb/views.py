from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def fresh(request):
    return render(request,"fresh.html")

def minitv(request):
    return render(request,"minitv.html")