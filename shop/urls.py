from django.urls import path
from.import views
urlpatterns = [
	path('',views.mainpage,name='shop'),
	path('product/<int:prid>',views.productview, name='showproduct'),
	path('shop/checkout',views.checkout,name='checkout'),
	path('shop/contactus',views.cont,name='contact'),
	path('shop/about',views.aboutpage, name='about'),
	path('shop/tracker',views.tracker, name='tracker'),
	path("handlerequest/", views.handlerequest, name="HandleRequest"),
	path('search/',views.searchn, name='search'),
]