from django.contrib import admin
from django.urls import path,include
from great.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='Home'),
    path('store/',include('store.urls'))
    

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
