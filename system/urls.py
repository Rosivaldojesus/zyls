from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('cripto/', include('apps.cripto.urls'))

]