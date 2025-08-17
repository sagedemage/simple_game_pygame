import pygame


class Player:
    def __init__(self, pos: pygame.Rect, color: pygame.Color, speed: int):
        self.pos = pos
        self.color = color
        self.speed = speed


def main():
    pygame.init()

    # VGA Resolution: 640x480 (4:3)
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    quit = False
    fps = 60

    screen_color = pygame.Color(0, 200, 100, 255)

    player_pos = pygame.Rect((10, screen.get_height() / 2), (25, 25))
    player_color = pygame.Color(150, 0, 0, 255)
    player = Player(player_pos, player_color, speed=2)

    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= player.speed
        if keys[pygame.K_s]:
            player_pos.y += player.speed
        if keys[pygame.K_a]:
            player_pos.x -= player.speed
        if keys[pygame.K_d]:
            player_pos.x += player.speed
        if keys[pygame.K_ESCAPE]:
            quit = True

        # boundaries
        if player.pos.x < 0:
            player.pos.x = 0
        if player.pos.x > screen.get_width() - player.pos.width:
            player.pos.x = screen.get_width() - player.pos.width
        if player.pos.y < 0:
            player.pos.y = 0
        if player.pos.y > screen.get_height() - player.pos.height:
            player.pos.y = screen.get_height() - player.pos.width

        # render loop
        screen.fill(screen_color)

        pygame.draw.rect(screen, player.color, player.pos, 0)

        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
