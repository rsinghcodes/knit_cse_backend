from rest_framework import serializers
from .models import (
    HeroContent, Highlight, Faculty, Alumni, GalleryEvent, GalleryPhoto,
    FeaturedItem, QuickLink, Course, Circular, Notice
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
        fields = ['id', 'name', 'description', 'date', 'location', 'cover_photo', 'cover_photo_url', 'photos', 'created_at']

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


from .models import CourseTimetable, CourseSyllabus

class CourseTimetableSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = CourseTimetable
        fields = ['id', 'course', 'year', 'file', 'file_url', 'created_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None

class CourseSyllabusSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = CourseSyllabus
        fields = ['id', 'course', 'year', 'file', 'file_url', 'created_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None

class CourseSerializer(serializers.ModelSerializer):
    timetables = CourseTimetableSerializer(many=True, read_only=True)
    syllabuses = CourseSyllabusSerializer(many=True, read_only=True)
    brochure_url = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_brochure_url(self, obj):
        request = self.context.get('request')
        if obj.brochure and request:
            return request.build_absolute_uri(obj.brochure.url)
        return None


class CircularSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Circular
        fields = ['id', 'title', 'date', 'file_size', 'language', 'file', 'file_url', 'link', 'order', 'is_active', 'created_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None


class NoticeSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Notice
        fields = ['id', 'title', 'description', 'date', 'file', 'file_url', 'link', 'order', 'is_active', 'created_at']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None

from .models import AboutDepartment, AboutSidebarLink

class AboutDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutDepartment
        fields = '__all__'

class AboutSidebarLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSidebarLink
        fields = '__all__'

from .models import Staff, Student

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'


from .models import StudentListPdf

class StudentListPdfSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = StudentListPdf
        fields = '__all__'

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file and request:
            return request.build_absolute_uri(obj.file.url)
        return None

from .models import ContactInfo, DirectoryEntry

class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class DirectoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectoryEntry
        fields = '__all__'

from .models import HeroBanner

class HeroBannerSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroBanner
        fields = ['id', 'image', 'image_url', 'caption', 'order', 'is_active', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


