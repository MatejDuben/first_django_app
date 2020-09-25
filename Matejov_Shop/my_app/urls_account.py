from django.urls import path


from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from . import views

app_name='account'

urlpatterns = [
  path('register/', views.registerPage, name='register'),
  path('login/', views.loginPage, name='login'),
  path('logout/', views.logoutUser, name='logout'),
  path('Admin/', views.admin_properties, name='admin')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)