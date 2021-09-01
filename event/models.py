from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from PIL import Image
from djrichtextfield.models import RichTextField
from django.utils.text import slugify
from django.core.exceptions import MultipleObjectsReturned
from common.models import Tag


w_allowance_percent = .05  # max 1
h_allowance_percent = .05  # max 1

img_max_size = 256  # kilobytes


def validate_image_res(img):
    if img.width < 600:
        raise ValidationError(f'Bu ne ufacuk resim! Eni en az 600px olsun.')

    if abs(img.width/img.height-16/9) > .1:
        raise ValidationError(
            f'Resmin oranı uygunsuz. ~16:9 oranında resim gerekli.')

    if img.size//1024 > img_max_size:
        raise ValidationError(
            f'Resmin dosya boyutu çok büyük. Maximum boyut: {img_max_size}KB')

    return


class EventType(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Etkinlik türünün adı')
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'etkinlik türü'
        verbose_name_plural = 'etkinlik türleri'


class EventTag(models.Model):
    name = models.CharField(max_length=200, verbose_name='Etiket adı')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'etiket'
        verbose_name_plural = 'etiketler'


class Event(models.Model):
    name = models.CharField(max_length=640, verbose_name='Etkinliğin adı')
    description = models.TextField(
        max_length=1400, null=True, verbose_name='Etkinliğin kısa açıklaması/özeti')
    body = RichTextField(blank=True, null=True,
                         verbose_name='Etkinliğin detaylı açıklaması')
    etype = models.ForeignKey(EventType, on_delete=models.CASCADE,
                              verbose_name="Etkinlik türü")
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=64,
        unique=True
    )

    origin_url = models.URLField(verbose_name='Etkinliğin resmi sitesi')
    internal_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='thumbnails',
        #default='thumbnails/none/placeholder.jpg',
        max_length=1024,
        validators=[validate_image_res],
        verbose_name='Albüm kapağı')
    deadline = models.DateTimeField(
        blank=True, null=True, verbose_name='Son başvuru tarihi')
    starts_at = models.DateTimeField(verbose_name='Başlangıç tarihi')
    ends_at = models.DateTimeField(verbose_name='Bitiş tarihi')
    location = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='Etkinliğin konumu')
    prize = models.CharField(max_length=200, blank=True, null=True,
                             verbose_name='Etkinlikte dağıtılacak toplam para ödülü')
    priority = models.IntegerField(
        default=1, verbose_name='Öncelik (aksi söylenmedikçe 1 bırakın)')
    holder = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Etkinliği düzenleyen kurum')
    published = models.BooleanField(default=True, verbose_name='Yayınla')
    tags = models.ManyToManyField(
        Tag, related_name='events', verbose_name='Alakalı etiketler')

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('priority', '-starts_at',)
        verbose_name = 'etkinlik'
        verbose_name_plural = 'etkinlikler'

    @property
    def url(self):
        return f'https://hackathonturkiye.com/etkinlik/{self.slug}' if self.has_details() else self.origin_url

    def __str__(self):
        return f"{self.name} ({self.starts_at.year})"

    def is_applicable(self):
        return timezone.now() < self.deadline if self.deadline else None

    def has_details(self):
        return bool(self.body)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.lower().replace(
            'ı', 'i'), allow_unicode=False)
        try:
            self.validate_unique()
        except:
            self.slug += f'-{self.pk}'
            self.validate_unique()
        super().save(*args, **kwargs)
