from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import People

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = People.objects.all()
    return render(request, "index.html", {'result':obj, 'result1':obj1})

# def demo(request1):

    # return render(request1, "index.html", {'result1':obj1})
    # name="india"
    # return render(request, "index.html",{'obj':name})

# def calculation(request):
#     x = float(request.GET['num1'])
#     y= float(request.GET['num2'])
#     res1 = x + y
#     res2 = x - y
#     res3 = x * y
#     res4 = x / y
#     return render(request, "result.html", {'result1':res1,'result2':res2,'result3':res3,'result4':res4})

# def subtraction(request):
#     x = float(request.GET['num1'])
#     y= float(request.GET['num2'])
#     res2 = x - y
#     return render(request, "result.html", {'result2':res2})
# def multiplication(request):
#     x = float(request.GET['num1'])
#     y= float(request.GET['num2'])
#     res3 = x * y
#     return render(request, "result.html", {'result3':res3})
# def divison(request):
#     x = float(request.GET['num1'])
#     y= float(request.GET['num2'])
#     res4 = x / y
#     return render(request, "result.html", {'result4':res4})

# def about(request):
#     return render(request, "result.html")
#
# def contact(request):
#     return HttpResponse("hello am contact")