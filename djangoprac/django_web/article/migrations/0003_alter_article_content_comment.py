# Generated by Django 5.1.2 on 2024-11-04 20:20

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_image_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='İçerik'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=40, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=250, verbose_name='Yorum İçeriği')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Yorum Tarihi')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='Makale')),
            ],
        ),
    ]