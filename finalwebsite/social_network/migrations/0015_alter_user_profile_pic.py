# Generated by Django 4.0.2 on 2022-03-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0014_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(default='picture/dp.png', max_length=250, upload_to='picture/'),
        ),
    ]
