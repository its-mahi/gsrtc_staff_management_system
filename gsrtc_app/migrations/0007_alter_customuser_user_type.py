# Generated by Django 4.1.5 on 2023-04-10 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsrtc_app', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff')], default=1, max_length=10),
        ),
    ]