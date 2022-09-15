from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    longlink = forms.CharField(  
        required=True,
        label="Длинная ссылка",
    )
    title = forms.CharField(  
        widget=forms.HiddenInput,
        required=False
    )
    slug = forms.SlugField(
        required=True,
        label="Идентификатор",
        help_text='Уникальный идентификатор'
    )
    name = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )

    class Meta:
        model = Link
        fields = ['longlink', 'title', 'slug', 'name']