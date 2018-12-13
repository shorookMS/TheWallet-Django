# Generated by Django 2.1 on 2018-12-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181212_0430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('label', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=120)),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='balance',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='savings',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Health', 'Health'), ('Personal', 'Personal'), ('Emergency', 'Emergency'), ('Entertainment', 'Entertainment'), ('Transportation', 'Transportation'), ('Others', 'Others')], max_length=13),
        ),
        migrations.AddField(
            model_name='goal',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='api.Profile'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='goal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='deposits', to='api.Goal'),
        ),
    ]
