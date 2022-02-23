import random
import settings
import pygame


def generateRandomList(n, l, h, distribution):
    arr = []

    if distribution == 1:
        for _ in range(n):
            arr.append(random.randint(l, h))

    elif distribution == 0:
        step = (h - l) // n

        for i in range(n):
            arr.append(l + i * step)

    random.shuffle(arr)

    return arr


def drawBar(screen, bar_size, bar_width, m, idx, colour):
    proportion = bar_size / m
    bar_height = round(proportion * settings.HEIGHT)

    draw_rect = pygame.Rect(
        bar_width * idx, settings.HEIGHT // 2 - bar_height // 2, bar_width, bar_height)

    if colour == 0:
        pygame.draw.rect(screen, (0, round(proportion * 255),
                         255 - round(proportion * 255)), draw_rect)

    if colour == 1:
        pygame.draw.rect(screen, (255, 0, round(proportion * 255)), draw_rect)

    if colour == 2:
        pygame.draw.rect(screen, (round(
            proportion * 255), round(proportion * 255), round(proportion * 255)), draw_rect)

    if colour == 3:
        pygame.draw.rect(screen, (round(proportion * 255), 255,
                         255 - round(proportion * 255)), draw_rect)


class Sort:
    def __init__(self, sort):
        self.sort = sort

    def generateVisual(self, n, l, h, distribution):
        arr = generateRandomList(n, l, h, distribution)

        self.visual = self.sort(arr)

    def displayVisual(self, screen, m, n, time_step, colour):
        bar_width = settings.WIDTH // n

        for state in self.visual:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            screen.fill(settings.WHITE)

            for idx, bar_size in enumerate(state):
                drawBar(screen, bar_size, bar_width, m, idx, colour)

            pygame.display.flip()
            pygame.time.delay(time_step)

        pygame.time.delay(2000)
        return True
