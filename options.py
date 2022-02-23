import menu
import pygame
import settings


def displayValues(screen, n, time_step, colour, distribution):
    items = [n, time_step, colour, distribution]
    txts = ["N", "Time Step", "Colour", "Distribution"]

    colour_options = {
        0: "Blue - Green",
        1: "Red - Purple",
        2: "Black - White",
        3: "Cyan - Yellow"
    }

    distribution_options = {
        0: "Uniform",
        1: "Random"
    }

    gap = settings.HEIGHT // (len(txts) + 1)

    for indx, (item, txt) in enumerate(zip(items, txts)):
        if txt == "Colour":
            item_str = f"{txt}: {colour_options[item]}"

        elif txt == "Distribution":
            item_str = f"{txt}: {distribution_options[item]}"

        else:
            item_str = f"{txt}: {str(item)}"

        draw_txt = settings.FONT.render(item_str, 1, settings.GREEN)

        size = settings.FONT.size(item_str)

        screen.blit(draw_txt, (settings.WIDTH // 2 +
                    300 - size[0] // 2, gap * (indx + 1)))


def settings_menu(screen, n, time_step, colour, distribution):
    buttons = menu.makeOptionsMenu()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for button in buttons:
                    if button.rect.collidepoint(pos):
                        if button.n_change:
                            n *= button.n_change
                            n = int(n // 1)

                        if n < 25:
                            n = 25

                        if n > 1600:
                            n = 1600

                        time_step += button.time_step_change

                        if time_step < 0:
                            time_step = 0

                        colour += button.colour_change
                        colour %= 4

                        distribution += button.distribution
                        distribution %= 2

        menu.drawMenu(screen, buttons)
        displayValues(screen, n, time_step, colour, distribution)
        pygame.display.flip()

    return n, time_step, colour, distribution
