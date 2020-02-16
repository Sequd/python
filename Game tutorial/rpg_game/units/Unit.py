from core.SpriteSheet import *
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

        self.image_pack_ui = ['./data/health_bar.jpg', './data/health_point.jpg', './data/mana_bar.jpg', './data/mana_point.jpg']
        self.images_ui = []
        for image in self.image_pack_ui:
            i = pygame.image.load(image)
            self.images_ui.append(i)

        self.walking_frames = [[], [], [], []]
        x, y = 0, 704  # start position on sprite sheet
        # Load all the right facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT)
            # self.walking_frames_r.append(image)
            self.walking_frames[RIGHT].append(image)
            x += 64

        x, y = 0, 576
        # Load all the left facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            # self.walking_frames_l.append(image)
            self.walking_frames[LEFT].append(image)
            x += 64

        x, y = 0, 512
        # Load all the up facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            # self.walking_frames_up.append(image)
            self.walking_frames[UP].append(image)
            x += 64

        x, y = 0, 640
        # Load all the down facing images into a list
        for n in range(0, 9):
            image = sprite_sheet.get_image(x, y, 64, 64)
            # self.walking_frames_down.append(image)
            self.walking_frames[DOWN].append(image)
            x += 64

        self.frames_dead = []
        x, y = 0, 1280
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_dead.append(image)
            x += 64

        self.frames_using_skill = [[], [], [], []]
        x, y = 0, 0
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_using_skill[UP].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_using_skill[LEFT].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_using_skill[DOWN].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_using_skill[RIGHT].append(image)
            x += 64

        self.frames_attack_melee = [[], [], [], []]
        x, y = 0, 768
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_melee[UP].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_melee[LEFT].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_melee[DOWN].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 6):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_melee[RIGHT].append(image)
            x += 64

        self.frames_attack_range = [[], [], [], []]
        x, y = 0, 1024
        for n in range(0, 13):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_range[UP].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 13):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_range[LEFT].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 13):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_range[DOWN].append(image)
            x += 64
        x, y = 0, y + 64
        for n in range(0, 13):
            image = sprite_sheet.get_image(x, y, 64, 64)
            self.frames_attack_range[RIGHT].append(image)
            x += 64

        self.frame = 0
        self.frame_dead = 0
        self.frame_using_skill = 0
        self.frame_attack_melee = 0
        self.frame_attack_range = 0
        self.is_using_skill = False
        self.is_attack = False
        self.is_attack_range = False
        self.image = self.walking_frames[d][self.frame]
        self.rect = pygame.Rect(self.position[X], self.position[Y], HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT)
        self.set_direction(d)
        self.moving = [0, 0, 0, 0]

    def set_direction(self, d):
        self.image = self.walking_frames[d][self.frame]
        self.position[D] = d

    def set_position(self, x, y, d=RIGHT):
        self.position = [x, y, d]
        self.set_direction(d)

    def get_rect(self):
        return pygame.Rect(self.position[X], self.position[Y], HERO_SPRITE_WIDTH, HERO_SPRITE_HEIGHT)

    def update(self):
        if self.state == DEAD:
            self.image = self.frames_dead[self.frame_dead]
            if len(self.frames_dead) > self.frame_dead + 1:
                self.frame_dead += 1
            return

        if self.is_attack:
            self.image = self.frames_attack_melee[self.position[D]][self.frame_attack_melee]
            if len(self.frames_attack_melee[D]) > self.frame_attack_melee + 1:
                self.frame_attack_melee += 1
            else:
                self.is_attack = False
                self.frame_attack_melee = 0
                self.image = self.walking_frames[self.position[D]][self.frame]
            return

        if self.is_attack_range:
            self.image = self.frames_attack_range[self.position[D]][self.frame_attack_range]
            if len(self.frames_attack_range[D]) > self.frame_attack_range + 1:
                self.frame_attack_range += 1
            else:
                self.is_attack_range = False
                self.frame_attack_range = 0
                self.image = self.walking_frames[self.position[D]][self.frame]
            return

        if self.is_using_skill:
            self.image = self.frames_using_skill[self.position[D]][self.frame_using_skill]
            if len(self.frames_using_skill[D]) > self.frame_using_skill + 1:
                self.frame_using_skill += 1
            else:
                self.is_using_skill = False
                self.frame_using_skill = 0
                self.image = self.walking_frames[self.position[D]][self.frame]
            return

        self.move()

        self.image = self.walking_frames[self.position[D]][self.frame]
        if len(self.walking_frames[self.position[D]]) > self.frame + 1:
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
