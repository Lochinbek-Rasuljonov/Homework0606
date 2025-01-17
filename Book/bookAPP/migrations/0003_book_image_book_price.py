# Generated by Django 5.1.3 on 2024-12-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookAPP', '0002_alter_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
