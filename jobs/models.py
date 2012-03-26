from django.db import models

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, unique=True)
    slug = models.CharField(max_length=765)
    class Meta:
        db_table = u'categories'

class Jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Categories, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=765)
    company = models.CharField(max_length=765)
    logo = models.CharField(max_length=765, blank=True)
    url = models.CharField(max_length=765, blank=True)
    position = models.CharField(max_length=765, blank=True)
    location = models.CharField(max_length=765)
    description = models.CharField(max_length=12000)
    how_to_apply = models.CharField(max_length=12000)
    is_public = models.IntegerField()
    is_activated = models.IntegerField()
    email = models.CharField(max_length=765)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    class Meta:
        db_table = u'jobs'
