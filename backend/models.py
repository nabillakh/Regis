from django.db import models


# Modèle de tâche
class Task(models.Model):
    title = models.CharField(max_length=200)  # Titre de la tâche
    description = models.TextField()  # Description de la tâche
    completed = models.BooleanField(default=False)  # Statut de la tâche

    def __str__(self):
        return self.title  # Représentation textuelle de la tâche