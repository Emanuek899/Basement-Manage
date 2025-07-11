# Generated by Django 5.2.3 on 2025-07-02 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Token",
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
                ("key", models.CharField(max_length=64)),
                (
                    "users",
                    models.ForeignKey(
                        db_column="users",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="users.users",
                    ),
                ),
            ],
            options={
                "db_table": "token",
                "managed": True,
            },
        ),
    ]
