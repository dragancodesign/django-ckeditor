from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Articles' 

    def __str__(self):
            return self.title