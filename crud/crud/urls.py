"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#Importar mainapp with my views
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('list-articles', views.articles_list, name="articles"),
    path('create-article', views.create_article, name="create_article"),
    path('clear-article/<str:id>', views.clear_article, name="clear"),
    path('update-article/<str:id>', views.update_article, name="update"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)