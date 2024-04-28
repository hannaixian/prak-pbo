import pygame, sys, random

class Object:
    def __init__(self, x, y, lebar, tinggi, warna):
        self.rect = pygame.Rect(x, y, lebar, tinggi)
        self.color = warna
    
    def draw (self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def draw_bola (self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

class Bola (Object):
    def __init__(self, x, y, lebar, tinggi, warna):
        super().__init__(x, y, lebar, tinggi, warna)
        self.speedX = 5 * random.choice((1, -1))
        self.speedY = 5 * random.choice((1, -1))

    def move (self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

    def hit (self, other):
        return self.rect.colliderect(other.rect)

    def bounce (self):
        self.speedY *= -1

class Hitter (Object):
    def __init__(self, x, y, lebar, tinggi, warna):
        super().__init__(x, y, lebar, tinggi, warna)
        self.speed = 0

    def move (self):
        self.rect.x += self.speed
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 700:
            self.rect.right = 700

class Wall (Object):
    def __init__(self, x, y, lebar, tinggi, warna):
        super().__init__(x, y, lebar, tinggi, warna)

class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Hit the Ball!")
        self.bg_color = pygame.Color("grey12")
        self.light_grey = (200, 200, 200)

        self.ball = Bola(340, 240, 20, 20, self.light_grey)
        self.hitter = Hitter(300, 485, 100, 15, self.light_grey)
        self.wall = Wall(0, 0, 700, 40, self.light_grey)
    
    def events (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hitter.speed -= 7
                if event.key == pygame.K_RIGHT:
                    self.hitter.speed += 7

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.hitter.speed += 7
                if event.key == pygame.K_RIGHT:
                    self.hitter.speed -= 7

    def update (self):
        self.ball.move()
        self.hitter.move()

        if self.ball.rect.top <= 0 or self.ball.rect.bottom >= 500:
            self.ball.bounce()

        if self.ball.rect.left <= 0 or self.ball.rect.right >= 700:
            self.ball.speedX *= -1

        if self.ball.hit(self.hitter) or self.ball.hit(self.wall):
            self.ball.bounce()

    def run (self):
        while True:
            self.events()
            self.update()

            self.screen.fill(self.bg_color)
            self.ball.draw_bola(self.screen)
            self.hitter.draw(self.screen)
            self.wall.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()

# def BallAnimation():
#     global ball_speed_x, ball_speed_y
	
#     ball.x += ball_speed_x
#     ball.y += ball_speed_y

#     if ball.top <= 0 or ball.bottom >= 500:
#         RandomDirBall()
#     if ball.left <= 0 or ball.right >= 700:
#         ball_speed_x *= -1

#     if ball.colliderect(hitter) or ball.colliderect(wall):
#            ball_speed_y *= -1

# def HitterMovement():
# 	hitter.x += hitter_speed

# 	if hitter.left <= 0:
# 		hitter.left = 0
# 	if hitter.right >= 700:
# 		hitter.right = 700

# def RandomDirBall():
#     global ball_speed_x, ball_speed_y

#     ball.center = (350, 250)
#     ball_speed_x *= random.choice((1,-1))
#     ball_speed_y *= random.choice((1,-1))


# pygame.init()

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((700, 500))
# pygame.display.set_caption("Hit the Ball!")

# ball = pygame.Rect(340, 240, 20, 20)
# hitter = pygame.Rect(300, 485, 100, 15)
# wall = pygame.Rect(0, 0, 700, 40)

# bg_color = pygame.Color("grey12")
# light_grey = (200, 200, 200)

# ball_speed_x = 5 * random.choice((1, -1))
# ball_speed_y = 5 * random.choice((1, -1))
# hitter_speed = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
			
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 hitter_speed -= 7
#             if event.key == pygame.K_RIGHT:
#                 hitter_speed += 7
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 hitter_speed += 7
#             if event.key == pygame.K_RIGHT:
#                 hitter_speed -= 7

#     BallAnimation()
#     HitterMovement()

#     screen.fill(bg_color)
#     pygame.draw.rect(screen, light_grey, hitter)
#     pygame.draw.rect(screen, light_grey, wall)
#     pygame.draw.ellipse(screen, light_grey, ball)

#     pygame.display.update()
#     clock.tick(60)