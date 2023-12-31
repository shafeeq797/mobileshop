"""
URL configuration for mobileshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('create/',views.create),
    path('login/',views.login),
    path('user/',views.user),
    path('createacc/',views.createacc),
    path('addseller/',views.addseller),
    path('addstaff/',views.addstaff),
    path('login1/',views.login1),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    path('addseller1/',views.addseller1),
    path('viewseller/',views.viewseller1),
    path('removeseller/<int:id>',views.removeseller1),
    path('updateseller/',views.updateseller),
    path('updateseller1/<int:id>',views.updateseller2),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

