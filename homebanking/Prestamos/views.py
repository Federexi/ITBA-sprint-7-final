from http import client
from django.shortcuts import render
from Clientes.models import Cliente
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views import generic
from .forms import LoanForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class LoanRequest(generic.CreateView):
    form_class = LoanForm
    success_url = reverse_lazy('prestamos')
    template_name = 'Prestamos/template/Prestamos/prestamos.html'

    def form_valid(self, form):
        user = self.request.user
        cliente = Cliente.objects.get(user_id = user.id)
        if not cliente.approve_loan(form.cleaned_data.get('loan_total')):
            form.add_error(field = None, error = 'Prestamo no aprobado')
            return self.form_invalid(form)
        else:
            form.instance.customer_id = cliente
            super(LoanRequest, self).form_valid(form)

            return render(self.request, 'Prestamos/template/Prestamos/prestamos.html', context={'form': form, 'success_msg': 'Prestamo aprobado!'})
