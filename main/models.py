from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.phone}"


class CoreModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CoreModel):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class News(CoreModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='news_image', null=True, blank=True)
    video = models.FileField(upload_to='news_video', null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}  &  {self.category}  &  {self.views}"


class Media(CoreModel):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='media_icon', null=True, blank=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}  &  {self.link}"


ADVERTISEMENT_TYPE_CHOICES = (
    ('sidebar', 'sidebar'),
    ('banner', 'banner')
)


class Advertisement(CoreModel):
    name = models.CharField(max_length=255)
    advertisement_type = models.CharField(max_length=25, choices=ADVERTISEMENT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='advertisement_image', blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    active_time = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}  &  {self.active_time}"


class Subscription(CoreModel):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.email}  &  {self.created_date}"


class Visits(CoreModel):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.count}"
