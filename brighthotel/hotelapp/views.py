from django.shortcuts import render, HttpResponse, redirect

from hotelapp.forms import ContactForm, RegisterForm, ConventionhallForm, RatingForm, BookingForm,NotificationsForm

from hotelapp.models import Register, Contact, admin, Conventionhall, Rating, Booking,Notifications

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os


# from django.contrib.auth.models import user

# Create your views here.
def openindex(request):
    return render(request, "index.html", {})


def openabout(request):
    return render(request, "about.html", {})


def opencontact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
        return render(request, "contact.html", {"msg": "saved successfully"})
    return render(request, "contact.html", {})


def openhome(request):
    return render(request, "index.html", {})


def opencustomer(request):
    return render(request, "customer.html", {})


def openregister(request):
    return render(request, "register.html", {})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        email = request.POST["email"]
        if Register.objects.filter(email=email).exists():
            return render(request, "register.html", {"msg": "this email already exists"})
        else:
            if form.is_valid():
                try:
                    form.is_valid()
                    form.save()
                    return render(request, "customer.html", {"msg": "registration successful"})
                except Exception as e:
                    return render(request, "register.html", {"msg": "invalid data"})
            return render(request, "register.html", {"msg": "invalid data"})

        # form = RegisterForm(request.POST)
        # if form.is_valid():
        #     try:
        #         form.save()
        #     # email_form=settings.Email_HOST_USER
        #
        #     except Exception as e:
        #         print(e)


