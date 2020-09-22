import os
from tech_news_data_collector.news_importer import *

CURRENT_PATH = os.path.dirname(__file__)

def test_json_importer_sucesso():
    file_path = os.path.join(CURRENT_PATH, 'fixture', 'doc.json')
    res = json_importer(file_path)
    assert len(res) == 1
    assert res[0]['title'] == 'Alemanha já trabalha na regulamentação de carros autônomos'
    assert len(res[0]['categories']) == 4
    for cat in res[0]['categories']:
        assert cat in ["Mobilidade Urbana/Smart Cities", "Veículos autônomos", "Carro", "Política"]
