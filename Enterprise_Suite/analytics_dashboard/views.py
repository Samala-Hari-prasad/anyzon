from django.shortcuts import render
from inventory_manager.models import Product
from task_scheduler.models import Task
from expense_tracker.models import Expense
from django.db.models import Sum

def index(request):
    data = {
        'total_products': Product.objects.count(),
        'low_stock_count': Product.objects.filter(quantity__lt=10).count(), # Simplification
        'pending_tasks': Task.objects.exclude(status='done').count(),
        'total_expenses': Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0,
    }
    return render(request, 'analytics_dashboard/index.html', {'data': data})
