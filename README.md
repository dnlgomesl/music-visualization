# Visualização de Notas Musicais

Este é um programa em Python que visualiza notas musicais a partir de um arquivo de música. A idéia seria simular um jogo de luz de acordo com o reconhecimento das notas presente na música.

## Descrição
O Visualizador de Notas Musicais é um programa Python que combina música e cores para criar uma experiência audiovisual imersiva. Inspirado no conceito de sinestesia, onde diferentes sentidos se cruzam, o programa realiza o processo inverso do que o Nathan realizou em seu projeto 'Música Colorida'. Em vez de converter cores em notas musicais, o Visualizador de Notas Musicais analisa uma música e gera uma exibição visual em tempo real, onde cada nota é representada por uma cor correspondente. Ao reproduzir a música, o programa cria uma interação visual sincronizada, trazendo uma dimensão extra à experiência sonora. Os espectadores podem se envolver em um jogo de luzes, mergulhando em um ambiente imersivo onde as notas musicais ganham vida por meio de cores vibrantes. O programa é altamente personalizável, permitindo que os usuários explorem diferentes músicas e criem suas próprias combinações de cores e notas para uma experiência única a cada reprodução.

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

## Observações
A música presente na pasta `músicas` do projeto é uma música sem copyrigth, disponível no [link](https://soundcloud.com/hothammusic/summertime]). Para observar o funcionamento assista ao [vídeo de demonstração](/demonstracao/demo.mkv).
