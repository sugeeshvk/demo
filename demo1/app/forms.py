from django import forms
from app.models import manage

class manageforms(forms.ModelForm):
    class Meta:
        model=manage
        fields="username","password","types",