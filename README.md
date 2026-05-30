# 📋 Task Tracker API

> Повноцінний REST API для управління задачами з JWT авторизацією, побудований на Django REST Framework

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?style=flat-square&logo=django)
![DRF](https://img.shields.io/badge/DRF-3.15-red?style=flat-square)
![JWT](https://img.shields.io/badge/JWT-Auth-orange?style=flat-square)

---

## ✨ Можливості

- 🔐 JWT авторизація (реєстрація, логін, refresh токен)
- ✅ Повний CRUD для задач
- 👤 Кожен користувач бачить тільки свої задачі
- 🎯 Пріоритети задач (low / medium / high)
- 📊 Статуси задач (todo / in_progress / done)
- 🌐 Фронтенд на HTML + JS

---

## 🛠 Технології

| Технологія | Версія | Призначення |
|---|---|---|
| **Python** | 3.13 | Мова програмування |
| **Django** | 5.0 | Веб-фреймворк |
| **Django REST Framework** | 3.15 | REST API |
| **SimpleJWT** | 5.3 | JWT авторизація |
| **SQLite** | — | База даних (dev) |
| **Gunicorn** | — | WSGI сервер (prod) |

---

## 📁 Структура проекту

```
TaskDRF/
├── config/
│   ├── settings.py     ← налаштування проекту
│   └── urls.py         ← головні маршрути
├── tasks/
│   ├── models.py       ← модель Task
│   ├── serializers.py  ← серіалізатори
│   ├── views.py        ← ViewSet + реєстрація
│   ├── urls.py         ← маршрути app
│   └── admin.py        ← адмін панель
├── index.html          ← фронтенд
├── Procfile            ← для деплою
├── requirements.txt    ← залежності
└── manage.py
```

---

## 🚀 Запуск локально

### 1. Клонуй репозиторій
```bash
git clone https://github.com/ohnista-lks07/task-tracker.git
cd task-tracker
```

### 2. Створи віртуальне середовище
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Встанови залежності
```bash
pip install -r requirements.txt
```

### 4. Застосуй міграції
```bash
python manage.py migrate
```

### 5. Створи суперюзера
```bash
python manage.py createsuperuser
```

### 6. Запусти сервер
```bash
python manage.py runserver
```

---

## 📌 API Ендпоінти

### Авторизація

| Метод | URL | Опис |
|---|---|---|
| `POST` | `/api/register/` | Реєстрація нового користувача |
| `POST` | `/api/token/` | Отримати JWT токени |
| `POST` | `/api/token/refresh/` | Оновити access токен |

### Задачі (потребують JWT токен)

| Метод | URL | Опис |
|---|---|---|
| `GET` | `/api/tasks/` | Список всіх задач користувача |
| `POST` | `/api/tasks/` | Створити нову задачу |
| `GET` | `/api/tasks/{id}/` | Отримати одну задачу |
| `PUT` | `/api/tasks/{id}/` | Оновити задачу повністю |
| `PATCH` | `/api/tasks/{id}/` | Оновити задачу частково |
| `DELETE` | `/api/tasks/{id}/` | Видалити задачу |

---

## 📝 Приклади запитів

### Реєстрація
```json
POST /api/register/
{
  "username": "sasha",
  "password": "mypassword123",
  "email": "sasha@example.com"
}
```

### Логін → отримати токени
```json
POST /api/token/
{
  "username": "sasha",
  "password": "mypassword123"
}

← Відповідь:
{
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

### Створити задачу
```json
POST /api/tasks/
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

{
  "title": "Зробити домашнє",
  "description": "Написати серіалізатори",
  "status": "todo",
  "priority": "high"
}
```

### Оновити статус
```json
PATCH /api/tasks/1/
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

{
  "status": "done"
}
```

---

## 🎨 Модель Task

```python
class Task(models.Model):
    title        # Назва задачі
    description  # Опис (необов'язковий)
    status       # todo / in_progress / done
    priority     # low / medium / high
    owner        # ForeignKey → User
    created_at   # Дата створення (автоматично)
    updated_at   # Дата оновлення (автоматично)
```

---

## 🔐 JWT Flow

```
1. POST /api/register/     ← створити акаунт
2. POST /api/token/        ← отримати access + refresh
3. GET  /api/tasks/        ← запит з токеном в заголовку
   Authorization: Bearer <access_token>
4. POST /api/token/refresh/ ← коли access закінчився
   {"refresh": "<refresh_token>"}
```

---

## 👩‍💻 Автор

**Oleksandra Ognista**

[![GitHub](https://img.shields.io/badge/GitHub-ohnista--lks07-black?style=flat-square&logo=github)](https://github.com/ohnista-lks07)