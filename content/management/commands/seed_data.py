from django.core.management.base import BaseCommand
from content.models import HeroContent, Highlight, Faculty, Alumni


class Command(BaseCommand):
    help = 'Seeds the database with initial data from the static frontend data.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Hero Content
        HeroContent.objects.update_or_create(
            pk=1,
            defaults={
                'welcome_text': 'Welcome to',
                'dept_name': 'Department of Computer Science & Engineering',
                'institute_name': 'Kamla Nehru Institute of Technology, Sultanpur',
                'tagline': 'Striving for excellence in technical education, research, and innovation since 1962.',
            }
        )
        self.stdout.write(self.style.SUCCESS('  [OK] Hero content seeded'))

        # Highlights
        if not Highlight.objects.exists():
            highlights = [
                {'text': 'Notice List of Eligible Students for tablet distribution scheduled on 31-October-2025 at 10 AM', 'href': '/', 'order': 1},
                {'text': 'Online Fee Payment', 'href': '/', 'order': 2},
                {'text': 'Academic Calendar for the Odd Semester 2025-26', 'href': '/', 'order': 3},
                {'text': 'Admissions Open 2025', 'href': 'https://knit.ac.in/admissions', 'order': 4},
                {'text': 'Tech Fest Registration Live!', 'href': 'https://knit.ac.in/techfest', 'order': 5},
            ]
            for h in highlights:
                Highlight.objects.create(**h)
            self.stdout.write(self.style.SUCCESS('  [OK] {} highlights seeded'.format(len(highlights))))
        else:
            self.stdout.write('  - Highlights already exist, skipping')

        # Alumni
        if not Alumni.objects.exists():
            alumni_data = [
                {'name': 'Amit Kumar', 'batch': '2018-2022', 'company': 'Google', 'designation': 'Software Engineer', 'linkedin': 'https://linkedin.com/in/amitkumar'},
            ]
            for a in alumni_data:
                Alumni.objects.create(**a)
            self.stdout.write(self.style.SUCCESS('  [OK] {} alumni seeded'.format(len(alumni_data))))
        else:
            self.stdout.write('  - Alumni already exist, skipping')

        # Faculty (placeholder)
        if not Faculty.objects.exists():
            faculty_data = [
                {'name': 'Dr. Example Faculty', 'designation': 'Professor & HOD', 'department': 'CSE', 'order': 1},
            ]
            for f in faculty_data:
                Faculty.objects.create(**f)
            self.stdout.write(self.style.SUCCESS('  [OK] {} faculty seeded (placeholder - update via admin or API)'.format(len(faculty_data))))
        else:
            self.stdout.write('  - Faculty already exist, skipping')

        self.stdout.write(self.style.SUCCESS('\nSeeding complete! Run: python manage.py createsuperuser'))
