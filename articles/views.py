from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article
# your_project/your_app/views.py (yoki models.py)

from utils.email_utils import send_email
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.exceptions import ValidationError

def send_email(subject, message, to_email):
    try:
        send_mail(
            subject,
            message,
            'from@example.com',
            [to_email],
            fail_silently=False,
        )
        print("Email yuborildi!")
    except ValidationError as e:
        print(f"Xatolik: {e}")

def my_view(request):
    to_email = 'qabul_qiluvchi_email@example.com'
    subject = 'Salom'
    message = 'Assalomu alaykum! Bu salom xabaridir.'

    send_email(subject, message, to_email)

    return render(request, 'my_template.html', {'context_variable': 'qiymat'})

to_email = 'qabul_qiluvchi_email@example.com'
subject = 'salom qoondee'
message = render_to_string('email_template.html', {'context_variable': 'qiymat'})

send_email(subject, message, to_email)


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo',)
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'summary', 'body', 'photo',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser okaying tekshirish
    def test_func(self):
        return self.request.user.is_superuser
