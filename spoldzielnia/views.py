from django.shortcuts import render, redirect
from .models import *


def index(request):
    flats = Flats.objects.all()

    return render(request, "index.html", {"flats": flats})


def indexedit(request, flatid):
    flat = Flats.objects.get(id=flatid)

    return render(request, "indexedit.html", {"flat": flat})


def indexupdate(request, flatid):
    if 'adress' in request.GET:
        adress = request.GET['adress']

    if 'postcode' in request.GET:
        postcode = request.GET['postcode']

    if adress != "" and postcode != "":
        flat = Flats.objects.get(id=flatid)
        flat.adress = adress
        flat.postcode = postcode
        flat.save()

    return redirect(index)


def indexshow(request, flatid):
    flat = Flats.objects.get(id=flatid)
    residents = Residents.objects.filter(flat=flatid)

    return render(request, "indexshow.html", {"flat": flat, "residents": residents})


def indexnew(request):
    return render(request, "indexnew.html")


def indexcreate(request):
    if 'adress' in request.GET:
        adress = request.GET['adress']

    if 'postcode' in request.GET:
        postcode = request.GET['postcode']

    if adress != "" and postcode != "":
        Flats.objects.create(adress=adress, postcode=postcode)

    return redirect(index)


def indexdestroy(request, flatid):
    Flats.objects.get(id=flatid).delete()

    return redirect(index)


def resident(request):
    residents = Residents.objects.all()

    return render(request, "resident.html", {"residents": residents})


def residentshow(request, residentid):
    resident = Residents.objects.get(id=residentid)
    flat = Flats.objects.get(id=resident.flat.id)
    payments = Payments.objects.filter(resident=residentid)
    suma = 0

    for i in payments:
        suma += i.price

    return render(request, "residentshow.html",
                  {"resident": resident, "flat": flat, "payments": payments, "suma": suma})


def residentnew(request, flatid):
    return render(request, "residentnew.html", {"flatid": flatid})


def residentcreate(request, flatid):
    if 'firstname' in request.GET:
        firstname = request.GET['firstname']

    if 'lastname' in request.GET:
        lastname = request.GET['lastname']

    if 'NIN' in request.GET:
        NIN = request.GET['NIN']

    if firstname != "" and lastname != "" and NIN != "":
        if (Residents.objects.filter(NIN=NIN).exists() == False):
            Residents.objects.create(firstname=firstname, lastname=lastname, NIN=NIN, flat=Flats.objects.get(id=flatid))

    return redirect(indexshow, flatid)


def residentedit(request, residentid):
    resident = Residents.objects.get(id=residentid)

    return render(request, "residentedit.html", {"resident": resident})


def residentupdate(request, residentid):
    if 'firstname' in request.GET:
        firstname = request.GET['firstname']

    if 'lastname' in request.GET:
        lastname = request.GET['lastname']

    if 'NIN' in request.GET:
        NIN = request.GET['NIN']

    resident = Residents.objects.get(id=residentid)

    if firstname != "" and lastname != "" and NIN != "" and (
            Residents.objects.filter(NIN=NIN).exists() == False or resident.NIN == NIN):
        resident.firstname = firstname
        resident.lastname = lastname
        resident.NIN = NIN
        resident.save()

    return redirect(indexshow, resident.flat.id)


def residentdestroy(request, residentid):
    resident = Residents.objects.get(id=residentid)
    flatid = resident.flat.id
    resident.delete()

    return redirect(indexshow, flatid)


def paymentshow(request, paymentid):
    payment = Payments.objects.get(id=paymentid)
    resident = Residents.objects.get(id=payment.resident.id)

    return render(request, "paymentshow.html", {"resident": resident, "payment": payment})


def paymentnew(request, residentid):
    return render(request, "paymentnew.html", {"residentid": residentid})


def paymentcreate(request, residentid):
    if 'name' in request.GET:
        name = request.GET['name']

    if 'price' in request.GET:
        price = request.GET['price']

    if name != "" and price != "" and int(price) > 0:
        Payments.objects.create(name=name, price=int(price), resident=Residents.objects.get(id=residentid))

    return redirect(residentshow, residentid)


def paymentedit(request, paymentid):
    payment = Payments.objects.get(id=paymentid)

    return render(request, "paymentedit.html", {"payment": payment})


def paymentupdate(request, paymentid):
    if 'name' in request.GET:
        name = request.GET['name']

    if 'price' in request.GET:
        price = request.GET['price']

    payment = Payments.objects.get(id=paymentid)

    if name != "" and price != "" and int(price) > 0:
        payment.name = name
        payment.price = int(price)
        payment.save()

    return redirect(residentshow, payment.resident.id)


def paymentdestroy(request, paymentid):
    payment = Payments.objects.get(id=paymentid)
    residentid = payment.resident.id
    payment.delete()

    return redirect(residentshow, residentid)
