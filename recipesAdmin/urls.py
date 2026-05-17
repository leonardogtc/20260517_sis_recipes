from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from recipesAdmin import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
