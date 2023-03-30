Django ORM (Object-Relational Mapping) - это набор инструментов, который позволяет работать с базами данных в Django, используя объектно-ориентированный подход. Это означает, что вы можете использовать Python-объекты для работы с данными в базе данных, а вся работа с SQL-запросами и связью с базой данных будет скрыта от вас.

Пример использования Django ORM:

1. Создайте модель для хранения данных в базе данных:
```
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
```

2. Создайте и сохраните объект в базу данных:
```
person = Person(name='John', age=30)
person.save()
```

3. Получите данные из базы данных:
```
# Получить все объекты модели
people = Person.objects.all()

# Получить объекты, удовлетворяющие условиям фильтрации 
filtered_people = Person.objects.filter(name='John')

# Получить конкретный объект по идентификатору 
person = Person.objects.get(id=1)
```

4. Обновите данные объекта и сохраните изменения в базе данных:
```
person.age = 31
person.save()
```

5. Удалите объект из базы данных:
```
person.delete()
```

Таким образом, Django ORM позволяет легко и удобно работать с базами данных в Django, используя объекты. Он также имеет широкий набор функций для поиска, фильтрации и сортировки данных в базе данных.



Ошибка говорит о том, что функция `product_rest_list` не принимает аргументов, но по факту она получает один аргумент. Это может быть связано с тем, что вам необходимо передать объект `request` в функцию `product_rest_list`. 

Вот как можно изменить функцию, чтобы она принимала объект запроса:

```python
def product_rest_list(request):
     object_list = Product.objects.all()
     data = []

     for itm in object_list:
         data.append(
             {
                 'id': itm.id,
                 'name': itm.name,
                 'price_now': itm.price_now,
       