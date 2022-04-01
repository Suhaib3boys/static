from django.shortcuts import render
from .models import WhyItem
from .models import Team


# Create your views here.
def index(request):
    obj = WhyItem.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {'why': obj, 'te': team})

