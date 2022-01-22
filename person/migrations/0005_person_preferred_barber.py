# Generated by Django 4.0.1 on 2022-01-22 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0001_initial'),
        ('person', '0004_person_nif'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='preferred_barber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barber.barber'),
        ),
    ]