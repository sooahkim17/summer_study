# Generated by Django 2.2.3 on 2019-07-17 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_contents',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.Board'),
        ),
    ]