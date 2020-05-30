# Generated by Django 3.0.6 on 2020-05-28 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0003_auto_20200528_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurportfoliomodel',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurs.IndustryModel'),
        ),
        migrations.AlterField(
            model_name='entrepreneurportfoliomodel',
            name='investment_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrepreneurs.InvestmentPlanModel'),
        ),
    ]