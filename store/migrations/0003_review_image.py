# Generated by Django 4.0.1 on 2022-01-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_user_review_author_rename_content_review_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]