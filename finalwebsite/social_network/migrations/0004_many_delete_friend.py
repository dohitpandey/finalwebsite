# Generated by Django 4.0.2 on 2022-03-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0003_remove_friend_album_friend_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='many',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alum', models.ManyToManyField(to='social_network.user')),
            ],
        ),
        migrations.DeleteModel(
            name='friend',
        ),
    ]
