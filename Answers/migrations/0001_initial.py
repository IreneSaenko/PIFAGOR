# Generated by Django 2.1.7 on 2019-04-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=30)),
                ('email', models.TextField()),
            ],
        ),
    ]
