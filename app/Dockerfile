# 1. Docker tasvirining asosiy bazasi (engil Python)
FROM python:3.10-slim

# 2. Loyihaning ishchi katalogi
WORKDIR /app

# 3. Zarur kutubxonalarni o‘rnatish
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Loyihani konteynerga nusxalash
COPY . /app /app/

# 5. Static fayllarni yig‘ish
RUN python manage.py collectstatic --noinput

# 6. Portni ochish
EXPOSE 8000

# 7. Django serverni ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projectname.wsgi:application"]
