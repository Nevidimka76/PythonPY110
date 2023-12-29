from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.views import View
from logic.services import addUserToCart, addUserToWish

class loginView(View):
    def get(self,rqst):
            return render(rqst, "login/login.html")
        
    # def login_view(request):
    #     if request.method == "GET":
    #         return render(request, "login/login.html")

    def post(self,rqst):
        data=rqst.POST
        user=authenticate(username=data['username'],password=data['password'])
        if user:
            login(rqst,user)
            addUserToCart(rqst, user.username)
            addUserToWish(rqst, user.username)
            return redirect('/')
        return render(rqst,'login/login.html',context={'error': 'Неверные данные'})

class logoutView(View):
    def get(self,rqst):
        logout(rqst)
        return redirect('/')

