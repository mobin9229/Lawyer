# Generated by Django 5.1.1 on 2024-09-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_lawyer"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageTitle",
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
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]