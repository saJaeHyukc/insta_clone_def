# Generated by Django 4.1.1 on 2022-10-16 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment_like_authros_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='like_authros_comments',
            new_name='like_authors_comments',
        ),
    ]
