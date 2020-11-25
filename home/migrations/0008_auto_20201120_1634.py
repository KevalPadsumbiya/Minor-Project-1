# Generated by Django 3.0.6 on 2020-11-20 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='vote_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField()),
                ('downvote', models.IntegerField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Comments')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserData')),
            ],
        ),
    ]