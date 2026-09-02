# TextChan

Просте API для анонімного блогу — будь-хто може зайти, прочитати пости 
інших і залишити власний, без реєстрації. Навчальний проект для практики 
FastAPI, SQLAlchemy та проєктування REST API.

## Функціонал

- Перегляд списку постів (з пагінацією)
- Перегляд окремого поста
- Створення поста (ім'я, тема, текст, у форматі Markdown)
- Редагування та видалення власного поста через секретний код
- Валідація вхідних даних

## Стек технологій

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Встановлення та запуск

\`\`\`bash
git clone https://github.com/Gnome-b/text-chan.git
cd text-chan
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

Після запуску документація API доступна на:
- Swagger UI: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Приклади запитів

### Створити пост
\`\`\`
POST /posts
{
  "name": "Аноним",
  "topic": "Перший пост",
  "text": "Привіт усім!",
  "secret_code": "1234"
}
\`\`\`

### Отримати список постів
\`\`\`
GET /posts?page=1&limit=10
\`\`\`

### Видалити пост
\`\`\`
DELETE /posts/{id}
{
  "secret_code": "1234"
}
\`\`\`

## Статус проекту

Навчальний проект