# Music Visualization

Este projeto, é um Projeto da disciplina Computação e Música que permite visualizar notas musicais em cores na tela. Cada nota é mapeada para uma cor correspondente e exibida em retângulos na tela.

## Pré-requisitos

- Python 3.9 (ou versão posterior) instalado

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```shell
   git clone https://github.com/dnlgomesl/music-visualization.git
   ```

2. Navegue até o diretório do projeto:

   ```shell
   cd music-visualization
   ```

3. Instale as dependências do projeto:

   - Usando o Makefile:

     ```shell
     make install
     ```

   - Ou, manualmente, execute o seguinte comando:

     ```shell
     pip install -r requirements.txt
     ```

## Execução

1. No diretório do projeto, execute o seguinte comando para iniciar a aplicação:

   - Usando o Makefile:

     ```shell
     make run
     ```

   - Ou, manualmente, execute o seguinte comando:

     ```shell
     python music_visualization.py
     ```

2. Insira o caminho do arquivo de música MP3 quando solicitado.

3. A visualização das notas musicais em cores será exibida na tela.

## Limpeza

- Para remover os arquivos gerados pelo projeto, execute o seguinte comando:

  - Usando o Makefile:

    ```shell
    make clean
    ```

  - Ou, manualmente, execute os seguintes comandos:

    ```shell
    rm -rf __pycache__
    ```