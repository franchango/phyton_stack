# Generated by Django 2.2.4 on 2021-02-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_auto_20210222_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
