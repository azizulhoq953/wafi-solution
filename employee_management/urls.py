from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from employee_management import settings

urlpatterns = [
   path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')), 
    path('', RedirectView.as_view(url='/employees/', permanent=True)),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
