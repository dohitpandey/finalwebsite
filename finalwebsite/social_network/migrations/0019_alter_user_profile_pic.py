# Generated by Django 4.0.2 on 2022-03-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0018_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='dp.png', max_length=250, upload_to='picture/'),
        ),
    ]