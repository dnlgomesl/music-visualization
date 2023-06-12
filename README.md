# Visualização de Notas Musicais

Este é um programa em Python que visualiza notas musicais a partir de um arquivo de música. A idéia seria simular um jogo de luz de acordo com o reconhecimento das notas presente na música.

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/dnlgomesl/music-visualization.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd music-visualization
   ```

3. Crie e ative um ambiente virtual (opcional):

   ```bash
   python -m venv venv
   source env/bin/activate
   ```

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Crie um arquivo `.env` com base no `.env-example`:

   ```bash
   cp .env-example .env
   ```

   Em seguida, edite o arquivo `.env` e insira o caminho correto para o arquivo de música no valor da variável `MUSIC_PATH`.

## Uso

Execute o programa com o seguinte comando:

```bash
python main.py
```

Isso iniciará a visualização das notas musicais de acordo com o arquivo de música definido no arquivo `.env`.