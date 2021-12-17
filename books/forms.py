from django.forms import ModelForm, RadioSelect
from books.models import Ticket, Review


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "description", "image")


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ("headline", "rating", "body")
        CHOICES = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
        widgets = {"rating": RadioSelect(choices=CHOICES)}
