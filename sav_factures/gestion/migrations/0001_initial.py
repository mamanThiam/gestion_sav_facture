# Generated by Django 5.1.4 on 2024-12-16 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('adresse', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telephone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Ascenseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modele', models.CharField(max_length=255)),
                ('marque', models.CharField(max_length=50)),
                ('numero_serie', models.CharField(max_length=255, unique=True)),
                ('charge', models.CharField(choices=[('450', '450'), ('630', '630'), ('800', '800'), ('1000', '1000'), ('1500', '1500'), ('2000', '2000')], max_length=15)),
                ('date_installation', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ascenseur', to='gestion.client')),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_services', models.TextField()),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('statut', models.CharField(choices=[('Payé', 'Payé'), ('Non payé', 'Non payé')], max_length=15)),
                ('date_emission', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='gestion.client')),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technicien', models.CharField(max_length=255)),
                ('statut', models.CharField(choices=[('En cours', 'En cours'), ('Términé', 'Términé')], max_length=50)),
                ('type_intervention', models.CharField(choices=[('Entretient', 'Entretient'), ('Réparation', 'Réparation'), ('Diagnostic', 'Diagnostic')], max_length=15)),
                ('date', models.DateField()),
                ('ascenseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interventions', to='gestion.ascenseur')),
            ],
        ),
    ]
