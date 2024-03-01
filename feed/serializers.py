from rest_framework import serializers
from feed.models import *


class UserSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    personalized_items = serializers.JSONField(allow_null=True)

    def create(self, validated_data):
        return ClientUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.login = validated_data.get('login', instance.login)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        return instance

    def update_items(self, instance, validated_data):
        instance.personalized_items = validated_data.get('personalized_items', instance.personalized_items)
        instance.save()

        return instance

class ParentClassSerializer(serializers.Serializer):
    share_link = serializers.URLField(max_length=200)
    likes = serializers.IntegerField(default=0)

    def get_like(self):
        ParentClass.objects.get(pk=self.parent.pk).likes += 1


class QuranAyahOfDaySerializer(ParentClassSerializer):
    title = serializers.CharField(allow_blank=False, max_length=100)
    ayah = serializers.IntegerField(default=1)
    arabic_text = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        return QuranAyahOfDay.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.ayah = validated_data.get('ayah', instance.ayah)
        instance.arabic_text = validated_data.get('arabic_text', instance.arabic_text)
        instance.save()

        return instance


class HadithOfDaySerializer(ParentClassSerializer):
    title = serializers.CharField(allow_blank=False, max_length=100)
    hadith_text = serializers.CharField(allow_blank=False, style={'base_template': 'textarea.html'})
    author = serializers.CharField(allow_blank=False, max_length=100)

    def create(self, validated_data):
        return HadithOfDay.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.hadith_text = validated_data.get('hadith_text', instance.hadith_text)
        instance.author = validated_data.get('author', instance.author)
        instance.save()

        return instance


class InspiringPictureSerializer(ParentClassSerializer):
    image_url = serializers.ImageField(required=True)
    theme = serializers.ChoiceField(choices=InspiringPicture.DEFAULT_THEMES)

    def create(self, validated_data):
        return InspiringPicture.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.theme = validated_data.get('theme', instance.theme)
        instance.save()

        return instance


class YouTubeVideoSerializer(ParentClassSerializer):
    preview_image = models.ImageField(upload_to=upload_video_preview)
    local_play = models.BooleanField(default=False)
    video_url = models.URLField(max_length=200)

    def create(self, validated_data):
        return YoutubeVideo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.preview_image = validated_data.get('preview_image', instance.preview_image)
        instance.local_play = validated_data.get('local_play', instance.local_play)
        instance.video_url = validated_data.get('video_url', instance.video_url)
        instance.save()

        return instance


class DhikrByUserSerializer(ParentClassSerializer):
    title = serializers.CharField(allow_blank=False, max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def create(self, validated_data):
        return DhikrByUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.last_updated = validated_data.get('last_updated', instance.last_updated)
        instance.save()

        return instance
