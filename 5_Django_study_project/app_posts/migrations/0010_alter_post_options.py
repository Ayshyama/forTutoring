# Generated by Django 4.2.6 on 2023-11-09 09:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app_posts", "0009_post_created_post_updated_alter_post_body"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "Post", "verbose_name_plural": "Posts"},
        ),
    ]
