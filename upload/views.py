from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .FormFileUpload import FormFileUpload
from modules.archivos import save_json_file

# Create your views here.
def form_upload(request):
    
    ruta_base = request.session.get("ruta_base")
    
    if request.method == 'POST':
        form = FormFileUpload(request.POST, request.FILES)
        
        if form.is_valid():
            save_json_file(ruta_base, form.cleaned_data["archivo"])
            return HttpResponseRedirect(reverse('upload_success'))
        else:
            return render(request, "form.html", {"form" : form})
        
    else:
        form = FormFileUpload()
        return render(request, "form.html", {'form' : form})
    

def upload_success(request):
    return render(request, "success.html")