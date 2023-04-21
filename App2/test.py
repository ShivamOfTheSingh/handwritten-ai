import pygame


canvas_width = 64
canvas_height = 64
scale = 10
pygame.init()
canvas = pygame.display.set_mode((canvas_width*scale, canvas_height*scale))
pygame.display.set_caption("Draw on canvas")

canvas.fill((255, 255, 255))
last_pos = None
draw_color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            last_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            last_pos = None
        elif event.type == pygame.MOUSEMOTION and last_pos is not None:
            current_pos = pygame.mouse.get_pos()
            pygame.draw.line(canvas, draw_color, last_pos, current_pos, 20)
            last_pos = current_pos

    pygame.display.flip()

canvas_resized = pygame.transform.scale(canvas, (canvas_width, canvas_height))
pygame.image.save(canvas_resized, "canvas.png")
pygame.quit()
