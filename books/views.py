from datetime import datetime

from django.shortcuts import redirect, render
from django.urls import reverse

from books.helpers import NavigationDates
from books.models import Book


def books_view(request):
    return redirect(reverse('catalog'))

def catalog_view(request):
    books = Book.objects.all()
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)

def same_date_books_view(request, date: datetime.date):
    template = 'books/books_same_date.html'
    books = Book.objects.filter(pub_date=date)
    dates = NavigationDates().dates

    len_dates = len(dates) - 1
    curr_date_id = dates.index(date)
    
    context = {
        'next_page': (False if curr_date_id + 1 > len_dates 
                      else dates[curr_date_id + 1].strftime('%Y-%m-%d')),
        'prev_page': (False if curr_date_id - 1 < 0 
                      else dates[curr_date_id - 1].strftime('%Y-%m-%d')),
        'books': books
        }
    return render(request, template, context)
