# Generated by Django 4.2.1 on 2023-10-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_alter_userprofile_auth_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_level',
            field=models.CharField(choices=[('viewer', 'Viewer'), ('member', 'Member'), ('admin', 'Admin'), ('manager', 'Manager')], max_length=10, null=True),
        ),
    ]
