from django.urls import path

from finance.views import (
    ExpenseTypeCreateView,
    ExpenseTypeListView,
    ExpenseTypeUpdateView,
    ExpenseTypeDeleteView,
    ExpenseCreateView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    StaffBonusCreateView,
    StaffBonusListView,
    StaffBonusUpdateView,
    StaffBonusDeleteView,
    StaffDeductionCreateView,
    StaffDeductionListView,
    StaffDeductionUpdateView,
    StaffDeductionDeleteView, staff_salary_profile_view, staff_salary_profile_update, salary_payment_create,
    salary_payment_view, WalletDashboardView, BankAdjustmentView, debtors_overview_view, WalletStatementView,
)

urlpatterns = [
    # ExpenseType URLs
    path('expense-type/', ExpenseTypeListView.as_view(), name='expense_type_index'),
    path('expense-type/create/', ExpenseTypeCreateView.as_view(), name='expense_type_create'),
    path('expense-type/update/<int:pk>/', ExpenseTypeUpdateView.as_view(), name='expense_type_update'),
    path('expense-type/delete/<int:pk>/', ExpenseTypeDeleteView.as_view(), name='expense_type_delete'),

    # Expense URLs
    path('expense/', ExpenseListView.as_view(), name='expense_index'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expense/update/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),

    # StaffBonus URLs
    path('staff-bonus/', StaffBonusListView.as_view(), name='staff_bonus_index'),
    path('staff-bonus/create/', StaffBonusCreateView.as_view(), name='staff_bonus_create'),
    path('staff-bonus/update/<int:pk>/', StaffBonusUpdateView.as_view(), name='staff_bonus_update'),
    path('staff-bonus/delete/<int:pk>/', StaffBonusDeleteView.as_view(), name='staff_bonus_delete'),

    # StaffDeduction URLs
    path('staff-deduction/', StaffDeductionListView.as_view(), name='staff_deduction_index'),
    path('staff-deduction/create/', StaffDeductionCreateView.as_view(), name='staff_deduction_create'),
    path('staff-deduction/update/<int:pk>/', StaffDeductionUpdateView.as_view(), name='staff_deduction_update'),
    path('staff-deduction/delete/<int:pk>/', StaffDeductionDeleteView.as_view(), name='staff_deduction_delete'),

    path('salary-profiles/', staff_salary_profile_view, name='staff_salary_profile_index'),
    path('salary-profiles/update/', staff_salary_profile_update, name='staff_salary_profile_update'),
    path('salary-payments/create/', salary_payment_create, name='salary_payment_create'),
    path('salary-payments/', salary_payment_view, name='salary_payment_view'),
    path('salary-payments/<str:month>/', salary_payment_view, name='salary_payment_view'),

    path('wallet/', WalletDashboardView.as_view(), name='wallet_dashboard'),
    path('debtors/', debtors_overview_view, name='debtor_index'),
    path('wallet/adjust/', BankAdjustmentView.as_view(), name='wallet_adjustment'),
    path('wallet-statement/', WalletStatementView.as_view(), name='wallet_statement'),


]
