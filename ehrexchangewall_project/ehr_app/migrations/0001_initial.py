# Generated by Django 4.2.2 on 2024-01-25 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ehr_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('file_path', models.CharField(max_length=300)),
                ('image_path', models.CharField(max_length=300)),
                ('desc', models.CharField(max_length=1000)),
                ('slug', models.CharField(default='', max_length=100)),
                ('license', models.CharField(default='', max_length=50)),
                ('downloads', models.IntegerField(default=0)),
                ('usability', models.FloatField(default=0.0)),
                ('file_type', models.CharField(max_length=300)),
                ('file_size', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]