from django.shortcuts import render

def loginPage(request):
      return render(request,"loginpage.html")

def checkUser(request):
   user = request.POST.get("uname")
   password = request.POST.get("psw")
   if user == "admin" and password == "admin":
       return render(request,"welcomePage.html",{"success":"Welcome  " +user})
   else:
       return render(request,"loginpage.html",{"error":"Check ur details"})

def addMerchant(request):
    return render(request,"addMerchant.html")