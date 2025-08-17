import pygame


class Player:
    def __init__(self, pos: pygame.Rect, color: pygame.Color, speed: int):
        self.pos = pos
        self.color = color
        self.speed = speed
        self.vx = 0
        self.vy = 0


class Object:
    def __init__(self, pos: pygame.Rect, color: pygame.Color):
        self.pos = pos
        self.color = color


def collision(player: Player, tree: Object):
    if player.pos.colliderect(tree.pos):
        if player.vx > 0:
            player.pos.x -= player.speed
        if player.vx < 0:
            player.pos.x += player.speed
        if player.vy > 0:
            player.pos.y -= player.speed
        if player.vy < 0:
            player.pos.y += player.speed

    return player.pos


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

    tree_pos = pygame.Rect((screen.get_width() / 4, screen.get_height() / 4), (25, 25))
    tree_color = pygame.Color(30, 70, 0, 255)
    tree1 = Object(tree_pos, tree_color)

    tree_pos = pygame.Rect((screen.get_width() / 2, screen.get_height() / 4), (25, 25))
    tree_color = pygame.Color(30, 70, 0, 255)
    tree2 = Object(tree_pos, tree_color)

    tree_pos = pygame.Rect(
        (screen.get_width() * 3 / 4, screen.get_height() / 4), (25, 25)
    )
    tree_color = pygame.Color(30, 70, 0, 255)
    tree3 = Object(tree_pos, tree_color)

    tree_pos = pygame.Rect(
        (screen.get_width() / 4, screen.get_height() * 3 / 4), (25, 25)
    )
    tree_color = pygame.Color(30, 70, 0, 255)
    tree4 = Object(tree_pos, tree_color)

    tree_pos = pygame.Rect(
        (screen.get_width() / 2, screen.get_height() * 3 / 4), (25, 25)
    )
    tree_color = pygame.Color(30, 70, 0, 255)
    tree5 = Object(tree_pos, tree_color)

    tree_pos = pygame.Rect(
        (screen.get_width() * 3 / 4, screen.get_height() * 3 / 4), (25, 25)
    )
    tree_color = pygame.Color(30, 70, 0, 255)
    tree6 = Object(tree_pos, tree_color)

    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.pos.y -= player.speed
            player.vy = -player.speed
        if keys[pygame.K_s]:
            player.pos.y += player.speed
            player.vy = player.speed
        if keys[pygame.K_a]:
            player.pos.x -= player.speed
            player.vx = -player.speed
        if keys[pygame.K_d]:
            player.pos.x += player.speed
            player.vx = player.speed
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

        # collision
        player.pos = collision(player, tree1)
        player.pos = collision(player, tree2)
        player.pos = collision(player, tree3)
        player.pos = collision(player, tree4)
        player.pos = collision(player, tree5)
        player.pos = collision(player, tree6)

        player.vx = 0
        player.vy = 0

        # render loop
        screen.fill(screen_color)

        pygame.draw.rect(screen, player.color, player.pos, 0)
        pygame.draw.rect(screen, tree1.color, tree1.pos, 0)
        pygame.draw.rect(screen, tree2.color, tree2.pos, 0)
        pygame.draw.rect(screen, tree3.color, tree3.pos, 0)
        pygame.draw.rect(screen, tree4.color, tree4.pos, 0)
        pygame.draw.rect(screen, tree5.color, tree5.pos, 0)
        pygame.draw.rect(screen, tree6.color, tree6.pos, 0)

        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
