# Generated by Django 4.1.4 on 2024-04-17 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userinvitation'),
        ('executor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayBookExecution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_run_id', models.CharField(max_length=255)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'UNKNOWN_STATUS'), (1, 'CREATED'), (2, 'RUNNING'), (3, 'FINISHED'), (4, 'FAILED')], default=1, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('started_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('finished_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
            ],
            options={
                'unique_together': {('account', 'playbook_run_id')},
            },
        ),
        migrations.CreateModel(
            name='PlayBookExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playbook_task_result', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbook')),
                ('playbook_execution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookexecution')),
                ('playbook_step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbookstep')),
                ('playbook_task_definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='executor.playbooktaskdefinition')),
            ],
        ),
    ]
