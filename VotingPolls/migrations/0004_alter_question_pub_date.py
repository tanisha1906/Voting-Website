# Generated by Django 4.1 on 2024-04-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VotingPolls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
