# Generated by Django 4.1 on 2024-03-28 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VotingContact', '0002_rename_content_contact_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='General Inquiry', max_length=100),
        ),
    ]
