from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth import logout
from backend.models import Task
from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
import json
import logging

logger = logging.getLogger(__name__)

# Récupérer toutes les tâches
def get_tasks(request):
    tasks = Task.objects.all()
    tasks_json = serializers.serialize('json', tasks)
    return JsonResponse(tasks_json, safe=False)

# Créer une nouvelle tâche
@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_task = Task(title=data['title'], description=data['description'])
        new_task.save()
        return JsonResponse({'message': 'Task created successfully'}, status=201)

# Mettre à jour une tâche existante
@csrf_exempt
def update_task(request, task_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        task = get_object_or_404(Task, pk=task_id)
        task.title = data.get('title', task.title)
        task.description = data.get('description', task.description)
        task.save()
        return JsonResponse({'message': 'Task updated successfully'})

# Supprimer une tâche
@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})

# Inscription d'un utilisateur (API)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Données reçues du formulaire:", data)
            username = data.get('username')
            email = data.get('email')
            password1 = data.get('password1')
            password2 = data.get('password2')

            # Vérifiez que les mots de passe correspondent
            if password1 != password2:
                return JsonResponse({"error": "Les mots de passe ne correspondent pas"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Le nom d'utilisateur existe déjà"}, status=400)

            # Créez l'utilisateur
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return JsonResponse({"message": "Utilisateur créé avec succès"}, status=201)
        except Exception as e:
            print("Erreur lors de la réception des données:", e)
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Méthode de requête non valide"}, status=405)


# GET request for the signup page (to display the form)
def signup_page(request):
    form = SignupForm()  # Assuming you have a SignupForm defined
    return render(request, 'signup.html', {'form': form})

# Connexion d'un utilisateur
@csrf_exempt
def login_view(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)

    return render(request, 'login.html')

# Page d'accueil après connexion
@login_required
def welcome_view(request):
    return render(request, 'welcome.html', {'username': request.user.username})

# Bienvenue après l'inscription
@login_required
def welcome(request):
    return render(request, 'welcome.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
