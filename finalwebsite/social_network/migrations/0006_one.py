# Generated by Django 4.0.2 on 2022-03-05 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0005_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social_network.user')),
            ],
        ),
    ]
