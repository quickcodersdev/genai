# Generated by Django 4.1.3 on 2022-11-04 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_question_audio_src_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='audio_src_url',
            field=models.CharField(max_length=255),
        ),
    ]
