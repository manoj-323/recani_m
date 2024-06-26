# Generated by Django 5.0.6 on 2024-06-16 10:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authz", "0007_adminchoices"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Saved_anime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saved_at", models.DateTimeField(auto_now_add=True)),
                (
                    "anime",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authz.generaldata",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "anime")},
            },
        ),
    ]
