from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from common.models import Tag


img_max_size = 256 # kilobytes

def validate_image_res(img):
    if 600 < img.width:
        raise ValidationError(f'Bu ne ufacık? Eni olsun en az 600px.')

    if img.size//1024 > img_max_size:
        raise ValidationError(f'Resmin dosya boyutu çok büyük. Maximum boyut: {img_max_size}KB')

    if abs(img.width/img.height-16/9)>.1:
        raise ValidationError(f'Resmin oranı uygunsuz. Geçerli oran: ~16:9.')
            
    raise ValidationError(f'Resim istediğim boyutta değil. Geçerli boyutlar: {valid_img_res}')

class PostCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name='Yazı kategorisi')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Post category"
        verbose_name_plural = "Post categories"


class PostTag(models.Model):
    name = models.CharField(max_length=160, verbose_name='Yazı etiketi')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    status_codes = (
        ("d", "Taslak"),
        ("c", "Revize"),
        ("p", "Yayında")
    )
    title = models.CharField(max_length=1400, verbose_name='Başlık')
    summary = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Özet')
    body = RichTextField(max_length=1024**2, verbose_name='Asıl içerik')
    status = models.CharField(max_length=1, choices=status_codes, default="d", verbose_name='Durum')
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=1400,
        unique=True,
    )
    thumbnail = models.ImageField(
        upload_to='blog/thumbnails', 
        default='blog/none.png',
        max_length=1024,
        validators=[validate_image_res]
        verbose_name='Albüm kapağı',
        )

v
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name='Yazar')

    category = models.ForeignKey(PostCategory, null=True, on_delete=models.SET_NULL, verbose_name='Kategori')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='Etiketler')

    # statistical
    priority = models.IntegerField(default=1, verbose_name='Öncelik')
    read = models.IntegerField(default=1)
    time = models.IntegerField(default=1, verbose_name='Yaklaşık okuma süresi (dk)')

    # autofilled
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    
    def published(self) -> bool:
        return self.status == 'p'

    def author_name(self): pass

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.lower().replace('ı', 'i'), allow_unicode=False)
        if self.time == 0: self.time = len(self.body.split(". ")) // 8
        if not self.published_at and self.published(): self.published_at = self.created_at
        super().save(*args, **kwargs)
