# Generated by Django 4.1.5 on 2023-01-10 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_demand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('key_skills', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Skills',
            },
        ),
    ]
