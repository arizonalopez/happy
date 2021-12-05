'''from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Bulletin, TYPE_CHOICES
from .forms import BulletinFilterForm
import requests

class BulletinFeed(Feed):
    description_template = 'lopez/bulletin_description.html'

    def get_object(self, request, *args, **kwargs):
        form = BulletinFilterForm(data=request.REQUEST)
        obj = {}
        if form.is_valid():
            obj = {
                'bulletin_type': form.cleaned_data['bulletin_type'],
                'category': form.cleaned_data['category'],
                'query_string': request.META['QUERY_STRING']
            }
        return obj

    def title(self, obj):
        t = 'My Website - Bulletin Board'
        if obj.get('bulletin_type', False):
            tp = obj['bulletin_type']
            t += ' - %s' % dict(TYPE_CHOICES)[tp]
        if obj.get('category', False):
            t += ' - %s' % obj['category'].title
        return t

    def link(self, obj):
        if obj.get('query_string', False):
            return reverse('bulletin_type') + '?' + obj['query_string']
        return reverse('bulletin_list')

    def feed_url(self, obj):
        if obj.get('query_string', False):
            return reverse('bulletin_rss') + '?' + obj['query_string']
        return reverse('bulletin_rss')


    def item_pubdate(self, item):
        return item.created

    def items(self, obj):
        qs = Bulletin.objects.order_by('-created')
        if obj.get('bulletin_type', False):
            qs = qs.filter(
                bulletin_type=obj['bulletin_type']).distinct()
        if obj.get('category', False):
            qs = qs.filter(
                category=obj['category']).distinct()

        return qs[:30]'''