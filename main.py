import pygame
import math


class Circle:
    def __init__(self, x=500, y=500, r=10, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dir = 0

    def move(self, vel):
        if self.dir >= 0:
            self.y = self.y - (math.sin(math.radians(90 - self.dir)) * vel)
            self.x = self.x - (math.cos(math.radians(90 - self.dir)) * vel)
        elif self.dir < 0:
            self.y = self.y - (math.sin(math.radians(90 - abs(self.dir))) * vel * -1)
            self.x = self.x - (math.cos(math.radians(90 - abs(self.dir))) * vel * -1)
        if self.x > 1000:
            self.x = 1000
        if self.x < 0:
            self.x = 0
        if self.y > 1000:
            self.y = 1000
        if self.y < 0:
            self.y = 0

    def update_rad(self, r):
        self.r = r

    def rotate(self, rot):
        if rot > 30:
            rot = 30
        if rot < -30:
            rot = -30
        self.dir += rot

    def render(self, win):
        circle = pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.r)


def grob(circle, key, vel):

    if key[pygame.K_DOWN]:
        circle.y += vel
    if key[pygame.K_LEFT] and key[pygame.K_UP]:
        circle.y -= vel
        circle.x -= vel
    elif key[pygame.K_UP]:
        circle.y -= vel
    elif key[pygame.K_LEFT]:
        circle.x -= vel
    if key[pygame.K_RIGHT] and key[pygame.K_UP]:
        circle.y -= vel
        circle.x += vel
    elif key[pygame.K_UP]:
        circle.y -= vel
    elif key[pygame.K_RIGHT]:
        circle.x += vel


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    bg = (255, 255, 255)
    size = (1000, 1000)
    vel = 5
    rot = 3

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Kreis fahren')

    circle = Circle()
    circle.render(screen)
    rect = pygame.draw.rect(screen, (255, 255, 0), (500, 500, 50, 50))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        key = pygame.key.get_pressed()

        # grob(circle, key, vel)

        if key[pygame.K_UP]:
            if vel <= 20:
                vel = vel + vel * 0.01
                print('mehr ', vel)
            circle.move(vel)
            if key[pygame.K_RIGHT]:
                circle.rotate(rot)
            if key[pygame.K_LEFT]:
                circle.rotate(rot * -1)
        else:
            if vel > 2:
                vel -= vel * 0.0025
                circle.move(vel)
                print('weniger ', vel)
            else:
                if key[pygame.K_RIGHT]:
                    circle.rotate(rot)
                if key[pygame.K_LEFT]:
                    circle.rotate(rot * -1)
        if key[pygame.K_RIGHT]:
            circle.rotate(rot)
        if key[pygame.K_LEFT]:
            circle.rotate(rot * -1)

        if circle.x > 1000:
            circle.x = 1000
        if circle.x < 0:
            circle.x = 0
        if circle.y > 1000:
            circle.y = 1000
        if circle.y < 0:
            circle.y = 0

        screen.fill(bg)
        circle.render(screen)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
