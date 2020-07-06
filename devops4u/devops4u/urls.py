from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('dsa/', include('dsa.urls')),
    path('admin/', admin.site.urls),
]
