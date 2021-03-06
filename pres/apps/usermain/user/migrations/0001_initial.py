# Generated by Django 2.1.7 on 2019-04-22 01:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollowed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(default=datetime.datetime.now)),
                ('user_followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to=settings.AUTH_USER_MODEL)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from_followed', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(max_length=32)),
                ('key', models.CharField(max_length=16)),
                ('is_banned', models.BooleanField(default=False)),
                ('has_checked_email', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserVisualization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from_visualization', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
