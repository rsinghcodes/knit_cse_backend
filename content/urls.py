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

from .views import AboutDepartmentView, AboutSidebarLinkViewSet

router.register(r'about-links', AboutSidebarLinkViewSet, basename='about-link')

from .views import StaffViewSet, StudentViewSet

router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'students', StudentViewSet, basename='student')
from .views import StudentListPdfViewSet
router.register(r'student-lists', StudentListPdfViewSet, basename='student-list')
from .views import CourseTimetableViewSet, CourseSyllabusViewSet
router.register(r'course-timetables', CourseTimetableViewSet, basename='course-timetable')
router.register(r'course-syllabuses', CourseSyllabusViewSet, basename='course-syllabus')

urlpatterns = [
    path('hero/', HeroContentView.as_view(), name='hero'),
    path('about/', AboutDepartmentView.as_view(), name='about'),
    path('', include(router.urls)),
]
