# faker_researcher_ids

Розширення для Python-пакета `Faker`. Дає змогу генерувати фейкові ідентифікатори авторів, подібні до використовуваних у наукометричних базах даних і системах обліку публікацій:
- Scopus;
- ORCID;
- Web of Science;
- Google Scholar.

## Інсталяція

Інсталяція за допомогою `pip`:  
```bash
pip install faker_researcher_ids
```

Або з використанням `uv`:  
```bash
uv add faker_researcher_ids
```

## Застосування

1. Імпортуйте необхідні залежності:  
```python
from faker import Faker  
from faker_researcher_ids import ScientificProvider
```

2. Створіть екземпляр класу `Faker`:
```python
fake = Faker()
```

3. Додайте провайдера до створеного екземпляра:
```python
fake.add_provider(ScientificProvider)
```

### Генерування ідентифікаторів

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