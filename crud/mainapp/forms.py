from mainapp.models import Article
from django import forms
from django.core import validators

class FormArticle(forms.ModelForm):
    class Meta:
            model = Article
            fields = '__all__'

    title = forms.CharField(
        label="Article Name",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the article name',
                'class': "title_form_article"
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'Article name very short'),
            validators.MaxLengthValidator(20, 'Very long article name '),
            
        ]
    )

    content = forms.CharField(
        required=True,
        label="Article Description",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(60, 'Very long description '),
        ]
    )
    content.widget.attrs.update({
        'placeholder': 'Enter article description',
        'class': "content_form_article",
        'id': 'contenido_form'
    }
    )

    image = forms.ImageField(required=True)

