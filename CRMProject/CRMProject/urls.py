from django.contrib import admin
from django.urls import path, include
from core.views import index, about
from perfilUsuario.views import registro, logout_view
from django.contrib.auth import views

urlpatterns = [
    # path para redireccionar a las paginas de core perfilUsuario dashboard y CRMProyect
    path('', index, name="index"),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name="about"),
    path('registro/', registro, name='registro'),
    path('login/', views.LoginView.as_view(template_name="perfilUsuario/login.html"), name='login'),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
