# Generated by Django 3.1.5 on 2021-01-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_list_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
