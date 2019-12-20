from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    所有自定义Model需要继承的超类
    """

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
