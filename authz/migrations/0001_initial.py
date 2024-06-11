# Generated by Django 5.0.6 on 2024-06-11 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Demographic', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Genre', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Rating', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Source', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Studio', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown Type', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_english', models.CharField(max_length=255)),
                ('score', models.FloatField()),
                ('ranked', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('members', models.IntegerField()),
                ('synopsis', models.TextField()),
                ('total_episodes', models.FloatField()),
                ('premiered', models.CharField(max_length=100)),
                ('duration_per_ep', models.CharField(max_length=100)),
                ('scored_by', models.FloatField()),
                ('favorites', models.IntegerField()),
                ('aired', models.CharField(max_length=100)),
                ('watching', models.IntegerField()),
                ('completed', models.IntegerField()),
                ('on_hold', models.IntegerField()),
                ('dropped', models.IntegerField()),
                ('plan_to_watch', models.IntegerField()),
                ('total', models.IntegerField()),
                ('scored_10_by', models.FloatField()),
                ('scored_9_by', models.FloatField()),
                ('scored_8_by', models.FloatField()),
                ('scored_7_by', models.FloatField()),
                ('scored_6_by', models.FloatField()),
                ('scored_5_by', models.FloatField()),
                ('scored_4_by', models.FloatField()),
                ('scored_3_by', models.FloatField()),
                ('scored_2_by', models.FloatField()),
                ('scored_1_by', models.FloatField()),
                ('demographic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authz.demographic')),
                ('genre', models.ManyToManyField(related_name='animes', to='authz.genre')),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authz.rating')),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authz.source')),
                ('studio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authz.studio')),
                ('typeof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authz.typeof')),
            ],
        ),
    ]
