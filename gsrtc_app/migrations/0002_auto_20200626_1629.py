from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsrtc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
    ]
