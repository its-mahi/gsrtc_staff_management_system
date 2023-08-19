from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsrtc_app', '0003_auto_20200627_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
