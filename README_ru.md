# faker_researcher_ids

Расширение для Python-пакета `Faker`. Позволяет генерировать фейковые идентификаторы авторов, используемые в наукометрических базах данных и системах учёта публикаций:
- Scopus;
- ORCID;
- Web of Science;
- Google Scholar.

## Установка

Установка при помощи `pip`:  
```bash
pip install faker_researcher_ids
```

Или с использованием `uv`:  
```bash
uv add faker_researcher_ids
```

## Использование

1. Импортируйте необходимые зависимости:  
```python
from faker import Faker  
from faker_researcher_ids import ScientificProvider
```

2. Создайте экземпляр класса `Faker`:
```python
fake = Faker()
```

3. Добавьте провайдера к созданному экземпляру:
```python
fake.add_provider(ScientificProvider)
```

### Генерация идентификаторов

```python
# Scopus Author ID
>>> fake.scopus_id()
'53070267764'

# Web of Science ID (aka ResearcherID)
>>> fake.wos_id()
'O-2416-2014'

# ORCID
>>> fake.orcid()
'https://orcid.org/0009-0008-7383-0730'

# Google Scholar ID
>>> fake.google_scholar_id()
'ogf35PW74DCe'
```