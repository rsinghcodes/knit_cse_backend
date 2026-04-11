from django.contrib import admin
from .models import HeroContent, Highlight, Faculty, Alumni, GalleryEvent, GalleryPhoto, Circular, Notice, ContactInfo, DirectoryEntry, HeroBanner


@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    pass


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['text', 'href', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'department', 'order']
    list_filter = ['department']
    list_editable = ['order']
    ordering = ['department', 'order', 'name']


@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['name', 'batch', 'company', 'designation']
    list_filter = ['batch']
    ordering = ['-batch', 'name']


@admin.register(GalleryEvent)
class GalleryEventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'created_at']


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['event', 'caption', 'order', 'uploaded_at']
    list_filter = ['event']


@admin.register(Circular)
class CircularAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectoryEntry)
class DirectoryEntryAdmin(admin.ModelAdmin):
    list_display = ['designation', 'name', 'mobile', 'email', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order', 'is_active', 'created_at']
    list_editable = ['order', 'is_active']
    ordering = ['order']



