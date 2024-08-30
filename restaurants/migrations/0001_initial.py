import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('cuisines', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=8)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
