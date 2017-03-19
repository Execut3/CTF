from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from app.models import ShopUser
from shop.models import *


def index(request, **kwargs):
    message = ''
    user = request.user
    shop_user = get_object_or_404(ShopUser, user=user)
    purchased_items = PurchasedItem.objects.filter(user=user)
    print purchased_items
    items = Item.objects.all()
    print items
    if request.method == 'POST':
        item_id = request.POST.get('id', 0)
        try:
            int(item_id)
        except:
            return HttpResponse('not a valid id....')

        item = get_object_or_404(Item, pk=item_id)
        print item
        print purchased_items
        if item in [i.item for i in purchased_items]:
            message = 'You already purchased this item'
        else:
            if shop_user.budget >= item.price:
                PurchasedItem.objects.get_or_create(user=user, item=item)
                shop_user.budget -= item.price
                shop_user.save()
                message = 'You successfully purchased this item'
            else:
                message = 'You don\'t have enough money to buy this item'

    return render_to_response('shop/index.html', locals(), RequestContext(request))

