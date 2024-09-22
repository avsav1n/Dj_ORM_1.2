from books.models import Book


class NavigationDates:
    '''Класс хранения информации о pub_date для навигации по страницам
    '''

    dates = sorted(Book.objects.values_list('pub_date', flat=True).distinct('pub_date'))

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance