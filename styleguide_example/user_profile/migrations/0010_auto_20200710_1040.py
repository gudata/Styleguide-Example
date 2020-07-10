# Generated by Django 3.0.7 on 2020-07-10 10:40

from django.db import migrations
import styleguide_example.common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0009_profile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=styleguide_example.common.fields.UidField(max_length=28),
        ),
    ]