# Generated by Django 4.1.7 on 2023-03-22 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_sensor_remove_measurement_project_delete_project_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'Измерение', 'verbose_name_plural': 'Измерения'},
        ),
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='updated_at',
        ),
    ]