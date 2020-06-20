from django.db import models

class Image(models.Model):
    friendly_name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='hosting/images')
    uri = models.CharField(max_length=1000)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.uri

    def save(self, *args, **kwargs):
        self.uri = self.image.url
        super().save(*args, **kwargs)
