# Web Crawler GitHub Tasks

[Read in English](README.md)

## Descrição

Este projeto automatiza o processo de criação de tarefas nos Projetos do GitHub usando Selenium. Ele lê tarefas predefinidas de um arquivo de dados e usa Selenium para fazer login no GitHub e adicionar essas tarefas a um projeto específico.

## Estrutura do Projeto

```plaintext
[project-root]/
├── .gitignore
├── README.md
├── README-ptbr.md
├── config.py
├── main.py
├── requirements.txt
├── driver/
│   ├── chromedriver
│   └── chromedriver.exe
├── services/
│   ├── selenium_service.py
│   └── __init__.py
├── data/
│   ├── cards.py
│   └── __init__.py
```

## Configuração

### Instalação

1. **Clone o repositório:**
    
    ```bash
    git clone https://github.com/ThiagoSchumann/web-crawler-github-tasks
    cd web-crawler-github-tasks
    ```
    
2. **Instale os pacotes necessários:**
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Baixe o WebDriver:**
    
    Baixe o WebDriver apropriado para seu navegador e sistema operacional, e coloque-o no diretório `driver/`. Atualize o caminho em `config.py` se necessário.

### Configuração

1. **Crie um arquivo `.env`:**
    
    Crie um arquivo `.env` no diretório raiz com suas variáveis de ambiente necessárias:
    
    ```env
    EMAIL=seu_email_github
    PASSWORD=sua_senha_github
    ```
    
2. **Atualize `config.py`:**
    
    Certifique-se de que `config.py` tem os caminhos e URLs corretos:
    
    ```python
    from decouple import config

    EMAIL = config("EMAIL")
    PASSWORD = config("PASSWORD")
    DRIVER_PATH = "driver/chromedriver.exe"  # Ajuste este caminho se estiver usando um SO diferente
    GITHUB_LOGIN_URL = "https://github.com/login"
    PROJECT_URL = "https://github.com/users/ThiagoSchumann/projects/10"
    ```

## Uso

1. **Execute o script principal:**
    
    ```bash
    python main.py
    ```
    
2. **Tarefas Automatizadas:**
    
    O script fará login no GitHub, navegará para o projeto especificado e adicionará tarefas definidas em `data/cards.py`.

## Arquivos e Diretórios Importantes

- **main.py**: O script principal que executa a automação do Selenium.
- **config.py**: Carrega variáveis de ambiente e configurações.
- **services/selenium_service.py**: Contém a lógica do Selenium para interagir com o GitHub.
- **data/cards.py**: Contém os dados dos cards a serem usados no projeto.

## Funcionalidades

- **Login Automatizado**: Faz login no GitHub usando as credenciais fornecidas.
- **Adição de Tarefas**: Adiciona tarefas predefinidas a um projeto específico do GitHub.

## Tecnologias Utilizadas

- **Backend**: Python, Selenium
- **Gerenciamento de Configuração**: Python-Decouple

## Contribuindo

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para suporte ou feedback, por favor, entre em contato pelo email [thiagoarturschumann@gmail.com](mailto:thiagoarturschumann@gmail.com).