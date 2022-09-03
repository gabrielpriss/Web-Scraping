# Web Scraping com Python, projeto feito durante o curso da Trybe

<details>
  <summary><strong>Objetivo</strong></summary><br />

  O projeto tem como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias raspadas estão no Blog da Trybe: https://blog.betrybe.com.
  Essas notícias são salvas no banco de dados utilizando as funções python no módulo `database.py`
  
  ---

  <strong>MongoDB</strong>

  É utilizado um banco de dados chamado `tech_news`.
  As notícias são armazenadas em uma coleção chamada `news`.

  Para rodar o MongoDB via Docker:
  <code>docker-compose up -d mongodb</code> no terminal. 
  Configurações do mongo com o docker estão no arquivo `docker-compose.yml`

  O mongoDB utilizará por padrão a porta 27017.

</details>

---
<details>
  <summary><strong> Requisitos</strong></summary>

  ## 1 - Função `fetch`
  local: `tech_news/scraper.py`

  Esta função é responsável por fazer a requisição HTTP ao site e obter o conteúdo HTML.

  - Utiliza um Rate Limit pois pode ser utilizada várias vezes em sucessão
  - Deve receber uma URL
  - Faz uma requisição HTTP `get` para a URL utilizando a função `requests.get`
  - Retorna o conteúdo HTML da resposta.
  - Caso a requisição seja bem sucedida com `Status Code 200: OK`, retorna seu conteúdo de texto;
  - Caso a resposta tenha o código de status diferente de `200`, retorna `None`;
  - Caso a requisição não receba resposta em até 3 segundos, ela é abandonada.

  📌 é definido o _header_ `user-agent` para que a raspagem do blog funcione corretamente. Para isso, o valor `"Fake user-agent"` recebe:

  ```python
  { "user-agent": "Fake user-agent" }
  ```

  ## 2 - Função `scrape_novidades`
  local: `tech_news/scraper.py`

  Esta função faz o scrape da página Novidades (https://blog.betrybe.com) para obter as URLs das páginas de notícias.

  - Recebe uma string com o conteúdo HTML da página inicial do blog
  - Faz o scrape do conteúdo recebido para obter uma lista contendo as URLs das notícias listadas.
  - A função retorna esta lista.
  - Caso não encontre nenhuma URL de notícia, a função retorna uma lista vazia.

  ## 3 - Função `scrape_next_page_link`
  local: `tech_news/scraper.py`

  Precisa do link da próxima página. Esta função é responsável por fazer o scrape deste link.

  - Recebe como parâmetro uma `string` contendo o conteúdo HTML retirado pela função fetch
  - Faz o scrape deste HTML para obter a URL da próxima página.
  - Retorna a URL obtida.
  - Caso não encontre o link da próxima página, função retorna `None`

  ## 4 - Função `scrape_noticia`
  local: `tech_news/scraper.py`

  - Recebe como parâmetro o conteúdo HTML da página de uma notícia
  - Busca as informações das notícias e preenche um dicionário:
    - `url` - link para acesso da notícia.
    - `title` - título da notícia.
    - `timestamp` - data da notícia, no formato `dd/mm/AAAA`.
    - `writer` - nome da pessoa autora da notícia.
    - `comments_count` - número de comentários que a notícia recebeu.
      - Se a informação não for encontrada, salve este atributo como `0` (zero)
    - `summary` - o primeiro parágrafo da notícia.
    - `tags` - lista contendo tags da notícia.
    - `category` - categoria da notícia.

  ## 5 - Função `get_tech_news`
  local: `tech_news/scraper.py`

  Aplicação de todas as funções anterioes.

  - Receber como parâmetro um número inteiro `n` e buscar as últimas `n` notícias.
  - Funções `fetch`, `scrape_novidades`, `scrape_next_page_link` e `scrape_noticia` são utilizadas para buscar as notícias e processar o conteúdo.
  - As notícias buscadas são inseridas no MongoDB; utiliza as funções do diretório `tech_news/database.py`
  - Insere as notícias no banco, e retorna as mesmas.


  ## 6 - Função `search_by_title`
  local: `tech_news/analyzer/search_engine.py`

  Faz buscas por título.

  - Recebe uma string com um título de notícia
  - Busca as notícias do banco de dados por título
  - Retorna uma lista de tuplas com as notícias encontradas na busca. 
  Exemplo: 
  ```python
  [
    ("Título1_aqui", "url1_aqui"),
    ("Título2_aqui", "url2_aqui"),
  ]
  ```
  - A busca é _case insensitive_
  - Caso nenhuma notícia seja encontrada, retorna uma lista vazia.

  📌 Para acesso ao banco de dados utiliza `db` definido no módulo `tech_news/database.py`.

  ## 7 - Função `search_by_date`
  local: `tech_news/analyzer/search_engine.py`

  Busca as notícias do banco de dados por data.

  - Recebe como parâmetro uma data no formato ISO `AAAA-mm-dd`
  - Tem retorno no mesmo formato do requisito anterior.
  - Caso a data seja inválida, uma exceção `ValueError` é lançada com a mensagem `Data inválida`.
  - Caso nenhuma notícia seja encontrada, retorna uma lista vazia.

  ## 8 - Função `search_by_tag`,
  local: `tech_news/analyzer/search_engine.py`

  Busca as notícias por tag.

  - Recebe como parâmetro o nome da tag completo..
  - A função deve ter retorno no mesmo formato do requisito anterior.
  - Caso nenhuma notícia seja encontrada, retorna uma lista vazia.
  - A busca é_case insensitive_

  ## 9 - Função `search_by_category`
  local: `tech_news/analyzer/search_engine.py`

  Busca as notícias por categoria.

  - Recebe como parâmetro o nome da categoria completo.
  - Tem como retorno o mesmo formato do requisito anterior.
  - Caso nenhuma notícia seja encontrada, retorna uma lista vazia.
  - A busca é _case insensitive_
</details>
