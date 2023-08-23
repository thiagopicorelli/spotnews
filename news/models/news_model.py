from django.db import models
from django.core.exceptions import ValidationError
from news.models.category_model import Categories
from news.models.user_model import Users


class News(models.Model):
    def validate_word_count(value):
        if len(value.split()) < 2:
            raise ValidationError(
                'O título deve conter pelo menos 2 palavras.'
            )

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        validators=[validate_word_count],
        error_messages={"blank": ['Este campo não pode estar vazio.']}
    )
    content = models.TextField(
        blank=False,
        null=False,
        error_messages={"blank": ['Este campo não pode estar vazio.']},
    )
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to="img", blank=True, null=True)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
