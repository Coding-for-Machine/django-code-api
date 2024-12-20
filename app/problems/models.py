import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

# from django.template.defaultfilters import slugify
from django.utils.text import slugify


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


def get_roundom_code():
    return str(uuid.uuid4).replace(" ", "-")


# user model
User = get_user_model()


class Category(models.Model):
    name = CKEditor5Field(max_length=250)
    body = models.TextField()

    def __str__(self):
        return self.name


class Tage(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProblemsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Problems(models.Model):
    STATUS = (
        ("Oson", "Osan"),
        ("O'rta", "O'rta"),
        ("Qiyin", "Qiyin"),
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="OSON",
    )
    name = models.CharField(max_length=250)
    function_or_class_name = models.CharField(max_length=250, help_text="M: def main(args1, args2, ...) yoke class class_name: kiyin funkiya nomi. class larni yozgandan so'ng tab qo'yishni unitmang!!!")
    body = CKEditor5Field()
    slug = models.SlugField(max_length=250, blank=True)
    active = models.BooleanField(default=True)
    language = models.ManyToManyField(Language, default="python", help_text="qaysi dansturlash tillarida qullasa bo'ladi.")
    tag = models.ManyToManyField(Tage)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    published = ProblemsManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            now_slug = slugify(str(self.name))
            ex = Problems.objects.filter(slug=now_slug).exists()
            while ex:
                now_slug = slugify(str(self.name) + str(get_roundom_code()))
                ex = Problems.objects.filter(slug=now_slug).exists()
            self.slug = now_slug
        return super(Problems, self).save(*args, **kwargs)

class Answer(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=1)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)



class Comments(models.Model):
    body = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    # objects = models.manager()
    # published = CommidManager()

    def _str__(self):
        return self.body[:20]

    def get_absolute_url(self):
        return reverse(
            "runcode:commid-detile", kwargs={"id": self.id, "slug": self.slug}
        )

    def save(self, *args, **kwargs):
        if self.name:
            now_slug = slugify(str(self.name))
            ex = Comments.objects.filter(slug=now_slug).exists()
            while ex:
                now_slug = slugify(str(self.name) + str(get_roundom_code))
                ex = Comments.objects.filter(slug=now_slug).exists()
            self.slug = now_slug
        return super(Comments, self).save(*args, **kwargs)



class Algorithm(models.Model):
    problems = models.ForeignKey(Problems, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    code = models.TextField(
        help_text="Natijaga Erishish Uchin eng yaxshi va samarali codni kiriting!"
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.problems.name