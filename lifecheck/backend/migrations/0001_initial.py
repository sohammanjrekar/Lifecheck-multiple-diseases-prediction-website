# Generated by Django 4.1.1 on 2022-09-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("msg_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(default="", max_length=70)),
                ("phone", models.CharField(default="", max_length=70)),
                ("desc", models.CharField(default="", max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Patients",
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
                ("patient_name", models.CharField(max_length=50)),
                ("Age", models.IntegerField(default=0)),
                ("address", models.CharField(max_length=111)),
                ("city", models.CharField(max_length=111)),
                ("state", models.CharField(max_length=111)),
                ("zip_code", models.CharField(max_length=111)),
                ("phone", models.CharField(default="", max_length=111)),
                ("email", models.CharField(max_length=111)),
                ("doctor_name", models.CharField(max_length=50)),
                ("join_date", models.DateField(auto_now_add=True)),
                ("image", models.ImageField(default="", upload_to="backend/images")),
            ],
        ),
    ]
