from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FormFileUpload(forms.Form):
    archivo = forms.FileField()
    
    def clean_archivo(self):
        data = self.cleaned_data["archivo"]
        
        if data.name.strip().split(".")[1].lower() != "json":
            raise ValidationError(_("El archivo no es un JSON válido."))
        
        return data