import pandas as pd
import plotly.express as px
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from rest_framework.viewsets import ModelViewSet

from core.forms import RegisterForm
from core.models import User, EURUSD_H1
from core.serializers import UserSerializer


class SignupView(CreateView):
    """
    Регистрация
    """
    queryset = User.objects.all()
    form_class = RegisterForm
    success_url = '/signin/'
    template_name = 'core/signup.html'


class SigninView(LoginView):
    """
    Логин
    """
    redirect_authenticated_user = True
    template_name = "core/login.html"


class UserViewSet(ModelViewSet):
    """
    Стартовая страница, если пользователь авторизован, то перенаправляет его на профиль, иначе остается на index.html
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def auth_page(request):
        if request.user.is_authenticated:
            return redirect("/main/")
        return render(request, "core/index.html")


# class UserProfileView(LoginRequiredMixin, ListView):
#     """
#     Профиль
#     """
#     model = User
#     login_url = '/signin/'
#     template_name = "core/main.html"
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['qs'] = EURUSD_D1.objects.all()
#     #     print(context['qs'])
#     #     return context
#
#     df = pd.read_sql()
#
#     fig = go.Figure(data=[go.Candlestick(x=df['Date'],
#                                          open=df['AAPL.Open'],
#                                          high=df['AAPL.High'],
#                                          low=df['AAPL.Low'],
#                                          close=df['AAPL.Close'])])

    # fig.show()

class EURUSD_H1View(LoginRequiredMixin, ListView):
    model = EURUSD_H1.objects.all()
    login_url = '/signin/'
    template_name = "core/main.html"

    def get(self):
        qs = EURUSD_H1.objects.all()
        print(qs)
        projects_data = [
            {
                'time': x.time,
                'open': x.open,
                'high': x.high,
                'low': x.low,
                'close': x.close,

            } for x in qs
        ]
        df = pd.DataFrame(projects_data)

        fig = px.timeline(
            df,
        )