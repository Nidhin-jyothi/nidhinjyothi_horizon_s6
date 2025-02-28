import pygame
import random
import math

pygame.init()

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dynamic Circle Sketcher")

# Persistent canvas
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
canvas.fill((255, 255, 255))

circle_list = []  # Stores drawn circles
drawing = False
initial_pos = None
circle_size = 10
total_path = 0

active = True
while active:
    screen.blit(canvas, (0, 0))  # Maintain drawn elements
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left-click to start drawing
                initial_pos = event.pos
                drawing = True
                circle_size = 10
            elif event.button == 3 and circle_list:  # Right-click to remove last circle
                circle_list.pop()
                canvas.fill((255, 255, 255))  # Reset canvas
                total_path = 0
                for i, (cx, cy, cs, ccolor) in enumerate(circle_list):
                    pygame.draw.circle(canvas, ccolor, (cx, cy), cs)
                    if i > 0:
                        pygame.draw.line(canvas, (0, 0, 0), (circle_list[i-1][0], circle_list[i-1][1]), (cx, cy), 2)
                        total_path += math.dist((circle_list[i-1][0], circle_list[i-1][1]), (cx, cy))

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if initial_pos:
                color_variant = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                circle_list.append((*initial_pos, circle_size, color_variant))
                pygame.draw.circle(canvas, color_variant, initial_pos, circle_size)
                if len(circle_list) > 1:
                    pygame.draw.line(canvas, (0, 0, 0), (circle_list[-2][0], circle_list[-2][1]), initial_pos, 2)
                    total_path += math.dist((circle_list[-2][0], circle_list[-2][1]), initial_pos)
                drawing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.image.save(canvas, "sketch.png")
                print("Sketch saved!")
            elif event.key == pygame.K_SPACE:
                canvas.fill((255, 255, 255))
                circle_list.clear()
                total_path = 0
                print("Canvas wiped!")

    if drawing and initial_pos:
        circle_size += 1  # Expand circle while holding click
        pygame.draw.circle(screen, (0, 0, 0), initial_pos, circle_size, 1)
    
    font = pygame.font.Font(None, 30)
    text = font.render(f"Total Path: {round(total_path, 2)}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.update()

pygame.quit()
