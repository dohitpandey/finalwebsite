# Generated by Django 4.0.2 on 2022-03-09 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0010_user_nameslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(default='settings.MEDIA_ROOT/picture/dp.png', max_length=250, null=True, upload_to='picture/'),
        ),
    ]
