"""textmining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from adjidev import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kelas/', views.kelasIndex),
    path('kelas-add', views.kelasAdd),
    path('edit-kelas/<int:id>', views.editKelas),
    path('do-edit-kelas/<int:id>', views.updateKelas),
    path('hapus-kelas/<int:id>', views.destroyKelas),

    path('abstract/', views.indexAbstract),
    path('add-abstract', views.addAbstract),
    path('edit-abstract/<int:id>', views.editAbstract),
    path('do-edit-abstract/<int:id>', views.updateAbstract),
     path('preproses/<int:id>', views.preproses),
]
