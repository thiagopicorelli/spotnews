# Generated by Django 4.2.3 on 2023-08-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_news"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(),
        ),
    ]
