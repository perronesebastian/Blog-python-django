# Generated by Django 4.0 on 2021-12-21 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0011_alter_post_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
