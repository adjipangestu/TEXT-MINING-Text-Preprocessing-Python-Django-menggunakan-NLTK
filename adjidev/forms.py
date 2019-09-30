from django import forms
from adjidev.models import Kelas, Abstract

class KelasForm(forms.ModelForm):
    nama_kelas = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nama Kelas'}))
    class Meta:  
        model = Kelas
        fields = '__all__'

class AbstractForm(forms.ModelForm):
    abstract = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Abstrak'}))
    class Meta:
        model = Abstract
        fields = '__all__'

