# Generated by Django 3.0.6 on 2020-11-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_votes_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='deviceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('mobile_name', models.CharField(max_length=250)),
                ('specifications', models.CharField(max_length=1500)),
                ('image_link', models.CharField(max_length=1000)),
            ],
        ),
    ]