from django.db import models


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


class Advertisement(CoreModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='advertisement_image', blank=True, null=True)
    video = models.FileField(upload_to='advertisement_video', blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    active_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}  &  {self.active_time}"


class Subscription(CoreModel):
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.email}  &  {self.created_date}"
