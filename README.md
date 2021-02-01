# Youtube_analysis

Este projeto tem como objetivo capturar comentários de vídeos do YouTube e analisar eles. Para rodar o projeto você precisa seguir as seguintes etapas:

## 1 - Clonar o repositório.

## 2 - Instalar as libs necessarias.
    pip install requirements.txt

## 3 - Baixar o chrome driver no [link](https://chromedriver.chromium.org/downloads).

## 4 - Copiar o caminho absoluto do Chrome Driver e alterar a variavel "chrome_driver" no arquivo "youtube_crawler.py". Em caso de dúvida ler a documentação do chrome driver.
    chrome_driver = caminho/do/seu/chrome_driver

## 5 - Rodar o código "setup.py" passando o nome do canal que será analizado (recomendo que o nome não tenha espaços e nem caracteres especiais).
    python3 setup.py nome_do_canal

## 6 - Rodar o código "main.py" passando o nome do canal, mesmo usado no comando acima, e a url do canal
    python3 main.py nome_do_canal https://www.youtube.com/c/nome_do_canal/videos

## Exemplo:
    git clone git@github.com:gomesgui06/youtube_analysis.git
    cd youtube_crawler
    pip install requirements
    python3 setup.py manual_do_mundo
    python3 main.py manual_do_mundo https://www.youtube.com/c/manual_do_mundo/videos

>>>>>>> master
