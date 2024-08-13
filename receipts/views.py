from django.shortcuts import render
from receipts.models import Receipt


def Home(request):
    receipts = Receipt.objects.all()
    context = {
        "receipts_object": receipts
    }
    return render(request, "receipts/ReceiptList.html", context)
