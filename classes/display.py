import pygame

pygame.init()

class Display:

    def game_over(self, message):
        self.window.fill((0, 0, 0))
        font = pygame.font.Font(None, 40)
        text = font.render(message, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = 300, 300
        self.window.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(3000)

    def _loot_item(self, gyver, items):
        """check if MacGyver meet an uncollected item,
        if he does, add it to the bag and mark the item as looted
        """
        for item in items:
            if gyver.x == item.x and gyver.y == item.y and item.looted is False:
                gyver.bag += 1
                item.looted = True
                self.show_info('You collected the {}'.format(item.name))
                self.window.blit(self.floor, (self.tile_size*item.x, self.tile_size*item.y))
                self.show_bag(gyver)
                return item
        return None

    def set_map(self, mapping):
        for y, line in enumerate(mapping.map):
            for x, tile in enumerate(line):
                if tile == '#':
                    self.window.blit(self.wall, (x*self.tile_size, y*self.tile_size))
                else:
                    self.window.blit(self.floor, (x*self.tile_size, y*self.tile_size))

    def show_looted_items(self, items):
        for x, item in enumerate(items):
            if item.looted:
                self.window.blit(item.pygame_img, (300+self.tile_size*x, 615))
        pygame.display.flip()

    def set_characters(self, gyver, bad_guy):
        gyver_position = (gyver.x * self.tile_size, gyver.y * self.tile_size)

        bad_guy_position = (bad_guy.x * self.tile_size, bad_guy.y * self.tile_size)

        self.window.blit(gyver.pygame_img, gyver_position)
        self.window.blit(bad_guy.pygame_img, bad_guy_position)


    def set_items(self, items):
        for item in items:
            image = item.pygame_img
            self.window.blit(image, (item.x * self.tile_size, item.y * self.tile_size))


    def show_info(self, message):
        """This function display the message given on the bottom left corner"""
        self.window.fill((0, 0, 0), self.bot_left)
        info_message = message
        info_render = self.font.render(info_message, True, (255, 255, 255))
        self.window.blit(info_render, self.bot_left)
        pygame.display.update(self.bot_left)


    def show_bag(self, gyver):
        """This function display the number of collected item on the bottom right corner"""
        self.window.fill((0, 0, 0), self.bot_right)
        bag_message = 'You collected {}/3 items'.format(gyver.bag)
        bag_render = self.font.render(bag_message, True, (255, 255, 255))
        self.window.blit(bag_render, self.bot_right)
        pygame.display.update(self.bot_right)


    def move_character(self, mapping, gyver, items, old_y, old_x):
        self.window.fill((0, 0, 0), self.bot_left)
        pygame.display.update(self.bot_left)
        if(old_y != gyver.y or old_x != gyver.x):
            if mapping.is_path_available(gyver.y, gyver.x):
                mapping.move_character(old_y, old_x, gyver.y, gyver.x)
                self._loot_item(gyver, items)
                self.show_looted_items(items)
                self.window.blit(gyver.pygame_img,
                                 (gyver.x * self.tile_size, gyver.y * self.tile_size))
                self.window.blit(self.floor, (old_x * self.tile_size, old_y * self.tile_size))
                pygame.display.update()
            else:
                gyver.y = old_y
                gyver.x = old_x
                message = 'Invalid Destination'
                self.show_info(message)


    def __init__(self, width, height, title):
        self.window = pygame.display.set_mode((width, height))
        self.tile_size = 40
        self.path = 'ressource/image/'
        self.floor = pygame.image.load('{}floor.jpg'.format(self.path))
        self.wall = pygame.image.load('{}wall.jpg'.format(self.path))
        self.bot_left = pygame.Rect(15, 615, 250, 50)
        self.bot_right = pygame.Rect(450, 615, 250, 50)
        self.font = pygame.font.Font(None, 20)
        pygame.display.set_caption(title)
