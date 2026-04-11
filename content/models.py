from django.db import models
from pathlib import Path
from pypdf import PdfReader
from langdetect import detect


class HeroContent(models.Model):
    welcome_text = models.CharField(max_length=200, default='Welcome to')
    dept_name = models.CharField(max_length=300, default='Department of Computer Science & Engineering')
    institute_name = models.CharField(max_length=300, default='Kamla Nehru Institute of Technology, Sultanpur')
    tagline = models.TextField(default='Striving for excellence in technical education, research, and innovation since 1962.')
    logo = models.ImageField(upload_to='hero/', blank=True, null=True)

    class Meta:
        verbose_name = 'Hero Content'

    def __str__(self):
        return 'Hero Section'

    def save(self, *args, **kwargs):
        # Enforce singleton — only one hero content
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Highlight(models.Model):
    text = models.CharField(max_length=500)
    href = models.URLField(blank=True, default='/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.text[:60]


class Faculty(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'CSE'),
        ('MCA', 'MCA'),
    ]
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default='CSE')
    photo = models.ImageField(upload_to='faculty/photos/', blank=True, null=True)
    cv = models.FileField(upload_to='faculty/cvs/', blank=True, null=True)
    profile_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Faculty'

    def __str__(self):
        return f'{self.name} ({self.department})'


class Alumni(models.Model):
    name = models.CharField(max_length=200)
    batch = models.CharField(max_length=20, help_text='e.g. 2019')
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='alumni/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-batch', 'name']
        verbose_name_plural = 'Alumni'

    def __str__(self):
        return f'{self.name} (Batch {self.batch})'


