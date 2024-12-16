# Generated by Django 5.1.4 on 2024-12-16 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascenseur',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ascenseurs', to='gestion.client'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='statut',
            field=models.CharField(choices=[('En cours', 'En cours'), ('Terminé', 'Terminé')], max_length=50),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='type_intervention',
            field=models.CharField(choices=[('Entretien', 'Entretien'), ('Réparation', 'Réparation'), ('Diagnostic', 'Diagnostic')], max_length=15),
        ),
    ]