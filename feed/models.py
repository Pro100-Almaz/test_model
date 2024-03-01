from django.contrib.auth.models import AbstractUser
from django.db import models


class ClientUser(AbstractUser):
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    personalized_items = models.JSONField(null=True, default=dict)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'login'

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    def get_username(self):
        return self.login

    def __str__(self):
        return self.login


class ParentClass(models.Model):
    share_link = models.URLField(null=True, max_length=200)
    likes = models.IntegerField(null=True, default=0)
    creator = models.ForeignKey(ClientUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.share_link


def upload_image(filename):
    return 'images/{filename}'.format(filename=filename)


def upload_video_preview(filename):
    return 'images/{filename}'.format(filename=filename)


class QuranAyahOfDay(ParentClass):
    title = models.CharField(max_length=100)
    ayah = models.IntegerField(default=1)
    arabic_text = models.TextField()

    def __str__(self):
        return f"{self.title} {self.ayah}"


class HadithOfDay(ParentClass):
    title = models.CharField(max_length=200)
    hadith_text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.author}"


class InspiringPicture(ParentClass):
    DEFAULT_THEMES = [
        ('summer', 'summer'),
        ('winter', 'winter'),
        ('spring', 'winter'),
        ('fall', 'fall'),
        ('masjid', 'masjid'),
        ('mekkah', 'mekkah')
    ]

    title = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True)
    image_url = models.ImageField(upload_to=upload_image)
    theme = models.CharField(max_length=100, choices=DEFAULT_THEMES, default=DEFAULT_THEMES[0])

    def __str__(self):
        return f"{self.theme} {self.image_url}"


class YoutubeVideo(ParentClass):
    preview_image = models.ImageField(upload_to=upload_video_preview)
    title = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True)
    local_play = models.BooleanField(default=False)
    video_url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.preview_image} {self.video_url}"


class DhikrByUser(ParentClass):
    title = models.CharField(max_length=100)
    user_progress = models.IntegerField(null=True, default=0)
    last_updated = models.DateTimeField(auto_now=True)
    user_plan = models.IntegerField(null=True, default=100)

    def __str__(self):
        return f"{self.title} {self.user_progress}"
