# Generated by Django 5.0.4 on 2024-05-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hw2app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img_file",
            field=models.ImageField(blank=True, null=True, upload_to="media/products/"),
        ),
    ]