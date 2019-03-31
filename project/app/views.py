from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import Message


class MesIndexView(generic.ListView):
    model = Message


class MesAddView(PermissionRequiredMixin, generic.CreateView):
    model = Message
    fields = "__all__"
    success_url = reverse_lazy("app:index")
    permission_required = ("app.add_message",)
    raise_exception = True


class MesChangeView(PermissionRequiredMixin, generic.UpdateView):
    model = Message
    fields = "__all__"
    success_url = reverse_lazy("app:index")
    permission_required = ("app.change_message",)
    raise_exception = True


class MesDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Message
    fields = "__all__"
    success_url = reverse_lazy("app:index")
    permission_required = ("app.delete_message",)
    raise_exception = True
