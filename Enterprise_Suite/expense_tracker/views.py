from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Category
from django.db.models import Sum
from datetime import datetime

@login_required
def index(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total_balance = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    categories = Category.objects.filter(user=request.user)
    
    # Monthly calc
    now = datetime.now()
    monthly_sum = expenses.filter(date__month=now.month, date__year=now.year).aggregate(Sum('amount'))['amount__sum'] or 0
    
    return render(request, 'expense_tracker/index.html', {
        'expenses': expenses,
        'total_balance': total_balance,
        'monthly_sum': monthly_sum,
        'categories': categories
    })

@login_required
def add_expense(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        Expense.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            amount=request.POST.get('amount'),
            category=category,
            date=request.POST.get('date'),
            description=request.POST.get('description')
        )
        return redirect('expense_tracker:index')
    return render(request, 'expense_tracker/add.html')
