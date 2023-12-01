# Generated by Django 4.2.6 on 2023-11-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_email', models.CharField(max_length=100)),
                ('teacher_contact', models.BigIntegerField()),
            ],
        ),
    ]
