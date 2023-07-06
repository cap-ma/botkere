from django.shortcuts import render
from .forms import OrderForm
import requests


# Create your views here.
def home(request):
    if request.method == "POST":
        print("hellllllo")
        order_form = OrderForm(data=request.POST)

        if order_form.is_valid():
            val1 = request.POST.get("phone_number")
            val2 = request.POST.get("comment")

            send_to_telegram({"phone_num": val1, "comment": val2})
            order_form = OrderForm()

    else:
        order_form = OrderForm()
    return render(request, "index.html", {"order_form": order_form})


def send_to_telegram(message):
    apiToken = "5912956702:AAGB0agcGgcV1xsOcTGyZ9_RCFnPtDy894Y"
    chatID = "-928593511"
    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage"

    try:
        response = requests.post(apiURL, json={"chat_id": chatID, "text": message})
        print(response.text)
    except Exception as e:
        print(e)
