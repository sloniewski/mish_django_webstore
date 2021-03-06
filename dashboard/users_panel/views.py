from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import reverse

from django_filters.views import FilterView

from dashboard.main.mixins import StaffOnlyMixin
from .forms import UserBulkActions, FilterUsersForm

User = get_user_model()


class StaffListView(StaffOnlyMixin, FilterView):
    model = User
    template_name = 'dashboard/users/staff_list.html'
    strict = False
    paginate_by = 20
    filterset_class = FilterUsersForm

    def get_queryset(self):
        return self.model.objects.staff()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if self.filterset.is_bound and self.page_kwarg not in self.request.GET.keys():
            messages.info(
                self.request,
                'Found {} objects in database'.format(len(self.object_list)),
            )
        return response

    def get_context_data(self, *args, **kwargs):
        context = super(StaffListView, self).get_context_data(*args, **kwargs)
        context.update({
            'actions': list(UserBulkActions.keys()),
        })
        return context


class ClientListView(StaffOnlyMixin, FilterView):
    model = User
    template_name = 'dashboard/users/client_list.html'
    strict = False
    paginate_by = 20
    filterset_class = FilterUsersForm

    def get_queryset(self):
        return self.model.objects.clients()

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if self.filterset.is_bound and self.page_kwarg not in self.request.GET.keys():
            messages.info(
                self.request,
                'Found {} objects in database'.format(len(self.object_list)),
            )
        return response

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'actions': list(UserBulkActions.keys()),
        })
        return context


class UserBulkActionView(StaffOnlyMixin, FormView):
    template_name = 'dashboard/users/bulk_action.html'
    model = User

    def get_form_class(self):
        action = self.get_action()
        return UserBulkActions[action]

    def get_action(self):
        action = self.request.POST.get('action')
        if action not in list(UserBulkActions.keys()) or action is None:
            raise Http404("requested action not found")
        return self.request.POST.get('action')

    def post(self, *args, **kwargs):
        submitted = self.request.POST.get('submit')
        if submitted == 'select':
            return self.get(self.request, *args, **kwargs)
        elif submitted == 'save':
            return super().post(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.execute()
        messages.success(self.request, form.get_message())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'action': self.get_action(),
            'object_list': self.model.objects.filter(id__in=self.request.POST.getlist('object_list'))
        })
        return context

    def get_success_url(self):
        return reverse('users_panel:client-list')


class StaffLoginView(LoginView):
    # TODO redirect after login
    template_name = 'dashboard/users/login.html'

    def get_success_url(self):
        if not self.request.user.is_staff:
            return reverse('product:product-list')
        if not self.request.GET.get(self.redirect_field_name):
            return reverse('product_panel:product-list')
        return super().get_success_url()


class StaffLogoutView(LogoutView):
    template_name = 'dashboard/users/logout.html'
