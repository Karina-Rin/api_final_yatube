# Generated by Django 3.2.16 on 2022-11-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20221127_1949'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
