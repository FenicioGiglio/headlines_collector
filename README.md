# G1 News Scraper 📰

Este é um script em Python que automatiza a coleta das principais manchetes do portal de notícias G1 (g1.globo.com). Ele utiliza as bibliotecas **Selenium** e **`undetected-chromedriver`** para navegar no site, extrair os títulos e os links das notícias em destaque e exibi-los no console.

***

## ✨ Funcionalidades

-   **Navegação Automatizada**: Acessa a página inicial do G1 de forma autônoma.
-   **Extração de Dados**: Coleta o título e o link correspondente de cada manchete principal.
-   **Anti-Detecção**: Utiliza `undetected-chromedriver` para emular um navegador comum, dificultando a detecção como um bot.
-   **Modo Headless**: É executado em segundo plano (`--headless=new`), sem abrir uma janela visível do navegador, otimizando o consumo de recursos.
-   **Uso de Perfil de Usuário**: Configurado para usar um perfil específico do Google Chrome, o que pode ajudar a manter sessões, cookies e configurações preexistentes.

***

## 🔧 Requisitos

Para executar este script, você precisará ter o **Python 3** e o **Google Chrome** instalados. Além disso, as seguintes bibliotecas Python são necessárias:

-   `selenium`
-   `undetected-chromedriver`

***

## ⚙️ Instalação e Configuração

1.  **Clone este repositório ou baixe o arquivo `.py`** para o seu computador.

2.  **Instale as dependências** necessárias através do pip:
    ```bash
    pip install selenium undetected-chromedriver
    ```

3.  **Configure o seu perfil do Chrome (Passo Essencial)**:
    O script precisa saber onde os dados do seu perfil do Google Chrome estão armazenados. Você **precisa** alterar a variável `user_data_path` no código.

    -   Encontre esta linha no script:
        ```python
        user_data_path = r"C:\Users\fenic\AppData\Local\Google\Chrome\User Data\Default"
        ```
    -   **Substitua o caminho** pelo local correspondente no seu sistema operacional:
        -   **Windows**: `C:\Users\<SeuNomeDeUsuario>\AppData\Local\Google\Chrome\User Data` (Você pode digitar `%LOCALAPPDATA%` na barra de endereço do Explorer para encontrar a pasta `AppData`).
        -   **macOS**: `~/Library/Application Support/Google/Chrome`
        -   **Linux**: `~/.config/google-chrome`

    -   O nome do perfil (`profile_name`) geralmente é `"Default"`, a menos que você utilize múltiplos perfis no Chrome.

***

## 🚀 Como Usar

Após configurar corretamente o caminho do perfil, abra um terminal ou prompt de comando, navegue até a pasta onde o script está salvo e execute o seguinte comando:

```bash
python nome_do_seu_script.py
