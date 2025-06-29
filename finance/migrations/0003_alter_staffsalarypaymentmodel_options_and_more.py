# Generated by Django 5.0 on 2025-06-15 17:09

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_initial'),
        ('human_resource', '0002_alter_staffmodel_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffsalarypaymentmodel',
            options={'ordering': ['-month']},
        ),
        migrations.AlterModelOptions(
            name='staffsalarysummarymodel',
            options={'ordering': ['-month']},
        ),
        migrations.AlterUniqueTogether(
            name='staffsalarypaymentmodel',
            unique_together={('staff', 'month')},
        ),
        migrations.AlterUniqueTogether(
            name='staffsalarysummarymodel',
            unique_together={('month',)},
        ),
        migrations.AddField(
            model_name='staffsalarypaymentmodel',
            name='target_bonus',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expensemodel',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='finance.expensetypemodel'),
        ),
        migrations.AlterField(
            model_name='staffbonusmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bonuses_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffbonusmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonuses', to='human_resource.staffmodel'),
        ),
        migrations.AlterField(
            model_name='staffdeductionmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deductions_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffdeductionmodel',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deductions', to='human_resource.staffmodel'),
        ),
        migrations.AlterField(
            model_name='staffsalarymodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_profiles_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffsalarymodel',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='staffsalarymodel',
            name='staff',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salary_profile', to='human_resource.staffmodel'),
        ),
        migrations.AlterField(
            model_name='staffsalarypaymentmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_payments_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffsalarypaymentmodel',
            name='month',
            field=models.DateField(help_text='Use the first day of the month to represent the salary month'),
        ),
        migrations.AlterField(
            model_name='staffsalarysummarymodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salary_summaries_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='staffsalarysummarymodel',
            name='month',
            field=models.DateField(help_text='Use the first day of the month for reference, e.g., 2025-06-01'),
        ),
        migrations.AlterField(
            model_name='staffsalarysummarymodel',
            name='total_staff',
            field=models.PositiveIntegerField(),
        ),
        migrations.RemoveField(
            model_name='staffsalarypaymentmodel',
            name='year',
        ),
        migrations.RemoveField(
            model_name='staffsalarysummarymodel',
            name='year',
        ),
    ]
