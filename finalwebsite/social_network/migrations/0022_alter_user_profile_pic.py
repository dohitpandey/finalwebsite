# Generated by Django 4.0.2 on 2022-03-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0021_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(default='/dp.png/', upload_to='picture/'),
        ),
    ]
