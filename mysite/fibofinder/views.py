from django.shortcuts import render
import time
from django.core.exceptions import ValidationError
from fibofinder.models import Fibonacci

def get_fibonacci_number(num):
    num1 = 0
    num2 = 1
    if num==0:
        return num1
    elif num==1:
        return num2
    iter=1
    while(iter<=num):
        a = num1
        num1 = num1 + num2
        num2 = a
        iter+=1
    return num1

def opening_page(request):
    start_time = time.time()
    obj = None
    if request.GET.get("get_number"):
        num = int(request.GET.get("get_number"))
        if num>=0:
            obj = Fibonacci.objects.get_or_create(number=num,defaults={"number":num,"fibo_number":get_fibonacci_number(num)})
    end_time = time.time()
    time_taken = end_time - start_time
    context=None
    if obj:
        context = {
            "time_taken":time_taken,
            "fibonacci_number": obj[0].fibo_number
        }
    return render(request, 'fibonacci.html', context=context)
