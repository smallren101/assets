# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-01 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetsapp', '0013_auto_20180901_0356'),
    ]

    operations = [
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡名称')),
                ('model', models.CharField(max_length=128, verbose_name='网卡型号')),
                ('mac', models.CharField(max_length=64, verbose_name='MAC地址')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')),
                ('net_mask', models.CharField(blank=True, max_length=64, null=True, verbose_name='掩码')),
                ('bonding', models.CharField(blank=True, max_length=64, null=True, verbose_name='绑定地址')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetsapp.Asset')),
            ],
            options={
                'verbose_name': '网卡',
                'verbose_name_plural': '网卡',
                'db_table': 't_nic',
            },
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([('asset', 'model', 'mac')]),
        ),
    ]
