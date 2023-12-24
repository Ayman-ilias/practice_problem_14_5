from django.shortcuts import render,redirect
from .import forms

def modelform(request):
    if request.method == 'POST':
        model_form = forms.ExploreModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('modelform')
    else:
        model_form = forms.ExploreModelForm
    return render(request, 'model.html', {'form': model_form})

