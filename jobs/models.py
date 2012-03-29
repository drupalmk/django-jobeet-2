from django.db import models

class CategoriesManager(models.Manager):
    def get_with_jobs(self, limit_per_category):
        categories = self.raw('SELECT c0_.id AS id, c0_.name AS name1, c0_.slug AS slug2 FROM categories c0_ INNER JOIN jobs j1_ ON c0_.id = j1_.category_id AND (j1_.category_id = c0_.id) GROUP BY id')
        new_categories = []
        for c in categories:
            c.active_jobs = Jobs.objects.get_active_by_category(c, limit_per_category)
            new_categories.append(c)
        return new_categories
    
    def get_by_slug(self, sl):
        return self.get(slug=sl)
        
class JobsManager(models.Manager):
    def get_active_by_category(self, cat, limit):
        import datetime
        return self.filter(category=cat, is_activated=True, expires_at__gt=datetime.datetime.now()).values('id').order_by('-expires_at')[:limit]

class Categories(models.Model):
    
    active_jobs = []
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255)
    
    objects = CategoriesManager()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        db_table = u'categories'

class Jobs(models.Model):
    
    JOB_TYPES = (
        ('fulltime', 'Full time'),
        ('parttime', 'Part time'),
        ('freelance', 'Freelance'),
    )
    
    objects = JobsManager()
   
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, null=True, blank=False)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPES)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    how_to_apply = models.CharField(max_length=4000)
    is_public = models.BooleanField()
    is_activated = models.BooleanField()
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        import datetime
        if not self.id:
            self.created_at = datetime.datetime.now()
            from jobeet import settings
            self.expires_at = self.created_at + datetime.timedelta(settings.JOB_EXPIRATION_DAY)
        else:
            self.updated_at = datetime.datetime.now()
        super(Jobs, self).save(*args, **kwargs) 
    
    def __unicode__(self):
        return self.company + 'is looking for ' + self.position
    
    class Meta:
        db_table = u'jobs'
