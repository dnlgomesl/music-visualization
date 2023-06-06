import pygame
import numpy as np
import soundfile as sf
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Configurações de cores
BLACK = (0, 0, 0)

# Carrega a música
music_file = "C:/Users/dev/Documents/GitHub/music-visualization/musicas/Drive.mp3"
pygame.mixer.music.load(music_file)

# Reproduz a música em loop
pygame.mixer.music.play(-1)

# Obtém informações da música
data, sample_rate = sf.read(music_file)

# Define as notas e cores correspondentes
notes = {
    "C": (255, 0, 0),    # Vermelho
    "C#": (255, 165, 0), # Laranja
    "D": (255, 255, 0),  # Amarelo
    "D#": (0, 128, 0),   # Verde Escuro
    "E": (0, 0, 255),    # Azul
    "F": (75, 0, 130),   # Roxo
    "F#": (238, 130, 238), # Violeta
    "G": (255, 0, 255),  # Magenta
    "G#": (255, 192, 203), # Rosa Claro
    "A": (255, 255, 255),# Branco
    "A#": (128, 128, 128), # Cinza
    "B": (128, 0, 0)     # Marrom
}

# Configura a janela
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Visualização de Notas Musicais")

# Função para obter a nota mais próxima da frequência
def get_closest_note_frequency(frequency):
    closest_note = min(notes, key=lambda x: abs(notes[x] - frequency))
    return notes[closest_note]

# Loop principal
clock = pygame.time.Clock()
running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtém o quadro atual
    current_frame = data[frame * sample_rate: (frame + 1) * sample_rate, 0]

    # Calcula a transformada de Fourier para obter as frequências dominantes
    spectrum = np.fft.fft(current_frame)
    frequencies = np.fft.fftfreq(sample_rate, d=1 / sample_rate)

    # Filtra as frequências positivas
    positive_frequencies = frequencies[:sample_rate // 2]
    positive_spectrum = spectrum[:sample_rate // 2]

    # Obtém a frequência com maior amplitude
    max_amplitude_index = np.argmax(np.abs(positive_spectrum))
    dominant_frequency = positive_frequencies[max_amplitude_index]

    # Obtém a nota mais próxima da frequência dominante
    closest_note_color = get_closest_note_frequency(dominant_frequency)

    # Preenche a janela com a cor da nota mais próxima
    window.fill(closest_note_color)

    # Atualiza a janela
    pygame.display.update()

    # Define a taxa de quadros por segundo
    clock.tick(60)

    # Incrementa o quadro
    frame = (frame + 1) % (len(data) // sample_rate)

# Encerra o Pygame
pygame.quit()
sys.exit()
