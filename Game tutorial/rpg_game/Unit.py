from SpriteSheet import *
from Constants import *


class Unit:
    def __init__(self, screen, file_name, x, y, d, name, hp, mp, defence=0):
        self.is_render_ui = False
        self.speed = PLAYER_SPEED
        self.screen = screen
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.defence = defence
        self.state = ALIVE
        self.position = [x, y, d]
        self.name = name
        self.file_name = file_name
        sprite_sheet = SpriteSheet(file_name)

        self.image_pack_ui = ['./health_bar.jpg', './health_point.jpg', './mana_bar.jpg', './mana_point.jpg']
        self.images_ui = []

        for image in self.image_pack_ui:
            i = pygame.image.load(image)
            self.images_ui.append(i)

        self.walking_frames_r = []
        x, y = 0, 704  # start position on sprite sheet
        # Load all the right facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT)
            self.walking_frames_r.append(image)
            x += 64

        self.walking_frames_l = []
        x, y = 0, 576
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_l.append(image)
            x += 64

        self.walking_frames_up = []
        x, y = 0, 512
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_up.append(image)
            x += 64

        self.walking_frames_down = []
        x, y = 0, 640
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.walking_frames_down.append(image)
            x += 64

        self.frames_dead = []
        self.frame_dead = 0
        x, y = 0, 1280
        # Load all the left facing images into a list
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_dead.append(image)
            x += 64

        self.frame = 0
        self.image = self.walking_frames_down[self.frame]
        self.set_direction(d)
        self.moving = [0, 0, 0, 0]

    def set_direction(self, d):
        if d == RIGHT:
            self.image = self.walking_frames_r[self.frame]
        if d == LEFT:
            self.image = self.walking_frames_l[self.frame]
        if d == UP:
            self.image = self.walking_frames_up[self.frame]
        if d == DOWN:
            self.image = self.walking_frames_down[self.frame]

    def set_position(self, x, y, d=RIGHT):
        self.position = [x, y, d]
        self.set_direction(d)

    def update(self):
        if self.state == DEAD:
            self.image = self.frames_dead[self.frame_dead]
            if len(self.frames_dead) > self.frame_dead + 1:
                self.frame_dead += 1
            return
        self.move()
        if self.moving[RIGHT] == 1:
            self.image = self.walking_frames_r[self.frame]
            if len(self.walking_frames_r) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[LEFT] == 1:
            self.image = self.walking_frames_l[self.frame]
            if len(self.walking_frames_l) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[DOWN] == 1:
            self.image = self.walking_frames_down[self.frame]
            if len(self.walking_frames_down) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving[UP] == 1:
            self.image = self.walking_frames_up[self.frame]
            if len(self.walking_frames_up) > self.frame + 1:
                self.frame += 1
            else:
                self.frame = 0

        if self.moving == [0, 0, 0, 0]:
            self.frame = 0

    def move(self):
        if self.moving[UP] == 1:
            self.position[Y] -= self.speed
        if self.moving[DOWN] == 1:
            self.position[Y] += self.speed
        if self.moving[RIGHT] == 1:
            self.position[X] += self.speed
        if self.moving[LEFT] == 1:
            self.position[X] -= self.speed

        if self.position[Y] < 0:
            self.position[Y] = 0
        if self.position[Y] > SCREEN_HEIGHT - HERO_SPRITE_HEIGHT:
            self.position[Y] = SCREEN_HEIGHT - HERO_SPRITE_HEIGHT
        if self.position[X] < 0:
            self.position[X] = 0
        if self.position[X] > SCREEN_WIDTH - HERO_SPRITE_WIDTH:
            self.position[X] = SCREEN_WIDTH - HERO_SPRITE_WIDTH

    def lose_hp(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.state = DEAD

    def render_ui(self):
        self.screen.blit(self.images_ui[HEALTH_BAR], (self.position[X] + 7, self.position[Y] + HERO_SPRITE_HEIGHT))
        d_hp = int(self.hp / HEALTH_BAR_SIZE / HEALTH_POINT_SIZE)
        for i, p in enumerate(range(0, d_hp)):
            self.screen.blit(self.images_ui[HEALTH_POINT],
                             (self.position[X] + 7 + (i * HEALTH_POINT_SIZE), self.position[Y] + HERO_SPRITE_HEIGHT))

        self.screen.blit(self.images_ui[MP_BAR], (self.position[X] + 7, self.position[Y] + HERO_SPRITE_HEIGHT + 7))
        d_mp = int(self.mp / MP_BAR_SIZE / MP_POINT_SIZE)
        for i, p in enumerate(range(0, d_mp)):
            self.screen.blit(self.images_ui[MP_POINT],
                             (self.position[X] + 7 + (i * MP_POINT_SIZE), self.position[Y] + HERO_SPRITE_HEIGHT + 7))

    def render(self):
        self.screen.blit(self.image, (self.position[X], self.position[Y]))
        self.render_rect()
        if self.is_render_ui:
            self.render_ui()

    def render_rect(self):
        if DRAW_RECT:
            pygame.draw.rect(self.screen, GREEN,
                             [self.position[X], self.position[Y], HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT], 2)
