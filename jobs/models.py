from django.db import models

class CategoriesManager(models.Manager):
    def get_with_jobs(self):
        return self.extra(tables=["jobs"],
                          where=["""jobs.category_id = categories.id"""])

class Categories(models.Model):
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
   
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, null=True, blank=False)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPES)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    how_to_apply = models.CharField(max_length=4000)
    is_public = models.BooleanField()
    is_activated = models.BooleanField()
    email = models.CharField(max_length=255)
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
