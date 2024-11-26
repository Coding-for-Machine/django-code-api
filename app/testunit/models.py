 
from django.db import models
from problems.models import Problems, Language
import os
from pathlib import Path

DIR = Path(__file__).resolve().parent.parent

class Unittestproblems(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    unit_test_class_name = models.CharField(help_text="pastdagi kiritgan class nomi bo'lishi kerak!!!", max_length=100)
    unit_test_code = models.TextField(help_text="misol: python dasturlash tilidagi unittest orqali yozilgan kod bo'lish kerak yoki boshqa dasturlash tilida u dasturlash tillari qo'shilgan bo'lsa!!!")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.language.name} {self.problem.name if self.problem else ''}"

class Memorytime(models.Model):
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    memory_time_code = models.TextField(help_text="misol: python dasturlash tilidagi tracemalloc (3.4 versiadan yuqorida ishlaydi) orqali yozilgan kod bo'lish kerak yoki boshqa dasturlash tilida u dasturlash tillari qo'shilgan bo'lsa")
    line1 = models.TextField(help_text="User  uchun 1 kod(python dasturlash tilidagi tracemalloc yozilgan)")
    line2 = models.TextField(help_text="User  uchun 1 kod(python dasturlash tilidagi tracemalloc yozilgan)")

    def __str__(self):
        return str(self.language.name + (self.problem.name if self.problem else ""))