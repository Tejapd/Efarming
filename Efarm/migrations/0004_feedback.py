

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Efarm', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
