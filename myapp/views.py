from django.shortcuts import render
from .models import food

# Create your views here.
def index(request):
    Food=food.objects.all()
    return render(request,'myapp/index.html',{'Food':Food})