from faker import Faker
from faker_researcher_ids import ScientificProvider
import pytest
import re

fake = Faker()
fake.add_provider(ScientificProvider)

@pytest.fixture(params=[2015, 2023])
def template_from_year(monkeypatch, request):
    def mock_random_int(*args, **kwargs):
        return request.param
    
    monkeypatch.setattr(ScientificProvider, 'random_int', mock_random_int)
    template = r'[A-Z]-\d{4}-20\d{2}' if request.param < 2022 else r'[A-Z]{3}-\d{4}-20\d{2}'
    return {'year': request.param, 'template': template}

def test_wos_id(template_from_year):
    wos_id = fake.wos_id()
    assert re.fullmatch(template_from_year.get('template'), wos_id)
    assert wos_id.endswith(str(template_from_year.get('year')))

def test_orcid_structure():
    orcid = fake.orcid()
    assert re.fullmatch(r'https://orcid.org/000\d-\d{4}-\d{4}-\d{3}(\d|X)', orcid)

@pytest.mark.parametrize('orcid, expected', [
    ('21825009', '7'),
    ('21694233', 'X'),
    ('900057196681', '9')
])
def test_orchid_checksum(orcid: str, expected: str):
    assert ScientificProvider._orcid_checksum(orcid) == expected

def test_scopus_id():
    assert re.fullmatch(r'\d{11}', fake.scopus_id())

def test_google_scholar_id():
    assert re.fullmatch(r'[A-Za-z0-9]{12}', fake.google_scholar_id())