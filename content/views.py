from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView

from .models import (
    HeroContent, Highlight, Faculty, Alumni, GalleryEvent, GalleryPhoto,
    FeaturedItem, QuickLink, Course, Circular, Notice
)
from .serializers import (
    HeroContentSerializer, HighlightSerializer,
    FacultySerializer, AlumniSerializer,
    GalleryEventSerializer, GalleryPhotoSerializer,
    FeaturedItemSerializer, QuickLinkSerializer, CourseSerializer,
    CircularSerializer, NoticeSerializer
)


class HeroContentView(APIView):
    """Singleton hero section — GET for everyone, PATCH for admins."""
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAdminUser()]

    def get(self, request):
        hero = HeroContent.load()
        serializer = HeroContentSerializer(hero, context={'request': request})
        return Response(serializer.data)

    def patch(self, request):
        hero = HeroContent.load()
        serializer = HeroContentSerializer(
            hero, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HighlightViewSet(viewsets.ModelViewSet):
    queryset = Highlight.objects.filter(is_active=True)
    serializer_class = HighlightSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class GalleryEventViewSet(viewsets.ModelViewSet):
    queryset = GalleryEvent.objects.all()
    serializer_class = GalleryEventSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class GalleryPhotoViewSet(viewsets.ModelViewSet):
    queryset = GalleryPhoto.objects.all()
    serializer_class = GalleryPhotoSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class FeaturedItemViewSet(viewsets.ModelViewSet):
    queryset = FeaturedItem.objects.all()
    serializer_class = FeaturedItemSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class QuickLinkViewSet(viewsets.ModelViewSet):
    queryset = QuickLink.objects.all()
    serializer_class = QuickLinkSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]


class CircularViewSet(viewsets.ModelViewSet):
    queryset = Circular.objects.filter(is_active=True)
    serializer_class = CircularSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.filter(is_active=True)
    serializer_class = NoticeSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context

from .models import AboutDepartment, AboutSidebarLink
from .serializers import AboutDepartmentSerializer, AboutSidebarLinkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AboutDepartmentView(APIView):
    def get_permissions(self):
        if self.request.method in ['GET']:
            return []
        return [IsAdminUser()]

    def get(self, request):
        obj = AboutDepartment.load()
        serializer = AboutDepartmentSerializer(obj)
        return Response(serializer.data)

    def put(self, request):
        obj = AboutDepartment.load()
        serializer = AboutDepartmentSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class AboutSidebarLinkViewSet(viewsets.ModelViewSet):
    queryset = AboutSidebarLink.objects.all()
    serializer_class = AboutSidebarLinkSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

from .models import Staff, Student
from .serializers import StaffSerializer, StudentSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]


from .models import StudentListPdf
from .serializers import StudentListPdfSerializer

class StudentListPdfViewSet(viewsets.ModelViewSet):
    serializer_class = StudentListPdfSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def get_queryset(self):
        queryset = StudentListPdf.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
            if self.request.method in ['GET']:
                return []
            return [IsAdminUser()]
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


from .models import CourseTimetable, CourseSyllabus
from .serializers import CourseTimetableSerializer, CourseSyllabusSerializer

class CourseTimetableViewSet(viewsets.ModelViewSet):
    serializer_class = CourseTimetableSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print("VALIDATION ERRORS:", serializer.errors)
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = CourseTimetable.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class CourseSyllabusViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSyllabusSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def get_queryset(self):
        queryset = CourseSyllabus.objects.all()
        course_id = self.request.query_params.get('course', None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

from .models import ContactInfo, DirectoryEntry
from .serializers import ContactInfoSerializer, DirectoryEntrySerializer

class ContactInfoView(APIView):
    """Singleton contact info — GET for everyone, PATCH for admins."""
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [IsAdminUser()]

    def get(self, request):
        obj = ContactInfo.load()
        serializer = ContactInfoSerializer(obj, context={'request': request})
        return Response(serializer.data)

    def patch(self, request):
        obj = ContactInfo.load()
        serializer = ContactInfoSerializer(
            obj, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectoryEntryViewSet(viewsets.ModelViewSet):
    queryset = DirectoryEntry.objects.all()
    serializer_class = DirectoryEntrySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]


from .models import HeroBanner
from .serializers import HeroBannerSerializer

class HeroBannerViewSet(viewsets.ModelViewSet):
    queryset = HeroBanner.objects.filter(is_active=True)
    serializer_class = HeroBannerSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        return [IsAdminUser()]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


