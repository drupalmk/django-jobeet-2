from django.utils import unittest
from jobs.models import Jobs, Categories
import datetime


class JobeetTestCase(unittest.TestCase):
    def setUp(self):
        from autofixture import AutoFixture
        programming = Categories.objects.get_by_slug('programming')
        jobs_fx = AutoFixture(Jobs, field_values={'is_activated':True, 'category':programming})
        
        jobs = jobs_fx.create(15)
        
        for j in jobs:
            j.save()
        

class JobsTestCase(unittest.TestCase):
    
    def setUp(self):
        programming = Categories.objects.get(name='Programming')
        self.acme = Jobs.objects.create(
            category=programming,
            company='Acme Inc',
            url='http://www.acme.com',
            position='Web Designer',
            location='Warsaw, Poland',
            description='Some description',
            how_to_apply='Send resume to jobs@acme.com',
            email='jobs@acme.com',
            is_public=True,
            is_activated=True,
        )

    def test_job_expiration_date_is_30_days_from_creation_date(self):
        self.acme.save()
        from jobeet import settings
        self.assertEqual(self.acme.created_at + datetime.timedelta(settings.JOB_EXPIRATION_DAY), self.acme.expires_at)

    def test_set_updated_datetime(self):
        self.acme.save()
        self.acme.company = 'New Company'
        now = datetime.datetime.now()
        self.acme.save()
        now = now.replace(microsecond=0);
        self.acme.updated_at = self.acme.updated_at.replace(microsecond=0)
        self.assertEqual(self.acme.updated_at.isoformat(), now.isoformat())
      
      

    def tearDown(self):
        self.acme.delete()
        
        
class CategoryTestCase(unittest.TestCase):

    def test_get_with_jobs(self):
    
        categories = Categories.objects.get_with_jobs()
        self.assertEqual(2, len(categories))