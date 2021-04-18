# Generated by Django 3.2 on 2021-04-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('isDone', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['deadline'],
            },
        ),
    ]
