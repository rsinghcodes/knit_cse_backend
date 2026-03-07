from rest_framework import serializers
from .models import (
    HeroContent, Highlight, Faculty, Alumni, GalleryEvent, GalleryPhoto,
    FeaturedItem, QuickLink, Course
)


class HeroContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroContent
        fields = '__all__'


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    cv_url = serializers.SerializerMethodField()

    class Meta:
        model = Faculty
        fields = [
            'id', 'name', 'designation', 'department',
            'photo', 'photo_url', 'cv', 'cv_url',
            'profile_link', 'order',
        ]

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None

    def get_cv_url(self, obj):
        request = self.context.get('request')
        if obj.cv and request:
            return request.build_absolute_uri(obj.cv.url)
        return None


class AlumniSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Alumni
        fields = [
            'id', 'name', 'batch', 'company', 'designation',
            'linkedin', 'photo', 'photo_url',
        ]

    def get_photo_url(self, obj):
        request = self.context.get('request')
        if obj.photo and request:
            return request.build_absolute_uri(obj.photo.url)
        return None


class GalleryPhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryPhoto
        fields = ['id', 'event', 'image', 'image_url', 'caption', 'order', 'uploaded_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class GalleryEventSerializer(serializers.ModelSerializer):
    photos = GalleryPhotoSerializer(many=True, read_only=True)
    cover_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = GalleryEvent
        fields = ['id', 'name', 'description', 'date', 'cover_photo', 'cover_photo_url', 'photos', 'created_at']

    def get_cover_photo_url(self, obj):
        request = self.context.get('request')
        if obj.cover_photo and request:
            return request.build_absolute_uri(obj.cover_photo.url)
        return None

class FeaturedItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = FeaturedItem
        fields = ['id', 'title', 'image', 'image_url', 'file_size', 'language', 'date', 'order', 'is_active', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class QuickLinkSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()

    class Meta:
        model = QuickLink
        fields = ['id', 'title', 'href', 'icon', 'icon_url', 'order', 'is_active']

    def get_icon_url(self, obj):
        request = self.context.get('request')
        if obj.icon and request:
            return request.build_absolute_uri(obj.icon.url)
        return None


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

