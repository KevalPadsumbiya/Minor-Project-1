# Generated by Django 3.0.6 on 2020-12-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201216_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email_verified',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
