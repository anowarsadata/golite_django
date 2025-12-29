from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # CKEditor
    path('ckeditor5/', include('django_ckeditor_5.urls')),

# Blog API
    path('api/blog/', include('apps.blog.api_urls', namespace='blog_api')),
# Products API (SAME STYLE AS BLOG)
    path('api/products/', include('apps.products.api_urls', namespace='products_api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
