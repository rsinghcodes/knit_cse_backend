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
