# Generated by Django 4.2.3 on 2023-08-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0009_alter_news_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                error_messages={"blank": ["Este campo não pode estar vazio."]},
                max_length=200,
            ),
        ),
    ]