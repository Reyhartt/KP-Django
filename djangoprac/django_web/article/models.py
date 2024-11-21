from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")   # Bu alan User tablosuna işaret ediyor.
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = CKEditor5Field('İçerik', config_name='extends')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi") # Anlık saati otomatik olarak ekle.
    article_image = models.FileField(blank=True, null=True, verbose_name="Makale Fotoğrafı")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_author = models.CharField(max_length=40, verbose_name="İsim")
    comment_content = models.CharField(max_length=250, verbose_name="Yorum İçeriği")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Yorum Tarihi")

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
