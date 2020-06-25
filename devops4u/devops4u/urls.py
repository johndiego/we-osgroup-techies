from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('meets/', include('meets.urls')),
    path('admin/', admin.site.urls),
]
