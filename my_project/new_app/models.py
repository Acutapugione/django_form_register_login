from typing import Any, Iterable
from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs) -> None:
        self.pk = 1
        return super(SingletonModel, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs) -> tuple[int, dict[str, int]]:
        return None
        
    @classmethod
    def load(cls):
        obj, is_created = cls.objects.get_or_create(pk=1)
        return obj
    
# Create your models here.
class StyleSettings(SingletonModel):
    background_color = models.TextField(blank=True)
    text_color = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    
    
class Notion(models.Model):
    text = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f"Notion [{self.pk}] {self.text[:15]}..."