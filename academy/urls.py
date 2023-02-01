from django.contrib import admin
from django.urls import path, include
from academy.views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('providers/',include('providers.urls')),
    path('orders/', include('orders.urls')),
    path('supplies/',include('supplies.urls')),
    path('users/',include('users.urls')),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
