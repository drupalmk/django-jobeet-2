from django.utils import unittest
from jobs.models import Jobs, Categories
from jobeet import settings
import datetime


class JobeetTestCase(unittest.TestCase):
    multi_db = False
    
    def setUp(self):
        from autofixture import AutoFixture
        programming = Categories.objects.get_by_slug('programming')
        import datetime
        now = datetime.datetime.now()
        jobs_fx = AutoFixture(Jobs, field_values={'category':programming, 'created_at':now, 'expires_at': now + datetime.timedelta(30)})
        
        self.jobs = jobs_fx.create(15)
        
        #job = jobs_fx.create(1)
        #for j in job:
        #    j.is_activated = True
        #    print j.is_activated
        #   print j.created_at
        #    print j.expires_at
        #   print j.category
        
        
        
        
        for j in self.jobs:
            j.is_activated = True
            j.save()
            
    #def tearDown(self):
    #    for j in self.jobs:
    #       j.delete()

class JobsTestCase(JobeetTestCase):
    
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
        
    def test_jobs_are_more_than_5(self):
        jobs = Jobs.objects.all()
        self.assertTrue(len(jobs) > 5)

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
      
    def test_jobs_by_category(self):
        from jobeet import settings
        programming = Categories.objects.get_by_slug('programming')
        jobs = Jobs.objects.get_active_by_category(programming, settings.MAX_JOBS_BY_CATEGORY)
        self.assertEqual(10, len(jobs))
        self.assertEqual(10, len(jobs))

    def tearDown(self):
        self.acme.delete()
        
        
class CategoryTestCase(JobeetTestCase):

    def test_get_with_jobs(self):
        categories = Categories.objects.get_with_jobs(settings.MAX_JOBS_BY_CATEGORY)
        self.assertEqual(2, len(list(categories)))
        programming = categories[1]
        print '$$$$$'
        print programming
        programmingJobs = programming.active_jobs
        self.assertTrue(len(programmingJobs) > 0)