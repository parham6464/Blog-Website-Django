# Generated by Django 4.2.10 on 2024-05-14 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]