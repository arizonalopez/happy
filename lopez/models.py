from django.db import models
from django.urls import reverse
from django.utils import text
import re
from slugify import slugify as awesome_slugify
awesome_slugify.to_lower = True
text.slugify = awesome_slugify
#from loggen.models import CreationModificationDateMixin
#from utils.models import UrlMixin

# Create your models here.
'''class Poll(models.Model):
    poll_id = '''

class Movie(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    url = models.CharField(verbose_name='URL', max_length=255)
    release_year = models.IntegerField(verbose_name="Release Year")

TYPE_CHOICES = (
    ('searching', 'Searching'),
    ('offering', 'Offering')
)

class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200)

    def __str__(self):
        return self.title

class Bulletin(models.Model):
    bulletin_type = models.CharField(verbose_name='Type', max_length=20, choices=TYPE_CHOICES)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=255)
    description = models.TextField(verbose_name='Description', max_length=300)
    contact_person = models.CharField(verbose_name='Contact person', max_length=255)
    phone = models.CharField(verbose_name='Phone', max_length=50, blank=True)
    email = models.CharField(verbose_name='Email', max_length=254, blank=True)
    image = models.ImageField(verbose_name='Image', max_length=255, upload_to='bulletin_board/', blank=True)

    def __str__(self):
        return self.title

    def get_url_path(self):
        try:
            path = reverse(
                'bulletin_detail',
                kwargs={'pk': self.pk}
            )
        except:
           return '' 
        else:
            return path

class ViralVideo(models.Model):
    title = models.CharField(
        verbose_name='Title', max_length=200, blank=True
    )
    embed_code = models.TextField(verbose_name='Youtube embed code', blank=True)
    desktop_impressions = models.PositiveIntegerField(
        verbose_name='Desktop impression', default=0
    )
    mobile_impressions = models.PositiveIntegerField(
        verbose_name='Mobile impression', default=0
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse(
            'viral_video_detail',
            kwargs={'id': str(self.id)}
        )

    def get_thumbnail_url(self):
        if not hasattr(self, '_thumbnail_url_cached'):
            url_pattern = re.compile(
                r"src='https://www.youtube.com/embed/([^']+)'"
            )
            match = url_pattern.search(self.embed_code)
            self._thumbnail_url_cached = ''
            if match:
                video_id = match.groups()[0]
                self._thumbnail_url_cached = 'http://img.youtube.com/vi/{}/0.jpg'.format(video_id)
        return self._thumbnail_url_cached



