# Generated by Django 4.2.6 on 2023-10-20 07:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_posts", "0006_remove_post_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.RenameField(
            model_name="post",
            old_name="categories",
            new_name="category",
        ),
    ]