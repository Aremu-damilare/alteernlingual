# Generated by Django 3.2.5 on 2023-01-15 11:01

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alteernlingual_topic', '0002_topic_read_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_policy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('terms_of_service', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('misc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
            ],
        ),
    ]
