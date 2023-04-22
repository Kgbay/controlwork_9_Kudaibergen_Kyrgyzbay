from django import forms
from django.core.exceptions import ValidationError

from .models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Image
        fields = ('image', 'note')
        widgets = {
            'image': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
        labels = {
            'note': 'Подпись изображения',
            'image': 'Изображения'
        }

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['note']) < 2:
            raise ValidationError("Длина поле должна быть больше двух символов")
        return cleaned_data


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='')