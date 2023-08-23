import datetime
from django import forms
from news.models.user_model import Users
from news.models.category_model import Categories

class CreateCategoryForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=200, required=True)

class CreateNewsForm(forms.Form):

  def __init__(self, *args, **kwargs):
    super(CreateNewsForm, self).__init__(*args, **kwargs)
    authorChoices = map(lambda e: (e.id, e.name), Users.objects.all())
    categoryChoices = map(lambda e: (e.id, e.name), Categories.objects.all())
    self.fields["author"] = forms.ChoiceField(label="Autoria", choices=authorChoices, required=True)
    self.fields["categories"] = forms.MultipleChoiceField(label="Categorias", choices=categoryChoices, widget=forms.CheckboxSelectMultiple, required=True)

  title = forms.CharField(label="Título", max_length=200, required=True)
  content = forms.CharField(label="Conteúdo", widget=forms.Textarea, required=True)
  author = forms.ChoiceField(label="Autoria", required=True)
  created_at = forms.DateField(label="Criado em", widget=forms.DateInput(attrs={"type": "date"}), initial=datetime.date.today().strftime('%Y-%m-%d'), required=True)
  image = forms.ImageField(label="URL da Imagem", required=False)
  categories = forms.MultipleChoiceField(label="Categorias", widget=forms.CheckboxSelectMultiple, required=True)