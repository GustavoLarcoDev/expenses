from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_object": receipts
    }
    return render(request, "receipts/ReceiptList.html", context)
