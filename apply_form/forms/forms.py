from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .models import ApllyContent


class ApplyForm(forms.Form):
    name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "お名前"}
        ),
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "メールアドレス"}
        ),
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "お問い合わせ内容"}
        ),
    )

    def send_email(self):
        subject = "ご応募"
        message = self.cleaned_data["message"]
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        from_email = "{name} <{email}>".format(name=name, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        content = ApllyContent()
        content.message = self.cleaned_data["message"]
        content.name = self.cleaned_data["name"]
        content.email = self.cleaned_data["email"]
        ApllyContent.objects.create(
            name=content.name, email=content.email, message=content.message
        )
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
