# Generated by Django 5.0.6 on 2024-06-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadservice', '0002_uploadedfile_delete_uploadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='filepath',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
    ]
