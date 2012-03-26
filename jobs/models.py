from django.db import models

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255)
    class Meta:
        db_table = u'categories'

class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Categories, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    how_to_apply = models.CharField(max_length=4000)
    is_public = models.IntegerField()
    is_activated = models.IntegerField()
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    class Meta:
        db_table = u'jobs'
