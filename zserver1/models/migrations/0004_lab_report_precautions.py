# Generated by Django 3.2 on 2022-10-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_tablets_side_effects'),
    ]

    operations = [
        migrations.CreateModel(
            name='lab_report_precautions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('Level', models.CharField(blank=True, max_length=100, null=True)),
                ('Precautions', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
