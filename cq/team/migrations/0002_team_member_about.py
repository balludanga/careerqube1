# Generated by Django 3.0.5 on 2020-08-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='about',
            field=models.TextField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]