# Generated by Django 4.1 on 2022-08-11 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db_query", "0002_alter_person_city_alter_person_district_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="country",
            name="name",
            field=models.CharField(
                choices=[("IND", "India"), ("ENG", "England"), ("AUS", "Australia")],
                max_length=20,
            ),
        ),
    ]
