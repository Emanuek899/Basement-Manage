# Generated by Django 5.2.3 on 2025-07-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("username", models.CharField(max_length=50, unique=True)),
                ("name", models.CharField(max_length=30)),
                ("lastname", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=100, unique=True)),
                ("pass_field", models.CharField(db_column="pass", max_length=20)),
                ("position", models.TextField()),
                ("date_sign", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "users",
                "managed": True,
            },
        ),
    ]
