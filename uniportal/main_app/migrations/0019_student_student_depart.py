# Generated by Django 4.1.5 on 2023-02-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_depart',
            field=models.CharField(default=0, max_length=100),
        ),
    ]