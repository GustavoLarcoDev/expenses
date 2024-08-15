from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_object": receipts
    }
    return render(request, "receipts/ReceiptList.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            Receipt = form.save(commit=False)
            Receipt.purchaser = request.user
            Receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "form": form
    }
    return render(request, "receipts/CreateReceipt.html", context)


@login_required
def category_list(request):
    list = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "category_list": list,
    }
    return render(request, "receipts/category_list.html", context)


@login_required
def account_list(request):
    receipt = Account.objects.filter(owner=request.user)
    context = {
        "account_list": receipt,
    }
    return render(request, "receipts/account_list.html", context)
