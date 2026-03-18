from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HeroContentView,
    HighlightViewSet,
    FacultyViewSet,
    AlumniViewSet,
    GalleryEventViewSet,
    GalleryPhotoViewSet,
    FeaturedItemViewSet,
    QuickLinkViewSet,
    CourseViewSet,
    CircularViewSet,
    NoticeViewSet,
)

router = DefaultRouter()
router.register(r'highlights', HighlightViewSet, basename='highlight')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'alumni', AlumniViewSet, basename='alumni')
router.register(r'gallery/events', GalleryEventViewSet, basename='gallery-event')
router.register(r'gallery/photos', GalleryPhotoViewSet, basename='gallery-photo')
router.register(r'featured', FeaturedItemViewSet, basename='featured')
router.register(r'quicklinks', QuickLinkViewSet, basename='quicklink')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'circulars', CircularViewSet, basename='circular')
router.register(r'notices', NoticeViewSet, basename='notice')

urlpatterns = [
    path('hero/', HeroContentView.as_view(), name='hero'),
    path('', include(router.urls)),
]
