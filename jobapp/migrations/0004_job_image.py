# Generated by Django 4.2.2 on 2023-06-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_remove_job_positions_job_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to='jobs/'),
        ),
    ]
