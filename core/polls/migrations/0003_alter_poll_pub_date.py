# Generated by Django 4.2.9 on 2024-02-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_poll_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
