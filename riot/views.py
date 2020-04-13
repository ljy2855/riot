from django.shortcuts import render
from .models import sohwan
from .fun import get_info,count_game

def search(request):
    summ = get_info(requst.get("keyword")
    return render(request, 'riot/search.html',{'summ': summ})

def base(request):
    return render(request, 'riot/base.html',{})





# Create your views here.