def opencustomer_home(request):
    return render(request, "customer_home.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        login = Register.objects.filter(email=email, password=password)
        if login.exists():
            request.session['email'] = email
            customer = Register.objects.get(email=email)
            return render(request, "customer_home.html", {"msg": customer.name})
        else:
            return render(request, "register.html", {"msg": "not valid"})

    else:
        return render(request, "register.html", {"msg": "not valid"})


def customer_logout(request):
    request.session["email"] = ""
    return render(request, "customer.html", {})


def viewcontactdetails(request):
    y = Contact.objects.all()
    return render(request, "viewcontactdetails.html", {"y": y})


def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/viewcontactdetails')


def view_Details(request):
    email = request.session["email"]
    customer = Register.objects.get(email=email)
    return render(request, "view_Details.html", {"customer": customer})


def change_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        newpassword = request.POST["newpassword"]
        customer = Register.objects.get(email=email, password=password)
        customer.email = email
        customer.password = newpassword
        customer.save()

        # login=Register.objects.filter(email=email,password=password)
        # if login.exists():
        #     password=newpassword

        return render(request, "customer.html", {})

    return render(request, "change_password.html", {})


def update_profile(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        mobile_number = request.POST["mobile_number"]
        city = request.POST["city"]
        address = request.POST["address"]
        customer = Register.objects.get(email=email)
        customer.email = email
        customer.password = password
        customer.name = name
        customer.mobile_number = mobile_number
        customer.city = city
        customer.address = address
        customer.save()
        return render(request, "customer.html", {"customer": customer})
    return render(request, "update_profile.html", {})


def openadmin(request):
    return render(request, "admin.html", {})


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        login = admin.objects.filter(email=email, password=password)
        if login.exists():
            request.session['email'] = email
            customer = admin.objects.get(email=email)
            return render(request, "admin_home.html", {})
        else:
            return render(request, "admin.html", {"msg": "not valid"})

    else:
        return render(request, "admin.html", {"msg": "not valid"})


def admin_logout(request):
    request.session["email"] = ""
    return render(request, "admin.html", {})


def admin_change_password(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        newpassword = request.POST["newpassword"]
        Admin = admin.objects.get(email=email, password=password)
        Admin.email = email
        Admin.password = newpassword
        Admin.save()

        return render(request, "admin.html", {})

    return render(request, "admin_change_password.html", {})


def admin_view_details(request):
    customer = Register.objects.all()
    return render(request, "admin_view_details.html", {"customer": customer})


def deletecustomer(request, id):
    customer = Register.objects.get(id=id)
    customer.delete()
    return redirect('admin_view_Details/')


def admin_add_conventionhall(request):
    if request.method == "POST":
        form = ConventionhallForm(request.POST, request.FILES)
        email = request.POST["email"]
        if Conventionhall.objects.filter(email=email).exists():
            return render(request, "admin_add_conventionhall.html", {"msg": "this email already exists"})

        else:
            if form.is_valid():
                print(form.errors)
                try:
                    form.is_valid()
                    form.save()
                    return render(request, "admin_home.html", {"msg": "registration successful"})
                except Exception as e:
                    print(e)
                    return render(request, "admin_add_conventionhall.html", {"msg": "invalid data1"})
            return render(request, "admin_add_conventionhall.html", {"msg": "invalid data"})
    return render(request, "admin_add_conventionhall.html", {"msg": "invalid data"})


def openadmin_add_conventionhall(request):
    return render(request, "admin_add_conventionhall.html", {})


def admin_view_conventionhall(request):
    y = Conventionhall.objects.all()
    return render(request, "admin_view_conventionhall.html", {"y": y})


def deleteconventionhall(request, id):
    customer = Conventionhall.objects.get(id=id)
    customer.delete()
    return redirect('admin_view_conventionhall/')


def customer_view_conventionhall(request):
    y = Conventionhall.objects.all()
    return render(request, "customer_view_conventionhall.html", {"y": y})


def rating(request, id):
    email = request.session["email"]
    print("email")
    customer = Register.objects.get(email=email)
    print("hello")
    hall = Conventionhall.objects.get(id=id)
    if request.method == "POST":
        form = RatingForm(request.POST)
        print(form.errors)
        email = request.POST["email"]
        if Rating.objects.filter(email=email).exists():
            return render(request, "rating.html", {"msg": "this email already exists", "hall": hall, "email": email})

        else:
            if form.is_valid():
                print(form.errors)
                try:
                    form.is_valid()
                    form.save()
                    return render(request, "rating.html", {"msg": "thank you for rating", "hall": hall, "email": email})
                except Exception as e:
                    print(e)
                    return render(request, "rating.html", {"msg": "invalid data1", "hall": hall, "email": email})
            return render(request, "rating.html", {"msg": "invalid data", "hall": hall, "email": email})
    return render(request, "rating.html", {"msg": "invalid data3", "hall": hall, "email": email})


# def rating(request,id):
#     y=Conventionhall.objects.get(id=id)
#     return render(request,"rating.html",{"y":y})

def edit_conventionhall(request):
    if request.method == "POST":
        print("error:")
        id = request.POST["id"]
        print("hello")
        customer = Conventionhall.objects.get(id=id)
        customer = ConventionhallForm(request.POST, instance=customer)
        print("error:", customer.errors)
        if customer.is_valid():
            print("error:", customer.errors)
            customer.save()
        return redirect("/admin_view_conventionhall")
    return redirect("/admin_view_conventionhall")


def open_edit_conventionhall(request, id):
    y = Conventionhall.objects.get(id=id)
    return render(request, "edit_conventionalhall.html", {"y": y})


def view_ratings(request, id):
    y = Conventionhall.objects.get(id=id)
    customer = Rating.objects.filter(conventionhall_id=y.id)
    return render(request, "view_ratings.html", {"customer": customer, "y": y})


def booking(request, id, cost):
    email = request.session["email"]
    print("email")
    customer = Register.objects.get(email=email)
    print("hello")
    hall1 = Conventionhall.objects.get(id=id)
    hall2 = Conventionhall.objects.get(cost=cost)
    print("hello12")
    if request.method == "POST":
        print("hii1")
        form = BookingForm(request.POST)
        print("hii11")
        print(form.errors)
        email = request.POST["email"]
        if form.is_valid():
            print("hii2")
            print(form.errors)
            try:
                form.is_valid()
                form.save()
                print("save1")
                return render(request, "customer_view_conventionhall.html",
                              {"msg": "thank you for booking", "hall1": hall1, "hall2": hall2, "email": email})
            except Exception as e:
                print(e)
                print("22")
                return render(request, "booking.html", {"msg": "invalid data1", "hall1": hall1, "email": email})
    return render(request, "booking.html", {"msg": "invalid data3", "hall1": hall1, "hall2": hall2, "email": email})


def admin_view_booking(request):
    z = Conventionhall.objects.all()
    y = Booking.objects.all()
    return render(request, "admin_view_booking.html", {"y": y, "z": z})


def accept(request, id):
    x = Booking.objects.get(id=id)
    if x.status == "new":
        x.status = "accepted"
        x.save()
        return render(request, "admin_view_booking.html", {"msg": "accepted"})
    else:
        return render(request, "admin_view_booking.html", {"msg": "customer already cancelled the booking"})


def reject(request, id):
    x = Booking.objects.get(id=id)
    if x.status == "new":
        x.status = "rejected"
        x.save()
        return render(request, "admin_view_booking.html", {"msg": "rejected"})
    else:
        return render(request, "admin_view_booking.html", {"msg": "customer already cancelled the booking"})


def customer_view_booking(request):
    email = request.session["email"]
    y = Booking.objects.filter(email=email)
    return render(request, "customer_view_booking.html", {"y": y})


def cancel(request, id):
    x = Booking.objects.get(id=id)
    if x.status == "new" or "accepted":
        x.status = "cancelled"
        x.save()
        return render(request, "customer_view_booking.html", {"msg": "canceled"})
    else:
        return render(request, "customer_view_booking.html", {"msg": "Admin already rejected the booking"})


def admin_add_notifications(request):
    if request.method == "POST":
        form = NotificationsForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.errors)
            try:
               form.is_valid()
               form.save()
               return render(request, "admin_home.html", {"msg": "Added successfully"})
            except Exception as e:
                return render(request, "admin_add_notifications.html", {"msg": "invalid data1"})
        return render(request, "admin_add_notifications.html", {"msg": "invalid data"})
    else:
        return render(request, "admin_add_notifications.html", {"msg": "invalid data"})


def customer_view_notifications(request):
    y = Notifications.objects.all()
    return render(request, "customer_view_notifications.html", {"y": y})
