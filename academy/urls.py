from django.contrib import admin
from django.urls import path, include
from academy.views import index, about_us

from academy.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about_us, name= 'about_us'),
    path('admin/', admin.site.urls),

    path('providers/',include('providers.urls')),
    path('orders/', include('orders.urls')),
    path('supplies/',include('supplies.urls')),
    path('users/',include('users.urls')),
    path('workshops/',include('workshops.urls')),


] + static(MEDIA_URL, document_root= MEDIA_ROOT)
