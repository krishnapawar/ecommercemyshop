from django.shortcuts import render,redirect
from.models import addproduct,contact,orders,OrderUpdate
from math import ceil
import json

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def mainpage(request):
	'''allProds = []
	catprods = addproduct.objects.values('category', 'id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = addproduct.objects.filter(category=cat)
		n = len(prod)
		nSlides = n // 4 + ceil((n / 4) - (n // 4))
		allProds.append([prod, range(1, nSlides), nSlides])'''
	
	allprods = []
	catprods = addproduct.objects.values('category','id')
	cats = {item['category'] for item in catprods}
	for cat in cats:
		prod = addproduct.objects.filter(category = cat)
		n = len(prod)
		nslides = n//4+ceil((n/4)-(n//4))
		allprods.append([prod, range(1, nslides), nslides])
		params= {'allprods':allprods}


	'''products = addproduct.objects.all()
	n = len(addproduct)
	nslides = n/4+ceil((n/4)-(n//4))
	print(products)'''
	params = {'allprods':allprods}
	return render(request,'shop/index.html',params)

def productview(request,prid):
	product = addproduct.objects.filter(id = prid)
	return render(request,'shop/productview.html',{'products':product[0]})

#this is checkout form code 
def checkout(request):
	if request.method == 'POST':
		check = orders()
		check.items_json = request.POST['items_json']
		check.name = request.POST['name']
		check.address = request.POST['address1'] +','+ request.POST['address2']
		check.email = request.POST['mail']
		check.city = request.POST['city']
		check.zip_code = request.POST['zipcode']
		check.phone = request.POST['phone']
		check.save()
		update = OrderUpdate(order_id=check.order_id, update_desc="The order has been placed")
		update.save()
		thank = True
		id = check.order_id 
		return render(request,'shop/checkout.html',{'thank':thank,'id':id})
	return render(request,'shop/checkout.html')

#This is contact form's code 
def cont(request):
	if request.method == 'POST':
		p = contact()
		p.name = request.POST['name']
		p.email = request.POST['email']
		p.phone = request.POST['phone']
		p.desc = request.POST['desc']
		p.save()
		return redirect('contact')
	else:
		return render(request,'shop/contact.html')

def aboutpage(request):
	return render(request,'shop/about.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        
        try:
            order = orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success","updates":updates, "itemsJson":order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')
