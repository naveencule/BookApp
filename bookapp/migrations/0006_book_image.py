# Generated by Django 5.0.3 on 2024-08-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=1234, upload_to='book_media'),
            preserve_default=False,
        ),
    ]
