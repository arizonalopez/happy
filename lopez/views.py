from django.shortcuts import render, get_object_or_404
from rest_framework import generics

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
import datetime
from .models import Bulletin, ViralVideo
from .serializer import BulletinSerializer
from django.conf import settings

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'lopez/datetime.html', {'now': now})

class RESTBulletinList(generics.ListCreateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer

class RESTBulletinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer

POPULAR_FROM = getattr(settings, 'VIRAL_VIDEOS_POPULAR_FROM', 500)

def viral_video_detail(request, id):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    qs = ViralVideo.objects.annotate(
        total_impressions=\
            models.F('desktop_impressions') + models.F('mobile_impressions'),
            label=models.Case(
                models.When(total_impressions__gt=POPULAR_FROM, then=models.Value('popular')
            ), models.When(created__gt=yesterday, then=models.Value('new'),
            default=models.Value('cool'), output_field=models.CharField()
            )
    ))
    #print(qs.query)
    qs = qs.filter(pk=id)
    if request.flavour == 'mobile':
        qs.update(
            mobile_impressions=models.F('mobile_impressions') + 1
        )
    else:
        qs.update(
            desktop_impressions=models.F('desktop_impressions') + 1
        )
    video = get_object_or_404(qs)
    return render(
        request, 'lopez/viral_video.html', {'video': video}
    )

def register(request):
    if request.POST:
        form = Register(request.POST)
        if form.is_valid:
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            form.save()
        else:
            return render(request, 'lopez/datetime.html', {'form': form}) 
    else:
        form = Register()
        return render(request, 'lopez/datetime.html', {'form': form})
    


  
