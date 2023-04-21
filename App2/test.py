import pygame
import imageio.v2 as imageio
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('../model')



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
            pygame.draw.line(canvas, draw_color, last_pos, current_pos, 25)
            last_pos = current_pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                canvas_resized = pygame.transform.scale(canvas, (canvas_width, canvas_height))
                pygame.image.save(canvas_resized, "canvas.png")
                
                running = False
    pygame.display.flip()

canvas_img = imageio.imread("canvas.png")
canvas_img = np.dot(canvas_img[..., :3], [0.2989, 0.5870, 0.1140]) / 255.0
canvas_img = np.reshape(canvas_img, (1, canvas_width, canvas_height))
prediction = model.predict(canvas_img)
prediction_label = np.argmax(prediction)

prediction_font = pygame.font.Font(None, 30)
prediction_text = prediction_font.render("Prediction: " + str(prediction_label), True, (0, 0, 0))
screen = pygame.display.set_mode((300, 100))
screen.blit(prediction_text, (50, 50))
screen.fill((255, 255, 255))
pygame.display.flip()

# Wait for user to quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
