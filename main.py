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
WHITE = (255, 255, 255)

# Carrega a música
music_file = "C:/Users/dev/Documents/GitHub/music-visualization/musicas/Drive.mp3"
pygame.mixer.music.load(music_file)

# Reproduz a música em loop
pygame.mixer.music.play(-1)

# Obtém informações da música
data, sample_rate = sf.read(music_file)

# Define as notas e cores correspondentes
notes = {
    "C": np.array([255, 0, 0]),    # Vermelho
    "C#": np.array([255, 165, 0]), # Laranja
    "D": np.array([255, 255, 0]),  # Amarelo
    "D#": np.array([0, 128, 0]),   # Verde Escuro
    "E": np.array([0, 0, 255]),    # Azul
    "F": np.array([75, 0, 130]),   # Roxo
    "F#": np.array([238, 130, 238]), # Violeta
    "G": np.array([255, 0, 255]),  # Magenta
    "G#": np.array([255, 192, 203]), # Rosa Claro
    "A": np.array([255, 255, 255]),# Branco
    "A#": np.array([128, 128, 128]), # Cinza
    "B": np.array([128, 0, 0])     # Marrom
}

# Configura a janela
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Visualização de Notas Musicais")

# Configura a fonte de texto
font = pygame.font.Font(None, 36)

# Função para calcular a diferença entre cores RGB
def color_difference(color1, color2):
    return np.sqrt(np.sum((color2 - color1) ** 2))

# Função para obter a nota mais próxima da frequência
def get_closest_note_frequency(frequency):
    closest_note = min(notes, key=lambda x: color_difference(notes[x], frequency))
    return closest_note, notes[closest_note]

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
    closest_note, closest_note_color = get_closest_note_frequency(dominant_frequency)

    # Preenche a janela com a cor da nota mais próxima
    window.fill(closest_note_color)

    # Renderiza o texto da nota na janela
    text_surface = font.render(closest_note, True, WHITE)
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    window.blit(text_surface, text_rect)

    # Atualiza a janela
    pygame.display.update()

    # Define a taxa de quadros por segundo
    clock.tick(60)

    # Incrementa o quadro
    frame = (frame + 1) % (len(data) // sample_rate)
    
    # Delay de 500 milissegundos
    pygame.time.delay(100)

# Encerra o Pygame
pygame.quit()
sys.exit()
