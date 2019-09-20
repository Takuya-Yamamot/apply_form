from django.urls import path
from django.conf.urls import include
from .views import index, ApllyFormView, ApllyResultView

app_name = "forms"
urlpatterns = [
    path("", index, name="index"),
    path("apply/", ApllyFormView.as_view(), name="apply"),
    path("apply/result/", ApllyResultView.as_view(), name="result"),
]
