from django.db import models
#from django_extensions.db.fields import UUIDField
from django.core.urlresolvers import reverse
# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=200)
    entry = models.TextField()
    visible = models.BooleanField()
    pub_date = models.DateTimeField('Date published')

    class Meta:
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry-detail', kwargs={'pk': self.pk})

class File(models.Model):
    IMAGE = 1
    VIDEO = 2
    ARCHIVE = 3
    FILE = 4
    FILE_TYPE_CHOICES = (
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
        (ARCHIVE, 'Archive'),
        (FILE, 'File'),
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    type = models.IntegerField(choices=FILE_TYPE_CHOICES, default=FILE)
    file = models.FileField(upload_to="blogalog/")

    def __unicode__(self):
        return self.title


