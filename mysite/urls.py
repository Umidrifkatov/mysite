from django.contrib import admin
from django.urls import path, include
from telegram.views import worker
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'E-CORP Admin'
admin.site.index_title = settings.COMPANY
admin.site.site_title = 'E-CORP'

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('', admin.site.urls),
    path('jet/dashboard/',  include('jet.dashboard.urls', 'jet-dashboard')),
    path(f'{settings.TOKEN}/', worker, name="bot"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
