# Último Dado - README

Este é um projeto simples em Django que demonstra como exibir o último dado de um modelo utilizando o Django REST Framework e templates HTML.

## Requisitos

- Python (versão 3.x)
- Django (versão 3.x)
- Django REST Framework

## Instalação

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/seu_usuario/seu_projeto.git
```

2. Navegue até o diretório do projeto:

```
cd seu_projeto
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Execute as migrações do Django para criar o banco de dados:

```
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

6. Acesse o projeto no seu navegador em `http://127.0.0.1:8000/ultimo_dado/`.

## Uso

1. Acesse a URL `http://127.0.0.1:8000/ultimo_dado/` para visualizar o último dado do modelo `Dados`.
2. Acesse a URL `http://127.0.0.1:8000/historico_dados/` para visualizar o histórico de todos os dados do modelo `Dados`.
3. Para adicionar novos dados, envie uma requisição POST para `http://127.0.0.1:8000/dados/`. Os dados devem ser enviados no corpo da requisição no formato JSON.
4. Para atualizar ou excluir um dado específico pelo seu ID, envie uma requisição PUT ou DELETE para `http://127.0.0.1:8000/dados/{id}/`, onde `{id}` é o ID do dado que você deseja atualizar ou excluir.

## Estrutura do Projeto

- `meu_projeto/`: Diretório raiz do projeto Django.
  - `meu_app/`: Aplicativo Django contendo o modelo `Dados` e as views para exibir o último dado e o histórico de dados.
    - `templates/`: Diretório para armazenar os arquivos de template HTML.
      - `ultimo_dado.html`: Template HTML para exibir o último dado.
      - `historico_dados.html`: Template HTML para exibir o histórico de dados.
    - `views.py`: Arquivo contendo as views Django para retornar o último dado e o histórico de dados.
  - `meu_projeto/`: Configurações do projeto Django.
    - `urls.py`: URLs do projeto.
  - `manage.py`: Script de gerenciamento do Django.

## Como Funciona

1. O modelo `Dados` possui campos como `sensor`, `botao`, `liga_robo`, `reset_contador` e `valor_contagem`.
2. A view `UltimoDado` é responsável por recuperar o último dado do modelo `Dados`.
3. A view `HistoricoDados` é responsável por recuperar todos os dados do modelo `Dados`.
4. Os templates HTML `ultimo_dado.html` e `historico_dados.html` exibem os dados recuperados, mostrando bolinhas verdes para valores verdadeiros e bolinhas vermelhas para valores falsos.

## Customização

Você pode personalizar o estilo dos templates HTML ou adicionar mais campos ao modelo `Dados` conforme necessário. Sinta-se à vontade para modificar o projeto de acordo com suas necessidades.
