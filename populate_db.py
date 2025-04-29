import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_links.settings")
django.setup()

from users.models import User
from links.models import Link
from users_collections.models import Collection


def populate_users(num_users=10):
    print("Заполнение тестовыми пользователями...")
    for i in range(1, num_users + 1):
        user = User.objects.create_user(
            username=f"user{i}",
            email=f"user{i}@example.com",
            password="password123"
        )
        print(f"Создан пользователь: {user.username}")


def populate_links(num_links=20):
    print("Заполнение тестовыми ссылками...")
    base_urls = [
        "https://example.com",
        "https://website.com",
        "https://sample.org",
        "https://testsite.net",
        "https://demo.io"
    ]
    for i in range(1, num_links + 1):
        link = Link.objects.create(
            title=f"Ссылка {i}",
            description=f"Описание ссылки {i}",
            url=f"{random.choice(base_urls)}/page{i}",
            image=f"https://via.placeholder.com/150?text=Image+{i}",
            link_type=random.choice(['website', 'article', 'video']),
        )
        print(f"Создана ссылка: {link.title}")


def populate_collections(num_collections=5):
    print("Заполнение тестовыми коллекциями...")
    for i in range(1, num_collections + 1):
        collection = Collection.objects.create(
            name=f"Коллекция {i}",
            description=f"Описание коллекции {i}",
        )
        print(f"Создана коллекция: {collection.name}")

    # Связывание ссылок с коллекциями
    print("Добавление ссылок в коллекции...")
    all_collections = Collection.objects.all()
    all_links = list(Link.objects.all())
    for collection in all_collections:
        random_links = random.sample(all_links, k=min(5, len(all_links)))
        collection.links.add(*random_links)
        print(f"В коллекцию '{collection.name}' добавлены ссылки.")


def main():
    # Очищение базы данных (опционально)
    User.objects.all().delete()
    Link.objects.all().delete()
    Collection.objects.all().delete()

    populate_users(num_users=30)
    populate_links(num_links=50)
    populate_collections(num_collections=30)

    print("База данных успешно заполнена!")


if __name__ == "__main__":
    main()
