# Generated by Django 5.1.5 on 2025-02-06 09:42

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_remove_news_image_remove_news_text_news_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='image',
        ),
        migrations.AlterField(
            model_name='ads',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Содержание новости'),
        ),
    ]
