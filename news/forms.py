from django import forms
from news.models.user_model import Users

class CreateCategoryForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200, required=True)

class CreateNewsForm(forms.Form):
  authors = Users.objects.all()
  authorChoices = map(lambda e: (e.id, e.name), authors)

  title = forms.CharField(label="Título", max_length=200, required=True)
  content = forms.CharField(label="Conteúdo", widget=forms.Textarea, required=True)
  author = forms.ChoiceField(label="Autoria", choices=authorChoices)