class GalleryEvent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, default='KNIT Campus')
    cover_photo = models.ImageField(upload_to='gallery/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class GalleryPhoto(models.Model):
    event = models.ForeignKey(GalleryEvent, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/photos/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'uploaded_at']

    def __str__(self):
        return f'{self.event.name} — photo {self.pk}'


class FeaturedItem(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='featured/', blank=True, null=True)
    file_size = models.CharField(max_length=30, blank=True, default='')
    language = models.CharField(max_length=30, blank=True, default='English')
    date = models.CharField(max_length=20, blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title[:80]
        
    def save(self, *args, **kwargs):
        if self.image:
            try:
                size_bytes = self.image.size
                if size_bytes < 1024 * 1024:
                    self.file_size = f"{int(size_bytes / 1024)} KB"
                else:
                    self.file_size = f"{round(size_bytes / (1024 * 1024), 2)} MB"
            except Exception as e:
                print(f"Error auto-detecting featured image size: {e}")
                
        super().save(*args, **kwargs)


class QuickLink(models.Model):
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=500, default='/')
    icon = models.ImageField(upload_to='quicklinks/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Course(models.Model):
    name = models.CharField(max_length=300)
    degree = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    intake = models.CharField(max_length=100)
    curriculum = models.TextField(blank=True)
    fees = models.CharField(max_length=200, blank=True, default='As per government norms')
    # JSON arrays stored as text
    eligibility = models.JSONField(default=list)
    highlights = models.JSONField(default=list)
    career_prospects = models.JSONField(default=list)
    brochure = models.FileField(upload_to='courses/brochures/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.name} ({self.degree})'


class Circular(models.Model):
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=30, blank=True, default='')
    file_size = models.CharField(max_length=30, blank=True, default='')
    language = models.CharField(max_length=30, default='English')
    file = models.FileField(upload_to='circulars/', blank=True, null=True)
    link = models.URLField(blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title[:80]
        
    def save(self, *args, **kwargs):
        # Auto-calculate file size and language if file is present
        if self.file:
            try:
                # Set file size
                size_bytes = self.file.size
                if size_bytes < 1024 * 1024:
                    self.file_size = f"{int(size_bytes / 1024)} KB"
                else:
                    self.file_size = f"{round(size_bytes / (1024 * 1024), 2)} MB"
                    
                # Try to detect language for PDF files
                if self.file.name and self.file.name.lower().endswith('.pdf'):
                    # Save first to ensure the file exists on disk if it's new
                    is_new = self.pk is None
                    if is_new:
                        super().save(*args, **kwargs)
                        
                    reader = PdfReader(self.file.path)
                    if len(reader.pages) > 0:
                        text = reader.pages[0].extract_text()
                        if text and text.strip():
                            lang_code = detect(text)
                            if lang_code == 'hi':
                                self.language = 'Hindi'
                            elif lang_code == 'en':
                                self.language = 'English'
                            # Fallback behavior is handled by not modifying the field
            except Exception as e:
                print(f"Error auto-detecting file metadata: {e}")
                
        super().save(*args, **kwargs)


class Notice(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, default='')
    date = models.CharField(max_length=30, blank=True, default='')
    file = models.FileField(upload_to='notices/', blank=True, null=True)
    link = models.URLField(blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title[:80]


class AboutDepartment(models.Model):
    intro_text_1 = models.TextField(blank=True, default="The Department of Computer Science & Engineering was established in 2010 with an intake of 60 students. The department has highly qualified, committed and well experienced faculty members with varied specializations. The faculties are involved in organizing and participating in several seminars, conferences and workshops. They have also published research papers in various national and international journals, presented papers in conferences in India. Over the years, the department has become a center of excellence, providing in-depth technical knowledge and opportunities for innovation and research, with well-equipped computer facilities.")
    intro_text_2 = models.TextField(blank=True, default="Computer Science & Engineering Department is the first point of contact for the campus community by supporting telephone, computing, networking, and applications. CSE Department is dedicated to facilitate and enhance teaching, learning, and administrative services and to increase the productivity and efficiency using information technology resources.")
    objective = models.TextField(blank=True, default="To be center of excellence in technical higher education, research, and support services, capable of making significant contribution to individual and societal empowerment.")
    vision = models.TextField(blank=True, default="To be centre of excellence in the computer science & engineering which will produce globally competent engineers with the moral values and technical skills for the betterment of the society.")
    mission = models.TextField(blank=True, default="• To groom our students with the quality of leadership and communication skills by working on real life projects.\n• To create an environment for engineering knowledge and innovative research.")

    class Meta:
        verbose_name = 'About Department'

    def __str__(self):
        return 'About Department Section'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class AboutSidebarLink(models.Model):
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=500, default='/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=100, default='CSE')
    photo = models.ImageField(upload_to='staff/photos/', blank=True, null=True)
    profile_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Staff'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    enrollment_no = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')
    batch = models.CharField(max_length=50, help_text='e.g. 2021-2025')
    linkedin = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-course', '-batch', 'name']
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'{self.name} ({self.enrollment_no})'


class StudentListPdf(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='student_lists')
    session_year = models.CharField(max_length=20, help_text='e.g., 2024-2025')
    year_of_study = models.CharField(max_length=20, help_text='e.g., 1st Year')
    file = models.FileField(upload_to='student_lists/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-session_year', 'year_of_study']
        verbose_name_plural = 'Student List PDFs'

    def __str__(self):
        return f'{self.course.name} - {self.session_year} ({self.year_of_study})'


class CourseTimetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='timetables')
    year = models.CharField(max_length=20, help_text='e.g., Year 1')
    file = models.FileField(upload_to='courses/timetables/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course', 'year']
        verbose_name_plural = 'Course Timetables'

    def __str__(self):
        return f'{self.course.name} - {self.year} Timetable'


class CourseSyllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='syllabuses')
    year = models.CharField(max_length=20, help_text='e.g., Year 1')
    file = models.FileField(upload_to='courses/syllabuses/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course', 'year']
        verbose_name_plural = 'Course Syllabuses'

    def __str__(self):
        return f'{self.course.name} - {self.year} Syllabus'


class ContactInfo(models.Model):
    page_title = models.CharField(max_length=200, default='Contact Us')
    page_subtitle = models.TextField(default="We're here to help and answer any questions you might have about the Computer Science & Engineering department.")
    address_line_1 = models.CharField(max_length=300, default='Kamla Nehru Institute of Technology,')
    address_line_2 = models.CharField(max_length=300, default='Sultanpur, Uttar Pradesh - 228118,')
    address_line_3 = models.CharField(max_length=300, default='India')
    phone = models.CharField(max_length=100, default='+91-5362-240454')
    email = models.CharField(max_length=200, default='cse@knit.ac.in')
    map_embed_url = models.URLField(max_length=1000, default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14309.832717983633!2d82.07223635541991!3d26.2792611!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399a7c86d691219f%3A0x99a3eb1e7c07f78f!2sKamla%20Nehru%20Institute%20of%20Technology%2C%20Sultanpur%20(U.P.)!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus')

    class Meta:
        verbose_name = 'Contact Info'

    def __str__(self):
        return 'Contact Info'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class DirectoryEntry(models.Model):
    designation = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    mobile = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=200, blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name_plural = 'Directory Entries'

    def __str__(self):
        return f'{self.designation} — {self.name}'


class HeroBanner(models.Model):
    image = models.ImageField(upload_to='hero/banners/')
    caption = models.CharField(max_length=300, blank=True, default='')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name_plural = 'Hero Banners'

    def __str__(self):
        return self.caption or f'Banner #{self.pk}'

