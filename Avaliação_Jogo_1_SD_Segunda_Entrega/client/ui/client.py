import pygame

class Player1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('client/ui/assets/teste1.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.direction = 'stand_down'
        self.left_states = {0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76)}
        self.right_states = {0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76)}
        self.up_states = {0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76)}
        self.down_states = {0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76)}
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction != self.direction:
            self.direction = direction

        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            elif event.key == pygame.K_RIGHT:
                self.update('right')
            elif event.key == pygame.K_UP:
                self.update('up')
            elif event.key == pygame.K_DOWN:
                self.update('down')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.update('stand_down')

class Player2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('client/ui/assets/teste.png')
        self.sheet.set_clip(pygame.Rect(11, 9, 34, 49))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.direction = 'stand_down'
        self.left_states = {0: (14,131,31,49), 1: (115,131,31,49), 2: (65,133,31,47), 3:(167,133,31,47)}
        self.right_states = {0: (11,192,31,47), 1: (62,190,31,49), 2: (114,192,31,47), 3:(164,190,31,49)}
        self.up_states = {0: (11,71,34,49), 1: (112,71,34,48), 2: (63,74,34,47), 3:(164,74,34,47)}
        self.down_states = {0: (11, 9, 34, 49), 1: (112,9,34,48), 2: (61,11,34,46), 3:(163,11,34,47)}
#sprites feitos no site
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction != self.direction:
            self.direction = direction

        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.update('left')
            elif event.key == pygame.K_d:
                self.update('right')
            elif event.key == pygame.K_w:
                self.update('up')
            elif event.key == pygame.K_s:
                self.update('down')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                self.update('stand_down')
