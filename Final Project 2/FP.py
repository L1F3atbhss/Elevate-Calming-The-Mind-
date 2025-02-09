import pygame
import sys
import time
import os
from PIL import Image

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 1300
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elevate - Calming the Mind")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (180, 215, 230)
RED = (250, 0, 0)
BLUE = (0, 0, 250)
SKYBLUE = (135, 206, 235)
CORNFLOWERBLUE = (154, 206, 235)
BABYBLUE = (137, 207, 240)
DODGERBLUE = (89, 174, 254)

# this is for loading the gif on DS2
#rn this is not used

def gif2img(file, name):

    cachedir = "./cache/" + name + "/"

    if True: # not os.path.exists(cachedir):

        noerr = True
        frameno = 1

        im = Image.open(file)
        im.convert("RGBA")
        im.save(cachedir + name + str(frameno) + ".png")

        while noerr:

            print("noerr")

            frameno += 1

            try: 
                im.seek(im.tell()+1)
                im.convert("RGBA")
                im.save(cachedir + name + str(frameno) + ".png")

            except:
                noerr = False
    
    # return the files from the cache as a list of images

# gif2img("./4-7-8 Breathing.gif", "b")

# Fonts
font = pygame.font.Font(None, 50)

# Utility to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Button class
class Button:
    def __init__(self, x, y, width, height, color, text_color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text_color = text_color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, font, self.text_color, surface, self.rect.centerx, self.rect.centery)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
# Main Menu
def main_menu():
    while True:
        screen.fill(WHITE)
        pygame.display.set_caption("Elevate - Calming the Mind")

        # Mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Buttons (X, Y with, Hight)
        relax_button = Button(100, 40, 450, 550, LIGHTBLUE, BLACK, "De-Stressing Exercises", action=M1)
        sound_button = Button(750, 40, 450, 550, LIGHTBLUE, BLACK, "library Of Calming Sounds", action=M2)
        quit_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Quit", action=sys.exit)

        # Draw buttons
        relax_button.draw(screen)
        quit_button.draw(screen)
        sound_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if relax_button.is_clicked(mouse_pos):
                    relax_button.action()
                if quit_button.is_clicked(mouse_pos):
                    quit_button.action()
                if sound_button.is_clicked(mouse_pos):
                    sound_button.action()
                    
        pygame.display.update()

#menu 1 (De-Stressing Exercises)
def M1():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - De-Stressing Exercises")
        screen.fill(WHITE)

        # Buttons (X, Y with, Hight)
        _1_button = Button(100, 40, 450, 550, CORNFLOWERBLUE, BLACK, "Breathing Exercises", action=MDS1)
        _2_button = Button(750, 40, 450, 550, CORNFLOWERBLUE, BLACK, "Gratitude Practice", action=MDS2)
        # Back button
        back_button = Button(920, 620, 300, 100, CORNFLOWERBLUE, BLACK, "Back", action=main_menu)

        # Draw buttons
        _1_button.draw(screen)
        _2_button.draw(screen)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if _1_button.is_clicked(mouse_pos):
                    _1_button.action()
                if _2_button.is_clicked(mouse_pos):
                    _2_button.action()
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                    
        pygame.display.update()

#library Of Calming Sounds
def M2():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - library Of Calming Sounds")
        screen.fill(WHITE)

        # Buttons (X, Y with, Hight)
        _1_button = Button(100, 20, 450, 280, SKYBLUE, BLACK, "Nature sounds", action=S1)
        _3_button = Button(100, 330, 450, 280, SKYBLUE, BLACK, "White Noise", action=S2)
        _2_button = Button(625, 20, 450, 280, SKYBLUE, BLACK, "Seasonal Ambience", action=S3)
        _4_button = Button(625, 330, 450, 280, SKYBLUE, BLACK, "Lullabies", action=S4)

        # Back button
        back_button = Button(920, 620, 300, 100, SKYBLUE, BLACK, "Back", action=main_menu)

        # Draw buttons
        _1_button.draw(screen)
        _2_button.draw(screen)
        _3_button.draw(screen)
        _4_button.draw(screen)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if _1_button.is_clicked(mouse_pos):
                    _1_button.action()
                if _2_button.is_clicked(mouse_pos):
                    _2_button.action()
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                if _3_button.is_clicked(mouse_pos):
                    _3_button.action()
                if _4_button.is_clicked(mouse_pos):
                    _4_button.action()
                    
        pygame.display.update()

