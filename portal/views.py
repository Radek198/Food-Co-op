
from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework.views import APIView

from portal.serializers import ProductSerializer
from .forms import AddKoopForm, SearchForm, AddSupplierForm, AddCategoryForm, AddProductForm, \
    CustomUserCreationForm, LoginForm, UpdateProfile
from .models import MyUser, Koop, Supplier, Product, Category, Order
from django.http import HttpResponse, HttpResponseRedirect


from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
import ast
import json
# Create your views here.



class StartView(View):

    def get(self, request):

        ctx = {}
        return render(request, "start.html", ctx)


class AddCustomUserView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/'

    def form_valid(self, form):

        # CustomUser.objects.create_user(**form.cleaned_data)
        MyUser.objects.create_user(
           form.cleaned_data['username'],
           password=form.cleaned_data['password1'],
           email=form.cleaned_data['email'])
        return HttpResponseRedirect('/start')


class UserListView(View):
    def get(self, request):

        myuser = MyUser.objects.order_by('username')
        return render(request, "user_list.html", {'myuser': myuser})

class UserInfoView(View):
    def get(self, request):
        myuser = request.user

        return render(request, "user_info.html", {'myuser': myuser})

    from django.contrib.auth.models import User

#    request.user
class LoginView(FormView):

    form_class = LoginForm
    template_name = 'login.html'
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return render(self.request, 'start.html', {})
        else:
            return HttpResponseRedirect('/start/')
            #return super(LoginView, self).form_valid(form)


class UserEditView(FormView):

    def get(self, request):

        form = UpdateProfile()
        return render(request, 'user_edit.html', {'form': form})


    def post(self, request):

        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_info')

        else:
            form = UpdateProfile()
            return render(request, 'user_edit.html', {'form': form})




    from django.contrib.auth import logout


class LogoutView(View):

    def get(self, request):
        print(request.user)
        print(request.user.is_authenticated)
        myuser = request.user
        order = Order.objects.filter(client=myuser)
        order.delete()
        logout(request)

        print(request.user)
        print(request.user.is_authenticated)

        return HttpResponseRedirect('/start/')




#class AddUserView(View):
#    def get(self, request):
#        form = AddUserForm()
#
#        ctx = {
#            "form": form
#        }
#        return render(request, "add_user.html", ctx)
#
#    def post(self, request):
#        form = AddUserForm(request.POST)
#        if form.is_valid():
#            nickname = form.cleaned_data['nickname']
#            email = form.cleaned_data['email']
#            password = form.cleaned_data['password']
#            kooperatywa = form.cleaned_data['kooperatywa']
#            supplier = form.cleaned_data['supplier']
#            koopadmin = form.cleaned_data['koopadmin']
#            form = AddStudentForm(request.POST)
#            newstudent = MyUser.objects.create(nickname= nickname, email=email, password = password,
#                                               kooperatywa = kooperatywa, supplier = supplier, koopadmin = koopadmin,)
#
#            id = newstudent.id
#
#            return HttpResponseRedirect('/start/')
#        else:
#            ctx = {'form': form}
#            return render(request, 'add_user.html', ctx)


class AddKoopView(View):

    def get(self, request):
        form = AddKoopForm()

        ctx = {
            "form": form
        }
        return render(request, "add_koop.html", ctx)

    def post(self, request):

        form = AddKoopForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            city = form.cleaned_data['city']

            newkopp = Koop.objects.create(name=name, email=email, city=city)


            return HttpResponseRedirect('/start/')
        else:
            ctx = {'form': form}
            return render(request, 'add_koop.html', ctx)


class EditKoopView(UpdateView):
    model = Koop
    fields = ['name', 'city', 'district', 'email', 'phone']
    template_name_suffix = '_update_form'
    success_url = ("/start")


class KoopListView(View):

    def get(self, request):
        koop = Koop.objects.order_by('name')
        form = SearchForm()
        ctx = {
            'koop': koop,
            "form": form

        }
        return render(request, "koop_list.html", ctx)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            name = Koop.objects.filter(name__icontains=search)
            city = Koop.objects.filter(city__icontains=search)
            ctx = {
                'name': name,
                'city': city
                   }

            return render(request, "koop_list.html", ctx)


