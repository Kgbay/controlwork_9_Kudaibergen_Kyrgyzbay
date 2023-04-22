from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from gallery_app.forms import ImageForm
from gallery_app.models import Image


class ImageDetail(DetailView):
    template_name = 'image.html'
    model = Image


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'developer']).exists()


class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'image_create.html'
    form_class = ImageForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


class ImageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'image_update.html'
    form_class = ImageForm
    model = Image

    def get_success_url(self):
        return reverse('post_view', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("У вас нет прав редактировать этот пост")
        return super(ImageUpdateView, self).dispatch(request, *args, **kwargs)


class ImageDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'image_confirm_remove.html'
    model = Image
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("У вас нет прав удалять этот пост")
        return super(ImageDeleteView, self).dispatch(request, *args, **kwargs)
