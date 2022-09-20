
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Отображение всех статей из БД
class ShowNewsView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Новости'
        return ctx

# Отображение всех статей одного автора из БД
class UserAllNewsView(ListView):
    model = News
    template_name = 'news/user_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f"Новости от пользователя {self.kwargs.get('username')}"
        return ctx

# Отображение одной новости из БД
class NewsDetailView(DetailView):
    model = News
    # Можно не писать строку ниже, так как по умолчанию такой путь создается автоматически
    # модель(таблица БД)_класс.
    # Если хотим свой адрес указать, то можно прописать самим типа template_name = 'news/news_detail.html'
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx

# Создание новости
class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'news/create_news.html'

    # fields = ['title', 'text', 'img']
    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление новости'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

# Обновление существующей новости
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'news/create_news.html'
    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление новости'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

# Удаление новости
class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    # Если всет удачно, то идем на эту страницу
    success_url = '/news'
    template_name = 'news/delete-news.html'

    def get_context_data(self, **kwards):
        ctx = super(DeleteNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Удаление новости'
        ctx['btn_text'] = 'Да, удалить'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        return False