class KoopInfoView(View):


     def get(self, request, id):

        koop = Koop.objects.get(id=id)
        name = koop.name
        city = koop.city
        district = koop.district
        email = koop.email
        phone = koop.phone
        id=koop.id

        ctx = {
            'id': id,
            'name': name,
            'city': city,
            'district': district,
            'email': email,
            'phone': phone
        }
        return render(request, "koop_info.html", ctx)


class SupplierAddView(View):

    def get(self, request):

        form = AddSupplierForm()

        ctx = {
            "form": form
        }
        return render(request, "supplier_add.html", ctx)

    def post(self, request):
        form = AddSupplierForm(request.POST, request.FILES)
        if form.is_valid():
            newsupplier = Supplier.objects.create(**form.cleaned_data)

            return HttpResponseRedirect('/supplier_add/')
        else:
            ctx = {
                "form": form
            }
            return render(request, "supplier_add.html", ctx)


class SupplierListView(View):

    def get(self, request):


        supplier = Supplier.objects.order_by('name')
        product = Product.objects.order_by('name')
        category = Category.objects.order_by('category_name')

        #form = SearchForm()
        ctx = {
            'supplier': supplier,
            'product': product,
            'category': category
        }
        return render(request, "supplier_list.html", ctx)


class SupplierInfoView(View):
    def get(self, request, id):
        supplier = Supplier.objects.get(id=id)
        name = supplier.name
        photo = supplier.photo
        last_name = supplier.last_name
        city = supplier.city
        region = supplier.region
        street = supplier.street
        email = supplier.email
        phone = supplier.phone

        products = Product.objects.filter(suppliers = supplier)


        ctx = {
            'photo': photo,
            'name': name,
            'last_name': last_name,
            'city': city,
            'region': region,
            'street': street,
            'email': email,
            'phone': phone,
            'products': products
        }
        return render(request, "supplier_info.html", ctx)



class AddCategoryView(View):
    def get(self, request):
        form = AddCategoryForm()

        ctx = {
            "form": form
        }
        return render(request, "add_category.html", ctx)

    def post(self, request):
        form = AddCategoryForm(request.POST)
        if form.is_valid():

            category_name = form.cleaned_data['category_name']
            slug = form.cleaned_data['slug']


            newcat = Category.objects.create(category_name = category_name, slug = slug)


            return HttpResponseRedirect('/supplier_list/')
        else:
            ctx = {'form': form}
            return render(request, 'add_category.html', ctx)


class AddProductView(View):
    def get(self, request):
        form = AddProductForm()

        ctx = {
            "form": form
        }
        return render(request, "add_product.html", ctx)

    def post(self, request):
        form = AddProductForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            supplier = form.cleaned_data['suppliers']
            category = form.cleaned_data['categories']

            newprod = Product.objects.create(name = name, description = description,
                                              categories= category)
            newprod.suppliers.add(*list(supplier))


            return HttpResponseRedirect('/product_add/')
        else:
            ctx = {'form': form}
            return render(request, 'add_product.html', ctx)


class CategoryInfoView(View):

    def get(self, request, slug):

        category = Category.objects.get(slug=slug)

        product = Product.objects.filter(categories=category.slug)
        products = product.order_by('name')


        ctx = {
            'products': products,
            'category': category
        }
        return render(request, "category_info.html", ctx)

class OrderView(View):
    def get(self, request):
        form = SearchForm()
        supplier = Supplier.objects.order_by('name')

        ctx = {
            'form': form,
            'supplier': supplier,
               }
        return render(request, "order.html", ctx)

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']


            product = Product.objects.filter(name__icontains=search)
            # supplier= Supplier.objects.order_by('name')
            ctx = {
                # 'supplier':supplier,
                'products': product,
                        }

            return render(request, "order.html", ctx)

class OrderAddView(APIView):

    def post(self, request):

        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        data = (serializer.data)
        list = (data["product"])

        myuser= request.user
        o = Order.objects.create(client=myuser)

        for pr in list:
            p=Product.objects.get(name=pr)

            o.product.add(p)




        print('dupa2')
        return HttpResponse()

class OrderViewView(View):

    def get(self, request):

        myuser = request.user
        orders = Order.objects.filter(client=myuser)


        ctx = {
            "orders": orders
        }
        return render(request, "order_view.html", ctx)


class ForumView(View):
    def get(self, request):
        ctx = {

        }
        return render(request, "forum.html", ctx)