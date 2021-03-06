# Generated by Django 4.0 on 2022-06-27 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='任务名')),
                ('start_time', models.IntegerField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.IntegerField(blank=True, null=True, verbose_name='结束时间')),
                ('username', models.CharField(max_length=100, verbose_name='执行者')),
                ('status', models.CharField(choices=[('waiting', '等待中'), ('running', '执行中'), ('finished', '完成'), ('interrupt', '中断')], max_length=100, verbose_name='状态')),
                ('params', models.TextField(blank=True, null=True, verbose_name='参数')),
                ('error', models.TextField(blank=True, null=True, verbose_name='错误信息')),
                ('confirm', models.BooleanField(default=False, verbose_name='结果确认')),
                ('serial', models.CharField(default='', max_length=20, verbose_name='串行标识')),
                ('package_src', models.CharField(blank=True, max_length=100, null=True, verbose_name='包路径')),
                ('function_name', models.CharField(max_length=100, verbose_name='函数名')),
            ],
            options={
                'ordering': ('-start_time',),
            },
        ),
        migrations.CreateModel(
            name='JobCmd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmd', models.TextField(verbose_name='命令')),
                ('run_type', models.CharField(choices=[('local', '本地'), ('salt_sync', 'salt同步'), ('salt_async', 'salt异步')], max_length=20, verbose_name='运行类型')),
                ('start_time', models.IntegerField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.IntegerField(blank=True, null=True, verbose_name='结束时间')),
                ('jid', models.IntegerField(blank=True, null=True, verbose_name='jid')),
                ('status', models.CharField(choices=[('waiting', '等待中'), ('running', '执行中'), ('success', '完成'), ('failed', '失败')], max_length=20, verbose_name='状态')),
                ('error', models.TextField(blank=True, null=True, verbose_name='错误信息')),
                ('out', models.TextField(blank=True, null=True, verbose_name='输出信息')),
                ('job_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmds', to='job_manager.jobtask', verbose_name='任务')),
            ],
        ),
    ]
