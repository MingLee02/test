# Generated by Django 3.2 on 2022-02-02 18:14

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=128, populate_from=['name'])),
                ('category_type', models.CharField(choices=[('D', 'Department'), ('I', 'Item')], default='I', max_length=1, verbose_name='Type')),
            ],
            options={
                'unique_together': {('name', 'category_type')},
            },
        ),
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=128, populate_from=['description'])),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.category')),
            ],
        ),
    ]
