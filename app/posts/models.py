import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Title", max_length=150)
    content = models.TextField(verbose_name="Content", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

@receiver(post_save, sender=Post)
def get_json_content(sender, instance, created, **kwargs):
  if instance.pk <= 100 and len(instance.content) == 0:
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{instance.pk}")
    target_content = response.json().get("body")
    instance.content = target_content
    instance.save()