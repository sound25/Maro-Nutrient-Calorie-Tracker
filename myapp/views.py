from django.shortcuts import render,redirect
from .models import food,consume

# Create your views here.
def index(request):
    if request.method=='POST':
        food_consumed=request.POST['item']
        consumes=food.objects.get(name=food_consumed)
        username='soundarya'
        consume_obj=consume(user=username,food_consumed=consumes)
        consume_obj.save()
        Food=food.objects.all()
    else:
        Food=food.objects.all()
    consumed_items=consume.objects.filter(user=request.user)
    return render(request,'myapp/index.html',{'Food':Food,'consumed_items':consumed_items})

def delete_consume(request,id):
    consumed_food=consume.objects.get(id=id)
    if request.method=='POST':
        consumed_food.delete()
        return redirect('/') 
    return render(request,'myapp/delete.html')


