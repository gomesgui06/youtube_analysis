# Youtube_analysis

Este projeto tem como objetivo capturar comentários de vídeos do YouTube e analisar eles. Para rodar o projeto você precisa seguir as seguintes etapas:

## 1 - Clonar o repositório.

## 2 - Virtualenv
    virtualenv venv
    source venv/bin/activate

## 3 - Instalar as libs necessarias.
    pip install requirements.txt

## 4 - Instalar o postgres
    https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198

## 5 - Baixar o chrome driver no [link](https://chromedriver.chromium.org/downloads).

## 6 - Copiar o caminho absoluto do Chrome Driver e alterar a variavel "chrome_driver" no arquivo "youtube_crawler.py". Em caso de dúvida ler a documentação do chrome driver.
    chrome_driver = caminho/do/seu/chrome_driver

## 7 - Rodar o código "setup.py" passando o nome do canal que será analizado (recomendo que o nome não tenha espaços e nem caracteres especiais).
    python3 setup.py nome_do_canal

## 8 - Rodar o código "main.py" passando o nome do canal, mesmo usado no comando acima, e a url do canal
    python3 main.py nome_do_canal https://www.youtube.com/c/nome_do_canal/videos

## Exemplo:
    git clone git@github.com:gomesgui06/youtube_analysis.git
    cd youtube_crawler
    pip install requirements
    python3 setup.py manual_do_mundo
    python3 main.py manual_do_mundo https://www.youtube.com/c/manual_do_mundo/videos

## comandos:
    install requirements: `python3 -m pip install -r requirements.txt`
    
    run postgres: docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

    postgres: \l (lista de metabase)
              \c {nome_do_metabase} (Para entrar no metabase)
              \dt+ (lista as tabelas que existem dentro do metabase)

