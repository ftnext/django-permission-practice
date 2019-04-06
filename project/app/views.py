from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission, Group
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Message
from .forms import UserCreateForm


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


class UserCreateView(PermissionRequiredMixin, generic.CreateView):
    form_class = UserCreateForm
    template_name = "app/user_form.html"
    success_url = reverse_lazy("app:index")
    permission_required = ("auth.add_user")
    raise_exception = True

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        kind = form.cleaned_data["kind"]
        if kind == "user":
            permission = Permission.objects.get(codename="add_message")
            user.user_permissions.add(permission)
        elif kind == "group":
            group = Group.objects.get(name='can-edit-and-delete-group')
            user.groups.add(group)
        else:
            pass  # ここには「基本的」に来ない。raise Http404 とかしといても良いかもしれない

        return HttpResponseRedirect(self.success_url)
