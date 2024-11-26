# Generated by Django 5.0.7 on 2024-08-01 05:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_remove_historique_annee_facturation_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=20)),
                ('nom_prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('sit_fam', models.CharField(max_length=100)),
                ('date_embauche', models.DateField()),
                ('nombre_enf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=100)),
                ('numero_demande', models.CharField(max_length=100)),
                ('agence', models.CharField(max_length=100)),
                ('nom_etablissement_hoteliers', models.CharField(max_length=100)),
                ('hotel_club_residence', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('nom_agent', models.CharField(max_length=100)),
                ('prenom_agent', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=20)),
                ('cat_prof', models.CharField(max_length=100)),
                ('date_demande', models.DateField()),
                ('date_debut_sejour', models.DateField()),
                ('date_fin_sejour', models.DateField()),
                ('nombre_total_enfants', models.IntegerField()),
                ('nombre_accompagnateurs', models.IntegerField()),
                ('nombre_enfants_chambre_parents', models.IntegerField()),
                ('total_membres_famille', models.IntegerField()),
                ('nombre_nuites', models.IntegerField()),
                ('nombre_chambre_double', models.IntegerField()),
                ('nombre_chambre_single', models.IntegerField()),
                ('type_vue', models.CharField(max_length=100)),
                ('formule', models.CharField(max_length=100)),
                ('montant_factures', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quote_part', models.DecimalField(decimal_places=2, max_digits=10)),
                ('annee_facturation', models.IntegerField()),
                ('mois_facturation', models.IntegerField()),
                ('statut', models.CharField(max_length=100)),
                ('date_statut', models.DateField()),
                ('date_demande_voucher', models.DateField()),
                ('date_envoi_voucher', models.DateField()),
                ('nature_periode', models.CharField(max_length=100)),
                ('saison', models.CharField(max_length=100)),
                ('reference_paiement', models.CharField(max_length=100)),
                ('nbr_etoiles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=100)),
                ('type_vue', models.CharField(max_length=100)),
                ('date_debut_sejour', models.DateField()),
                ('date_fin_sejour', models.DateField()),
                ('quota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
