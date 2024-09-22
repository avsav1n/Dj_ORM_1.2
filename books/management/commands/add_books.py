import json
from typing import Any

from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        with open(r'fixtures\books.json', encoding='utf-8') as fr:
            data = json.load(fr)
            
        for book in data:
            model = Book(**book['fields'])
            model.save()