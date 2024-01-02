from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'description')
        widgets = {
            'name': forms.TextInput(attrs ={"placeholder":"Name","class":"form-control"}),
            'email': forms.EmailInput(attrs ={"placeholder":"Email","class":"form-control"}),
            'description': forms.Textarea(attrs ={"placeholder":"Message","class":"form-control"}),
        }