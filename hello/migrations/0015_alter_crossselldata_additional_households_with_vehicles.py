# Generated by Django 4.2.4 on 2023-08-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0014_agentdata_crossselldata_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossselldata',
            name='additional_households_with_vehicles',
            field=models.CharField(max_length=20),
        ),
    ]
