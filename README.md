# README

## Sobre
Este projeto contém o arquivo `cachorro.py`, que obtém uma URL de imagem aleatória de cachorro ao ser executado. A URL da imagem é obtida da [Dog CEO API](https://dog.ceo/).

## Como funciona

A forma recomendada de usar este projeto é pela interface web:

- A aplicação web Flask oferece uma interface simples no navegador.
- Ao acessar a rota `/dog` (clicando em um botão ou similar na interface), o backend executa o `cachorro.py` para obter uma nova URL de imagem de cachorro.
- A URL da imagem é retornada para o frontend como JSON, que pode então exibir a imagem diretamente no navegador.

Assim, você pode obter imagens aleatórias de cachorro diretamente pelo navegador de forma prática e intuitiva.

## Requisitos
- Python 3
- Os seguintes pacotes (listados no `requirements.txt`):
  - requests
  - Flask 

## Como usar

### Rodando pela Interface Web
Você também pode usar a interface web disponível na pasta `app`:

1. Instale as dependências necessárias:
  ```bash
  pip install -r requirements.txt
  ```
2. Inicie a aplicação web:
  ```bash
  python app/app.py
  ```
3. Abra o navegador e acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) para usar a interface.

### Executando os Testes
O projeto inclui testes abrangentes em `tests/test_comprehensive.py` para validar o funcionamento correto:

1. Instale as dependências de teste:
  ```bash
  pip install -r requirements.txt
  ```
2. Execute os testes:
  ```bash
  python -m pytest tests/test_comprehensive.py -v
  ```

Os testes cobrem casos positivos e negativos, incluindo tratamento de erros, para garantir a robustez da aplicação.

## Correções e Atualizações

Na branch `dev/acertando-erros-assump`, vários problemas foram identificados e corrigidos com base nas falhas dos testes:

1. **Implementação do cachorro.py**: A função `get_dog_image_url()` não estava implementada corretamente e retornava um valor incorreto (12345). Foi atualizada para:
   - Obter uma URL de imagem aleatória de cachorro da Dog CEO API (https://dog.ceo/api/breeds/image/random).
   - Lidar com vários formatos de resposta (lista de dicionários ou dicionário único).
   - Tratar adequadamente exceções como erros de conexão, timeouts e JSON inválido, retornando `None` nesses casos.
   - Incluir um timeout de 10 segundos para a requisição.

2. **Correções nas rotas do app.py**: 
   - A rota `/` estava retornando erro 404 com conteúdo incorreto. Foi corrigida para renderizar o template `index.html` corretamente.
   - A rota `/dog` estava retornando erro 500 com string 'erro'. Foi atualizada para:
     - Chamar `get_dog_image_url()` e retornar a URL no formato JSON (`{'url': url}`).
     - Tratar exceções de forma elegante, retornando `{'url': None}` com status 200.

3. **Compatibilidade com Testes**: A implementação agora lida corretamente com as respostas mockadas nos testes, garantindo que todos os casos de teste positivos e negativos passem.

Essas mudanças garantem que a aplicação funcione conforme o esperado, obtendo e exibindo imagens aleatórias de cachorro via interface web, e todos os testes passam com sucesso.

---

## Nota sobre resolução de conflito

Na branch `conflito`, ocorreu um conflito de merge no arquivo `app/app.py` sobre o valor retornado pela rota `/dog`. O conflito foi resolvido restaurando a lógica correta: a rota retorna a URL gerada pelo `cachorro.py`, conforme esperado pela interface.

---
A interface permite obter uma imagem aleatória de cachorro diretamente pelo navegador.

