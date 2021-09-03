# Generated by Django 3.2.7 on 2021-09-03 08:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('test', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock())]))], default=''),
            preserve_default=False,
        ),
    ]