#song 1
def S1():
    # Initialize the mixer for music playback
    pygame.mixer.init()
    pygame.display.set_caption("Elevate - Nature sounds")
    pygame.mixer.music.load("calm_music.mp3")

    # Load the image
    nature_image = pygame.image.load("nature_image.jpeg")
    nature_image = pygame.transform.scale(nature_image, (400, 300))

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=M2)
        play_button = Button(250, 500, 200, 100, SKYBLUE, BLACK, "Play", action=lambda: pygame.mixer.music.play(-1))
        pause_button = Button(550, 500, 200, 100, SKYBLUE, BLACK, "Pause", action=lambda: pygame.mixer.music.pause())
        stop_button = Button(850, 500, 200, 100, SKYBLUE, BLACK, "Stop", action=lambda: pygame.mixer.music.stop())

        # Draw buttons
        back_button.draw(screen)
        play_button.draw(screen)
        pause_button.draw(screen)
        stop_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                if play_button.is_clicked(mouse_pos):
                    play_button.action()
                if pause_button.is_clicked(mouse_pos):
                    pause_button.action()
                if stop_button.is_clicked(mouse_pos):
                    stop_button.action()

        draw_text("Music Player", font, BLUE, screen, WIDTH // 2, 100)
        draw_text("Type Of Music: Nature sounds", font, BLUE, screen, WIDTH // 2, 135)

        # Display the image
        screen.blit(nature_image, (WIDTH // 2 - 200, 180))

        pygame.display.update() 

#song 2
def S2():
    # Initialize the mixer for music playback
    pygame.mixer.init()
    pygame.display.set_caption("Elevate - White Noise")
    pygame.mixer.music.load("White.Noise.mp3")

    # Load the image
    nature_image = pygame.image.load("White Noise.jpeg")
    nature_image = pygame.transform.scale(nature_image, (600, 300))

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=M2)
        play_button = Button(250, 500, 200, 100, SKYBLUE, BLACK, "Play", action=lambda: pygame.mixer.music.play(-1))
        pause_button = Button(550, 500, 200, 100, SKYBLUE, BLACK, "Pause", action=lambda: pygame.mixer.music.pause())
        stop_button = Button(850, 500, 200, 100, SKYBLUE, BLACK, "Stop", action=lambda: pygame.mixer.music.stop())

        # Draw buttons
        back_button.draw(screen)
        play_button.draw(screen)
        pause_button.draw(screen)
        stop_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                if play_button.is_clicked(mouse_pos):
                    play_button.action()
                if pause_button.is_clicked(mouse_pos):
                    pause_button.action()
                if stop_button.is_clicked(mouse_pos):
                    stop_button.action()

        draw_text("Music Player", font, BLUE, screen, WIDTH // 2, 100)
        draw_text("Type Of Music: White Noise", font, BLUE, screen, WIDTH // 2, 135)

        # Display the image
        screen.blit(nature_image, (WIDTH // 2 - 300, 180))

        pygame.display.update()

#song 3
def S3():
    # Initialize the mixer for music playback
    pygame.mixer.init()
    pygame.display.set_caption("Elevate - Seasonal Ambience")
    pygame.mixer.music.load("Seasonal.Ambience.mp3")

    # Load the image
    nature_image = pygame.image.load("Seasonal Ambience.jpeg")
    nature_image = pygame.transform.scale(nature_image, (600, 300))

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=M2)
        play_button = Button(250, 500, 200, 100, SKYBLUE, BLACK, "Play", action=lambda: pygame.mixer.music.play(-1))
        pause_button = Button(550, 500, 200, 100, SKYBLUE, BLACK, "Pause", action=lambda: pygame.mixer.music.pause())
        stop_button = Button(850, 500, 200, 100, SKYBLUE, BLACK, "Stop", action=lambda: pygame.mixer.music.stop())

        # Draw buttons
        back_button.draw(screen)
        play_button.draw(screen)
        pause_button.draw(screen)
        stop_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                if play_button.is_clicked(mouse_pos):
                    play_button.action()
                if pause_button.is_clicked(mouse_pos):
                    pause_button.action()
                if stop_button.is_clicked(mouse_pos):
                    stop_button.action()

        draw_text("Music Player", font, BLUE, screen, WIDTH // 2, 100)
        draw_text("Type of Music: Seasonal Ambience", font, BLUE, screen, WIDTH // 2, 135)

        # Display the image
        screen.blit(nature_image, (WIDTH // 2 - 300, 180))

        pygame.display.update() 

#Song 4
def S4():
    # Initialize the mixer for music playback
    pygame.mixer.init()
    pygame.display.set_caption("Elevate - Lullabies")
    pygame.mixer.music.load("Lullabies.mp3")

    # Load the image
    nature_image = pygame.image.load("Lullabies.jpeg")
    nature_image = pygame.transform.scale(nature_image, (400, 300))

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=M2)
        play_button = Button(250, 500, 200, 100, SKYBLUE, BLACK, "Play", action=lambda: pygame.mixer.music.play(-1))
        pause_button = Button(550, 500, 200, 100, SKYBLUE, BLACK, "Pause", action=lambda: pygame.mixer.music.pause())
        stop_button = Button(850, 500, 200, 100, SKYBLUE, BLACK, "Stop", action=lambda: pygame.mixer.music.stop())

        # Draw buttons
        back_button.draw(screen)
        play_button.draw(screen)
        pause_button.draw(screen)
        stop_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                if play_button.is_clicked(mouse_pos):
                    play_button.action()
                if pause_button.is_clicked(mouse_pos):
                    pause_button.action()
                if stop_button.is_clicked(mouse_pos):
                    stop_button.action()

        draw_text("Music Player", font, BLUE, screen, WIDTH // 2, 100)
        draw_text("Type of Music: Lullabies", font, BLUE, screen, WIDTH // 2, 135)

        # Display the image
        screen.blit(nature_image, (WIDTH // 2 - 190, 180))

        pygame.display.update() 

# Gratitude Practice
def MDS2():
   while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - Calming the Mind")
        screen.fill(WHITE)

        # Buttons (X, Y with, Hight)
        _1_button = Button(100, 40, 450, 550, BABYBLUE, BLACK, "Positive Reflections", action=GR1)
        _2_button = Button(750, 40, 450, 550, BABYBLUE, BLACK, "Expressing Appreciation", action=GR86)
        # Back button
        back_button = Button(920, 620, 300, 100, BABYBLUE, BLACK, "Back", action=M1)

        # Draw buttons
        _1_button.draw(screen)
        _2_button.draw(screen)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if _1_button.is_clicked(mouse_pos):
                    _1_button.action()
                if _2_button.is_clicked(mouse_pos):
                    _2_button.action()
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                    
        pygame.display.update()

#Breathing Exercises
def MDS1():
     while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - Calming the Mind")
        screen.fill(WHITE)

        # Buttons (X, Y with, Hight)
        _1_button = Button(100, 40, 450, 550, BABYBLUE, BLACK, "Square Breathing", action=DS1)
        _2_button = Button(750, 40, 450, 550, BABYBLUE, BLACK, "4-7-8 Breathing", action=DS2)
        # Back button
        back_button = Button(920, 620, 300, 100, BABYBLUE, BLACK, "Back", action=M1)

        # Draw buttons
        _1_button.draw(screen)
        _2_button.draw(screen)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if _1_button.is_clicked(mouse_pos):
                    _1_button.action()
                if _2_button.is_clicked(mouse_pos):
                    _2_button.action()
                if back_button.is_clicked(mouse_pos):
                    back_button.action()
                    
        pygame.display.update()

# Square Breathing
def DS1():
    # Colors
    BACKGROUND_COLOR = (30, 30, 30)
    SQUARE_COLOR = (50, 150, 255)
    pygame.display.set_caption("Elevate - Square Breathing")
    square_size = 150
    max_size = 300
    PHASE_DURATION = 4

    # Fonts
    font = pygame.font.Font(None, 74)

    # Phases
    phases = ["Breathe In", "Hold", "Breathe Out", "Hold"]
    phase_index = 0
    phase_start_time = time.time()

    while True:
        screen.fill(BACKGROUND_COLOR)
        current_time = time.time()
        elapsed_time = current_time - phase_start_time

        # Change phase when time is up
        if elapsed_time > PHASE_DURATION:
            phase_index = (phase_index + 1) % len(phases)
            phase_start_time = current_time

        # Determine square size
        phase = phases[phase_index]
        if phase == "Breathe In":
            square_size = 150 + int((max_size - 150) * (elapsed_time / PHASE_DURATION))
        elif phase == "Hold":
            square_size = max_size if "In" in phases[phase_index - 1] else 150
        elif phase == "Breathe Out":
            square_size = max_size - int((max_size - 150) * (elapsed_time / PHASE_DURATION))

        # Draw square
        square = pygame.Rect((WIDTH - square_size) // 2, (HEIGHT - square_size) // 2, square_size, square_size)
        pygame.draw.rect(screen, SQUARE_COLOR, square)

        # Draw text
        render = font.render(phase, True, WHITE)
        text_rect = render.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        screen.blit(render, text_rect)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=MDS1)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(pygame.mouse.get_pos()):
                    back_button.action()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# 4-7-8 Breathing
from itertools import cycle

def DS2():
    # Load GIF frames using Pillow
    gif_path = "4-7-8 Breathing.gif"
    pil_gif = Image.open(gif_path)
    
    # Extract frames and convert them to Pygame surfaces
    frames = []
    try:
        while True:
            frame = pil_gif.copy()
            frame = frame.convert("RGBA")
            mode = frame.mode
            size = frame.size
            data = frame.tobytes()
            pygame_image = pygame.image.fromstring(data, size, mode)
            frames.append(pygame_image)
            pil_gif.seek(pil_gif.tell() + 1)
    except EOFError:
        pass

    # Set up frame iteration
    frame_cycle = cycle(frames)
    frame_duration = 0.09
    last_update_time = time.time()
    current_frame = next(frame_cycle)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - 4-7-8 Breathing")
        screen.fill(DODGERBLUE)

        # Draw the current GIF frame
        gif_rect = current_frame.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(current_frame, gif_rect)

        # Back button
        back_button = Button(920, 620, 300, 100, CORNFLOWERBLUE, BLACK, "Back", action=MDS1)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()

        # Update the frame based on time
        current_time = time.time()
        if current_time - last_update_time >= frame_duration:
            current_frame = next(frame_cycle)
            last_update_time = current_time

        pygame.display.update()

# Positive Reflections
def GR1():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - Positive Reflections")
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=MDS2)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()

        draw_text("Gratitude Practice", font, BLUE, screen, WIDTH // 2, HEIGHT // 5)
        draw_text("Reflections on the positive and thankful moments of the day", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)

        pygame.display.update()

# Expressing Appreciation
def GR86():

    while True:
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.set_caption("Elevate - Expressing Appreciation")
        screen.fill(WHITE)

        # Back button
        back_button = Button(920, 620, 300, 100, LIGHTBLUE, BLACK, "Back", action=MDS2)
        back_button.draw(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(mouse_pos):
                    back_button.action()

        # Title
        draw_text("Gratitude Practice: Expressing Appreciation", font, BLUE, screen, WIDTH // 2, HEIGHT // 5)

        # Main description
        text = (
            "Write down three specific things or people you are grateful for today "
            "and why they made a positive impact."
        )
        words = text.split(' ')
        lines = []
        current_line = words[0]
        max_width = 600

        # Word wrapping logic
        for word in words[1:]:
            test_line = f"{current_line} {word}"
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)

        # Render each line
        for i, line in enumerate(lines):
            line_surface = font.render(line, True, BLACK)
            line_rect = line_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * font.size(line)[1]))
            screen.blit(line_surface, line_rect)

        pygame.display.update()

# Start at main_menu
main_menu()