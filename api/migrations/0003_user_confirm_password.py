# Generated by Django 2.1.7 on 2019-03-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_confirm_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
