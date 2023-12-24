from django.shortcuts import render
from .forms import ExploreForm

# Create your views here.
def djangoForm(request):
    form=ExploreForm()
    return render(request,'forms.html',{'form':form})

