import settings
import pygame
import visualiser
import options
import sorts_slow_comparison as slow
import sorts_fast_comparison as fast
import sorts_counting as counting
import sorts_vanity as vanity


class Button:
    def __init__(self, text, x, y, width, height, centre, sort):
        self.text = text

        if centre:
            self.x = x - width // 2
            self.y = y - height // 2

        else:
            self.x = x
            self.y = y

        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.sort = sort

    def drawButton(self, screen):
        pygame.draw.rect(screen, settings.BLUE, self.rect, 6, 2)
        text = settings.FONT.render(str(self.text), 1, settings.BLACK)
        size = settings.FONT.size(str(self.text))
        x = self.x + self.width // 2 - size[0] // 2
        y = self.y + self.height // 2 - size[1] // 2

        screen.blit(text, (x, y))


class OptionButton:
    def __init__(self, text, x, y, width, height, centre,
                 n_change, time_step_change, colour_change, distribution):
        self.text = text

        if centre:
            self.x = x - width // 2
            self.y = y - height // 2

        else:
            self.x = x
            self.y = y

        self.width = width
        self.height = height

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.n_change = n_change

        self.time_step_change = time_step_change
        self.colour_change = colour_change

        self.distribution = distribution

    def drawButton(self, screen):
        pygame.draw.rect(screen, settings.BLUE, self.rect, 6, 2)
        text = settings.FONT.render(str(self.text), 1, settings.BLACK)
        size = settings.FONT.size(str(self.text))
        x = self.x + self.width // 2 - size[0] // 2
        y = self.y + self.height // 2 - size[1] // 2

        screen.blit(text, (x, y))


def makeOptionsMenu():
    buttons = []
    txts = ["Increase Number", "Decrease Number",
            "Increase Timestep", "Decrease Timestep",
            "Cycle Colour", "Cycle Distribution"]

    n_changes = [2, 0.5, 0, 0, 0, 0]
    time_step_changes = [0, 0, 10, -10, 0, 0]

    colour_changes = [0, 0, 0, 0, 1, 0]

    distributions = [0, 0, 0, 0, 0, 1]

    gap = settings.HEIGHT // (len(txts) + 1)

    for indx, (txt, n_change, time_step_change, colour_change, distribution) in enumerate(zip(txts, n_changes,
                                                                                              time_step_changes, colour_changes, distributions)):

        buttons.append(OptionButton(txt, settings.WIDTH // 2 - 300, gap * (indx + 1),
                       450, gap - 30, True, n_change, time_step_change, colour_change, distribution))

    return buttons


def makeButtonColumn(txts, sorts, x):
    buttons = []

    gap = settings.HEIGHT // (len(txts) + 1)
    for indx, (txt, sort) in enumerate(zip(txts, sorts)):
        buttons.append(Button(txt, x, gap * (indx + 1),
                       400, gap - 30, True, sort))

    return buttons


def makeMenu():
    buttons = []
    txts_1 = ["Bubble", "Selection", "Insertion", "Merge", "Counting"]

    txts_2 = ["Radix", "Bogo", "Gnome", "Cocktail", "Settings"]

    sorts_1 = [slow.bubble, slow.selection,
               slow.insertion, fast.merge, counting.counting]

    sorts_2 = [counting.radix, vanity.bogo,
               vanity.gnome, vanity.cocktail, None]

    buttons.extend(makeButtonColumn(
        txts_1, sorts_1, settings.WIDTH // 2 - 300))
    buttons.extend(makeButtonColumn(
        txts_2, sorts_2, settings.WIDTH // 2 + 300))

    return buttons


def drawMenu(screen, buttons):
    screen.fill(settings.WHITE)

    for button in buttons:
        button.drawButton(screen)


def menu():
    buttons = makeMenu()
    screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pygame.display.set_caption("Sorting Visualiser")
    done = False
    n, l, h, time_step = 200, 0, 1600, 0
    colour, distribution = 0, 0

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for button in buttons:
                    if button.rect.collidepoint(pos):
                        if not button.sort:
                            n, time_step, colour, distribution = options.settings_menu(
                                screen, n, time_step, colour, distribution)
                            continue

                        sort = visualiser.Sort(button.sort)

                        if button.sort == vanity.bogo:
                            sort.generateVisual(7, l, h, distribution)

                            sort.displayVisual(
                                screen, h, 7, time_step, colour)

                            continue

                        sort.generateVisual(n, l, h, distribution)

                        sort.displayVisual(screen, h, n, time_step, colour)

        drawMenu(screen, buttons)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    menu()
    pygame.quit()
