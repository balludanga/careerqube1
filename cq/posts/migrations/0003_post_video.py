# Generated by Django 3.0.5 on 2020-05-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
