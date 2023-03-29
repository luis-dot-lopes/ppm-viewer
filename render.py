import pygame
import sys

width, height = 0, 0
pixels = []

if len(sys.argv) < 2:
    print("Error: no file to display")
    sys.exit(1)

with open(sys.argv[1], "rb") as file:
    lines = file.readlines()
    filetype, dimensions = lines[:2]
    width, height = map(int, dimensions.decode('utf-8')[:-1].split()[:-1])
    pixels = [int(pixel) for pixels in lines[2:] for pixel in pixels]
    pixels = [tuple(pixels[i:i + 3]) for i in range(0, len(pixels), 3)]

screen = pygame.display.set_mode((width, height))
imagesurface = pygame.Surface((width, height))
imagepixels = pygame.PixelArray(imagesurface)
for y in range(height):
    imagepixels[:, y] = pixels[width*y:width*y + width]

del imagepixels

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(imagesurface, (0, 0))
    pygame.display.flip()
