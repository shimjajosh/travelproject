from django.http import HttpResponse
from django.shortcuts import render
from . models import placeit
from . models import people
# Create your views here.
def demo(request):
    obj=placeit.objects.all()
    obj1 = people.objects.all()
    return render(request, "index.html",{'result':obj,'pics':obj1})
# def home(request):
#     return HttpResponse("welcome home")
#
# def about(request):
#     return render (request,"about.html")
#
# def contact(request):
#     return HttpResponse("contact  us")
#
# def details(request):
#     return render (request,"details.html")
#
# def thanks(request):
#     return HttpResponse("thank you for visiting us")