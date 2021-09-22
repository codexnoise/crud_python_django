from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(default='null', verbose_name="Image", upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        db_table = "data_articles"
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-id"]