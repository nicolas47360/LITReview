from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse
from books import forms
from books.models import Ticket, Review


class CreateTicketView(LoginRequiredMixin, CreateView):

    form_class = forms.TicketForm
    template_name = 'ticket.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        #return reverse('update', kwargs={'pk': self.object.pk})
        return reverse('update', args=[self.object.pk])


class UpdateTicketView(LoginRequiredMixin, UpdateView):
    model = Ticket
    form_class = forms.TicketForm
    template_name = 'update_ticket.html'


class DeleteTicketView(LoginRequiredMixin, DeleteView):
    form_class= forms.TicketForm
    template_name = 'delete_ticket.html'


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class_ticket = forms.TicketForm
    form_class_review = forms.ReviewForm
    template_name = 'create_review.html'

    def get(self, request, *args, **kwargs):
        form_ticket = self.form_class_ticket()
        form_review = self.form_class_review()
        return render(request, self.template_name,
                      context={'form_ticket': form_ticket, 'form_review': form_review})

    def post(self, request, *args, **kwargs):
        form_ticket = self.form_class_ticket(request.POST)
        form_review = self.form_class_review(request.POST)
        form_ticket.instance.user = self.request.user
        form_review.instance.user = self.request.user
        if form_ticket.is_valid():
            ticket = form_ticket.save()
            form_review.instance.ticket = ticket
            if form_review.is_valid():
                form_review.save()
        return render(request, self.template_name,
                      context={'form_ticket': form_ticket, 'form_review': form_review})


class UpdateReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = forms.TicketForm
    template_name = 'update.html'


class DeleteReviewView(LoginRequiredMixin, DeleteView):
    form_class = forms.TicketForm
    template_name = 'delete_review.html'


class HomeView(LoginRequiredMixin, CreateView):
    template_name = 'home.html'
    form_class = forms.TicketForm
