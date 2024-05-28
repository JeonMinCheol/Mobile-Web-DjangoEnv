from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]

urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
<<<<<<< HEAD
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 42ad12243e352767096b05e95ad728fe40a51acb
