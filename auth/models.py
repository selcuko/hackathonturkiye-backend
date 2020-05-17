from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self): return self.name

class Author(models.Model):

    email = models.EmailField()
    username = models.CharField(max_length=20, default=None)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, null=True, blank=True)

    account_linkedin = models.URLField(verbose_name='LinkedIN Profile URL')

    class Meta:
        ordering = ('first_name',)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

