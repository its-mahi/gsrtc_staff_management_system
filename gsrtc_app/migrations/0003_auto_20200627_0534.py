from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsrtc_app', '0002_auto_20200626_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
