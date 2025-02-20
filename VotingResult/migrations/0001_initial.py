# Generated by Django 4.1 on 2024-03-28 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_rules', models.TextField()),
                ('max_candidates_per_election', models.PositiveIntegerField(default=1)),
                ('min_age_to_vote', models.PositiveIntegerField(default=18)),
            ],
        ),
    ]
