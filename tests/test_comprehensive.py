import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
import requests
from unittest.mock import patch, MagicMock
from cachorro import get_dog_image_url
from app.app import app

# ===========================================
# TESTES POSITIVOS (1-10)
# ===========================================

# 1. Teste positivo para cachorro.py: resposta bem-sucedida da API
# Verifica se a função retorna corretamente a URL quando a API responde com dados válidos
def test_get_dog_image_url_success():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'url': 'https://example.com/dog.jpg'}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result == 'https://example.com/dog.jpg'

# 2. Teste positivo para cachorro.py: múltiplas imagens na resposta
# Verifica se a função retorna a primeira URL quando há várias imagens disponíveis
def test_get_dog_image_url_multiple_images():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'url': 'https://example.com/dog1.jpg'}, {'url': 'https://example.com/dog2.jpg'}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result == 'https://example.com/dog1.jpg'

# 3. Teste positivo para cachorro.py: resposta com informações de raça
# Verifica se a função funciona corretamente quando a resposta inclui dados adicionais (breeds)
def test_get_dog_image_url_with_breeds():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'url': 'https://example.com/dog.jpg', 'breeds': []}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result == 'https://example.com/dog.jpg'

# 4. Teste positivo para cachorro.py: URL HTTP válida
# Verifica se a função aceita URLs HTTP (não apenas HTTPS)
def test_get_dog_image_url_valid_url():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'url': 'http://example.com/dog.png'}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result == 'http://example.com/dog.png'

# 5. Teste positivo para cachorro.py: URL HTTPS segura
# Verifica se a função funciona com URLs HTTPS padrão
def test_get_dog_image_url_https():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'url': 'https://secure.example.com/dog.jpg'}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result == 'https://secure.example.com/dog.jpg'

# 6. Teste positivo para app.py: rota index bem-sucedida
# Verifica se a rota '/' retorna status 200 e contém elementos HTML esperados
def test_index_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Random Dog Generator' in response.data  # Verifica se o título está presente
        assert b'<button id="dog-btn">' in response.data  # Verifica se o botão está presente

# 7. Teste positivo para app.py: rota /dog retorna URL válida
# Verifica se a rota /dog retorna JSON com URL quando a função cachorro funciona
def test_get_dog_success():
    with patch('app.app.get_dog_image_url', return_value='https://example.com/dog.jpg'):
        with app.test_client() as client:
            response = client.get('/dog')
            assert response.status_code == 200
            assert response.json == {'url': 'https://example.com/dog.jpg'}

# 8. Teste positivo para app.py: formato JSON correto
# Verifica se a resposta da rota /dog tem o content-type correto
def test_get_dog_json_format():
    with patch('app.app.get_dog_image_url', return_value='https://example.com/dog.jpg'):
        with app.test_client() as client:
            response = client.get('/dog')
            assert response.content_type == 'application/json'

# 9. Teste positivo para app.py: URL válida na resposta
# Verifica se a URL retornada na resposta JSON é válida (começa com https://)
def test_get_dog_valid_url():
    with patch('app.app.get_dog_image_url', return_value='https://example.com/dog.jpg'):
        with app.test_client() as client:
            response = client.get('/dog')
            data = response.get_json()
            assert 'url' in data
            assert data['url'].startswith('https://')

# 10. Teste positivo para app.py: estrutura de resposta correta
# Verifica se a resposta JSON é um dicionário com exatamente uma chave 'url'
def test_get_dog_response_structure():
    with patch('app.app.get_dog_image_url', return_value='https://example.com/dog.jpg'):
        with app.test_client() as client:
            response = client.get('/dog')
            data = response.get_json()
            assert isinstance(data, dict)
            assert len(data) == 1

# ===========================================
# TESTES NEGATIVOS (11-20)
# ===========================================

# 11. Teste negativo para cachorro.py: resposta vazia da API
# Verifica se a função retorna None quando a API retorna lista vazia
def test_get_dog_image_url_empty_response():
    mock_response = MagicMock()
    mock_response.json.return_value = []
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result is None

# 12. Teste negativo para cachorro.py: resposta sem chave 'url'
# Verifica se a função retorna None quando o JSON não contém a chave 'url'
def test_get_dog_image_url_no_url_key():
    mock_response = MagicMock()
    mock_response.json.return_value = [{'id': 1}]
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result is None

# 13. Teste negativo para cachorro.py: erro de conexão
# Verifica se a função retorna None quando há erro genérico na requisição
def test_get_dog_image_url_request_exception():
    with patch('cachorro.requests.get', side_effect=Exception('Connection error')):
        result = get_dog_image_url()
        assert result is None

# 14. Teste negativo para cachorro.py: JSON inválido
# Verifica se a função retorna None quando a resposta não é um JSON válido
def test_get_dog_image_url_invalid_json():
    mock_response = MagicMock()
    mock_response.json.side_effect = ValueError('Invalid JSON')
    with patch('cachorro.requests.get', return_value=mock_response):
        result = get_dog_image_url()
        assert result is None

# 15. Teste negativo para cachorro.py: timeout na requisição
# Verifica se a função retorna None quando a requisição excede o tempo limite
def test_get_dog_image_url_timeout():
    with patch('cachorro.requests.get', side_effect=requests.exceptions.Timeout):
        result = get_dog_image_url()
        assert result is None

# 16. Teste negativo para app.py: função cachorro retorna None
# Verifica se a rota /dog retorna JSON com url: null quando a função retorna None
def test_get_dog_none():
    with patch('app.app.get_dog_image_url', return_value=None):
        with app.test_client() as client:
            response = client.get('/dog')
            assert response.status_code == 200
            assert response.json == {'url': None}

# 17. Teste negativo para app.py: exceção na função cachorro
# Verifica se a rota /dog trata exceções da função cachorro retornando url: null
def test_get_dog_exception():
    with patch('app.app.get_dog_image_url', side_effect=Exception('Error')):
        with app.test_client() as client:
            response = client.get('/dog')
            assert response.status_code == 200
            assert response.json == {'url': None}

# 18. Teste negativo para app.py: rota inexistente
# Verifica se rotas não definidas retornam status 404
def test_invalid_route():
    with app.test_client() as client:
        response = client.get('/invalid')
        assert response.status_code == 404

# 19. Teste negativo para app.py: função retorna string vazia
# Verifica se a rota /dog aceita e retorna string vazia quando a função retorna ''
def test_get_dog_with_empty_string():
    with patch('app.app.get_dog_image_url', return_value=''):
        with app.test_client() as client:
            response = client.get('/dog')
            assert response.status_code == 200
            assert response.json == {'url': ''}

# 20. Teste negativo para app.py: método HTTP não permitido
# Verifica se a rota /dog retorna 405 para métodos não suportados (POST)
def test_post_method_not_allowed():
    with app.test_client() as client:
        response = client.post('/dog')
        assert response.status_code == 405
