from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Link
from .forms import LinkForm
# Модули для получения поля title из URL
import urllib.request
from bs4 import BeautifulSoup #Альтернативная установка:  python -m pip install BeautifulSoup4

class listlink(ListView):
    model = Link
    template_name = 'link.html'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(listlink, self).get_context_data(**kwargs)
        links = Link.objects.filter(user=self.request.user).order_by('-id')

        ctx['title'] = 'Создание коротких ссылок'
        ctx['links'] = links
        ctx['form'] = LinkForm
        return ctx

    def post(self, request, *args, **kwargs):
        form = LinkForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            # Получение поля title из URL
            url = form.longlink
            try:
                headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'} 
                requestURL=urllib.request.Request(url,None,headers)
                response = urllib.request.urlopen(requestURL)
                html = response.read()
                form.title = BeautifulSoup(html, "html.parser").title.string
            except Exception: 
                messages.error(request, f'Ссылка некорректная!')
                return redirect('/link/')
            # Сохоанение формы
            form.save()
            messages.success(request, f'Успешно добавлена короткая ссылка!')
            return redirect('/link/')
        else :
            return render(request, 'link/link.html', {'form': form, 'links': Link.objects.filter(user=self.request.user).order_by('-id')})

# Удаление ссылки 
def delete_link(request, link_id):
    obj = Link.objects.get(id=link_id)
    if request.user == obj.user:
        obj.delete()
    messages.success(request, f'Ссылка успешно удалена!')
    return redirect('/link/')

# Переход по короткой ссылке
def GoToLink(request, short):
    url = get_object_or_404(Link, slug=short)
    return HttpResponseRedirect(url.longlink)