from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    d,m,y = now.day, now.month, now.year 
    return render(request, "newyear/index.html", {"is_newyear": d==1 and m==1})
