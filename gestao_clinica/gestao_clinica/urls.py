from django.contrib import admin
from django.urls import path, include
from gerenciar import views  # Importa as views do app 'gerenciar'

urlpatterns = [
    path('login/', views.login_paciente, name='login_paciente'),
    path('admin/', admin.site.urls),
    path('gerenciar/', include('gerenciar.urls')),  
    path('', views.login_paciente, name='login.html'), 
]


