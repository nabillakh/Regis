from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import get_tasks, create_task, update_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),  # Page d'accueil
    
    # Gestion des tâches
    path('api/tasks/', get_tasks, name="get_tasks"),
    path('api/tasks/create/', create_task, name="create_task"),
    path('api/tasks/update/<int:task_id>/', update_task, name='update_task'),
    path('api/tasks/delete/<int:task_id>/', delete_task, name='delete_task'),

    # Inscription et connexion
    path('signup/', views.signup_page, name='signup_page'),  # Affiche le formulaire d'inscription
    path('api/register/', views.signup, name='signup'),  # Endpoint POST pour l'inscription
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Page de bienvenue
    path('welcome/', views.welcome_view, name='welcome'),
]
