from django.db import models
from .utils import code_generator, create_shortcode
from .validators import validate_url
# Create your models here.

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qsm = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qsm
        return qs

class KirrURL(models.Model):
    url = models.CharField(max_length=220, validators = [validate_url,])
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if (self.shortcode is None) or self.shortcode=="":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)
