from django.shortcuts import render, redirect, HttpResponse
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store .models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator


# Create your views here.

# def index(request):
#     prds= None
#     ctg = Category.get_all_categories()
#     catigory_id = request.GET.get('category')

#     if catigory_id:
#         prds = Product.get_all_products_by_catigory_id(catigory_id)
#     else:
#         prds = Product.get_all_products()
#     data = {}
#     data['products'] = prds
#     data['categories'] = ctg
#     return render(request, 'index.html',data)


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                         cart[product] = quantity-1

                else:
                    cart[product] = quantity+1
                    
                
            else:
                cart[product] = 1

        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
        


    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        prds= None
        
        ctg = Category.get_all_categories()
        catigory_id = request.GET.get('category')

        if catigory_id:
            prds = Product.get_all_products_by_catigory_id(catigory_id)
        else:
            prds = Product.get_all_products()
        data = {}
        data['products'] = prds
        data['categories'] = ctg
        return render(request, 'index.html',data)

        

# -----------------------------------------------------------------------------------------all about index







# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         postData = request.POST
#         first_name = postData.get('firstname')
#         last_name = postData.get('lastname')
#         phone = postData.get('phone')
#         email = postData.get('email')
#         password = postData.get('password')

#         # validation
#         value = { 'first_name': first_name, 'last_name':last_name, 'phone': phone, 'email':email}
        
#         error_messege = None

#         customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password = password)

#         if (not first_name):
#             error_messege = 'firts name required'
#         elif len(first_name)< 4:
#             error_messege = 'first name must be of 4 charector or more'
        
#         elif not last_name:
#             error_messege = 'last name required'
#         elif len(last_name)<4:
#             error_messege = 'last name must be of 4 char'

#         elif not phone:
#             error_messege = 'phone number required'
#         elif len(phone)<10:
#             error_messege = 'phone number must be of 10 char'
        
#         elif len(password)<6:
#             error_messege = 'password must be of 6 char'
        
#         elif customer.isExists():
#             error_messege = "email adress already registered"

        # # saving
        # if not error_messege:
        #     print(first_name, last_name, phone, email, password)
        #     # customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password = password)
        #     # customer.save()
        #     customer.password = make_password(customer.password)
        #     customer.register()
        #     return redirect('homepage')
        
        # else:
        #     data = {'error': error_messege, 'values': value}
        #     # return render(request, 'signup.html', {'error': error_messege})
        #     return render(request, 'signup.html', data)

# class mathod of above code(signup)------->
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = { 'first_name': first_name, 'last_name':last_name, 'phone': phone, 'email':email}
        
        error_messege = None

        customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password = password)

        if (not first_name):
            error_messege = 'firts name required'
        elif len(first_name)< 4:
            error_messege = 'first name must be of 4 charector or more'
        
        elif not last_name:
            error_messege = 'last name required'
        elif len(last_name)<4:
            error_messege = 'last name must be of 4 char'

        elif not phone:
            error_messege = 'phone number required'
        elif len(phone)<10:
            error_messege = 'phone number must be of 10 char'
        
        elif len(password)<6:
            error_messege = 'password must be of 6 char'
        
        elif customer.isExists():
            error_messege = "email adress already registered"

        # saving
        if not error_messege:
            print(first_name, last_name, phone, email, password)
            # customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password = password)
            # customer.save()
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        
        else:
            data = {'error': error_messege, 'values': value}
            # return render(request, 'signup.html', {'error': error_messege})
            return render(request, 'signup.html', data)
            #-------------------------------------------------------------------------all about singnup

        










# def login(request):
#     if request.method =='GET':
#         return render(request, 'login.html')
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_messege = None
#         if customer:
#             flag = check_password(password, customer.password )
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_messege = 'email or password is invalid'
#         else:
#             error_messege = 'email or password is invalid'
        
#         print(email, password)
#         return render(request, 'login.html' , {'error':error_messege})

# class mathod of above code(login)---->
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_messege = None
        if customer:
            flag = check_password(password, customer.password )
            if flag:
                request.session['customer'] = customer.id
               

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_messege = 'email or password is invalid'
        else:
            error_messege = 'email or password is invalid'
        
        print(email, password)
        return render(request, 'login.html' , {'error':error_messege})
        # ----------------------------------------------------------------------------------------------all about login
  




def logout(request):
    request.session.clear()
    return redirect('login')











class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html' , {'products':products})
        
    


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart,  products)

        for product in products:
            order = Order(customer=Customer(id = customer), product= product, price= product.price, adress= address, phone= phone, quantity= cart.get(str(product.id)))
            order.save()
            
        request.session['cart'] = {}



        return redirect('cart')

    



class OrderView(View):

    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_order_by_customer(customer)
        print(orders)
        
        return render(request, 'orders.html', {'orders':orders})