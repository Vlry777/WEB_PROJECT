from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('providers/',include('providers.urls')),
    path('orders/', include('orders.urls')),
]
