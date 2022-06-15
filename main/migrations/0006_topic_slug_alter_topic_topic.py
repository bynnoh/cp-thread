# Generated by Django 4.0.5 on 2022-06-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]