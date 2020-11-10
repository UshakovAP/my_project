from django.forms import ModelForm, Form
from . import models
from django import forms
from .models import spisok_ispolnitelei, obl_kod, qual_opit, publications, pokazateli, dissertation, ohr_doc, block1, block2, block3, block4

class spisok_ispolniteleiForm(ModelForm):
    class Meta:
        model = spisok_ispolnitelei
        fields = "__all__"
        widgets = {
            'fio': forms.TextInput(attrs={'style': 'width: 450px;'}),
            'mg': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
            'vs': forms.TextInput(attrs={'placeholder': 'X.XX', 'pattern': '\d+(\.\d{2})?', 'style': 'width: 50px;'}),
        }

class obl_kodForm(ModelForm):
    class Meta:
        model = obl_kod
        fields = "__all__"
        widgets = {
            'kod': forms.TextInput(attrs={'placeholder': 'XX.XX.XX', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,2}', 'style': 'width: 75px;'}),
            'nazvaniye': forms.TextInput(attrs={'style': 'width: 450px;'}),
        }

class qual_opitForm(ModelForm):
    class Meta:
        model = qual_opit
        fields = "__all__"
        widgets = {
            'naimenovaniye': forms.TextInput(attrs={'style': 'width: 1000px;'}),
        }

class publicationsForm(ModelForm):
    class Meta:
        model = publications
        fields = "__all__"
        widgets = {
            'naimenovaniye': forms.TextInput(attrs={'style': 'width: 1000px;'}),
            'authors': forms.TextInput(attrs={'style': 'width: 1055px;'}),
            'journal': forms.TextInput(attrs={'style': 'width: 1055px;'}),
            'data': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
        }

class pokazateliForm(ModelForm):
    class Meta:
        model = pokazateli
        fields = "__all__"
        widgets = {
            'koliz': forms.TextInput(attrs={'style': 'width: 750px;'}),
            'kolvo': forms.TextInput(attrs={'style': 'width: 50px;'}),
        }

class dissertationForm(ModelForm):
    class Meta:
        model = dissertation
        fields = "__all__"
        widgets = {
            'nazvaniye': forms.TextInput(attrs={'style': 'width: 1000px;'}),
            'authors': forms.TextInput(attrs={'style': 'width: 1112px;'}),
            'n_s': forms.TextInput(attrs={'placeholder': 'XX.XX.XX', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,2}', 'style': 'width: 75px;'}),
            'data': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
        }

class ohr_docForm(ModelForm):
    class Meta:
        model = ohr_doc
        fields = "__all__"
        widgets = {
            'naimenovaniye': forms.TextInput(attrs={'style': 'width: 1000px;'}),
            'authors': forms.TextInput(attrs={'style': 'width: 1000px;'}),
            'nomer_ohr_doc': forms.TextInput(attrs={'placeholder': 'XXXXXXXXXX', 'pattern': '[0-9]{10}', 'style': 'width: 105px;'}),
            'data': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
        }

class block1Form(ModelForm):
    class Meta:
        model = block1
        fields = "__all__"
        widgets = {
            'tematika': forms.TextInput(attrs={'style': 'width: 1070px;'}),
            'fio': forms.TextInput(attrs={'style': 'width: 450px;'}),
            'str_podr': forms.TextInput(attrs={'style': 'width: 750px;'}),
        }
        
class block2Form(ModelForm):
    class Meta:
        model = block2
        fields = "__all__"
        widgets = {
            'n_v_r': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
            'o_v_r': forms.TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'pattern': '\d{1,2}\.\d{1,2}\.\d{1,4}', 'style': 'width: 105px;'}),
        }

class block3Form(ModelForm):
    class Meta:
        model = block3
        fields = "__all__"

class block4Form(ModelForm):
    class Meta:
        model = block4
        fields = "__all__"