from pydub import AudioSegment
import pygame
import numpy as np

# Configurações
FPS = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Inicialização do Pygame
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Visualização de Música")

# Carrega a música
music_path = input("Digite o caminho da música (MP3): ")
song = AudioSegment.from_mp3(music_path)

# Converte a música em um array numpy
song_array = np.array(song.get_array_of_samples())

# Normaliza os valores entre -1 e 1
song_array = song_array / np.max(np.abs(song_array))

# Frequência de amostragem da música
sample_rate = song.frame_rate

# Divide a música em quadros para análise
frame_size = int(sample_rate / FPS)
num_frames = int(len(song_array) / frame_size)

# Notas para detecção (Frequências em Hz)
notes = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88
}

# Cores correspondentes às notas
colors = {
    "C": (255, 0, 0),    # Vermelho
    "C#": (255, 165, 0), # Laranja
    "D": (255, 255, 0),  # Amarelo
    "D#": (0, 255, 0),   # Verde
    "E": (0, 255, 255),  # Ciano
    "F": (0, 0, 255),    # Azul
    "F#": (75, 0, 130),  # Índigo
    "G": (143, 0, 255),  # Roxo
    "G#": (128, 0, 128), # Roxo escuro
    "A": (255, 0, 255),  # Magenta
    "A#": (255, 192, 203), # Rosa claro
    "B": (255, 105, 180)  # Rosa
}

# Loop principal
frame = 0
running = True
while running:
    # Eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtém o quadro atual da música
    current_frame = song_array[frame * frame_size: (frame + 1) * frame_size]

    # Calcula a transformada de Fourier rápida (FFT) do quadro
    fft = np.abs(np.fft.fft(current_frame))

    # Encontra as quatro frequências dominantes
    sorted_indices = np.argsort(fft)[::-1][:4]
    sorted_frequencies = np.fft.fftfreq(frame_size)[:len(sorted_indices)]
    dominant_frequencies = sorted_frequencies[sorted_indices]

    # Verifica quais notas estão próximas das frequências dominantes
    detected_notes = []
    for frequency in dominant_frequencies:
        closest_note = min(notes, key=lambda x: abs(notes[x] - frequency))
        detected_notes.append(closest_note)

    # Preenche a tela com as cores correspondentes às notas detectadas
    color_list = [colors.get(note, (255, 255, 255)) for note in detected_notes]
    window.fill((255, 255, 255))  # Preenche a tela com branco
    for i, color in enumerate(color_list):
        x = (WINDOW_WIDTH // 4) * (i + 1)
        pygame.draw.rect(window, color, (x - 50, WINDOW_HEIGHT // 2 - 50, 100, 100))

    # Atualiza a tela
    pygame.display.flip()

    # Avança para o próximo quadro
    frame = (frame + 1) % num_frames

    # Define a taxa de quadros por segundo
    clock.tick(FPS)

# Encerra o Pygame
pygame.quit()
