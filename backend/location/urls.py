"""
URL configuration for location project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import insert_poste, get_all_postes,search_location,delete_post,update_post,get_alll_postes
urlpatterns = [
    path('admin/', admin.site.urls),
        path('postes/', insert_poste, name='insert-poste'),
        path('a/', get_all_postes, name='get-all-postes'),
        path('search_location/', search_location, name='search-location'),
          path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
           path("update_post/<int:post_id>/", update_post, name="update_post"),
            path('b/', get_alll_postes, name='get-alll-postes'),
            
           
]




