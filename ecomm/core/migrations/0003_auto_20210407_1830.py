# Generated by Django 3.1.7 on 2021-04-07 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='mobile',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='core.phonemodel'),
        ),
    ]