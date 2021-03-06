# Generated by Django 4.0.1 on 2022-01-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('home_details', models.TextField(max_length=300)),
                ('about', models.TextField(max_length=500)),
                ('can_live_with_dogs', models.BooleanField(default=False)),
                ('can_live_with_cats', models.BooleanField(default=False)),
                ('can_live_with_kids', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField()),
                ('image_one', models.CharField(max_length=300)),
                ('image_two', models.CharField(blank=True, max_length=300, null=True)),
                ('image_three', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='dogs.dog')),
            ],
        ),
    ]
