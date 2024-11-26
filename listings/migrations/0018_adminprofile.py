# Generated by Django 5.1.3 on 2024-11-26 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_dataset_alter_course_approval_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]