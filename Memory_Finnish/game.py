import pygame
import random

pygame.init()


screen_width = 600
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

#defining game variables

class Card_img():
    def __init__(self, x, y, width, height, image_path, translate):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.translate = translate
        self.is_face_up = False
        
    def draw(self):
        card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255,255,255), card_rect)
        screen.blit(self.image, (self.x, self.y))

class Card_word():
    def __init__(self, x, y, width, height, word, picture):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 32)
        self.color = (255, 255, 255)
        self.word = word
        self.translate = picture
        self.is_face_up = False
        
    def draw(self):
        card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, card_rect)
        
        #Draw the word on the card
        text_surface = self.font.render(self.word, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center = card_rect.center)
        screen.blit(text_surface, text_rect)

img = pygame.image.load("images/1.png")
# card = Card_word(0,100,150,150, "Hello", img)
# card2 = Card_img(0, 251, 150, 150, "images/1.png", "Hello")

bar_height = 100
grid_size = 4
card_width = screen_width // grid_size
card_height = (screen_height - bar_height) // grid_size


#Create the cards

#word list
words = ["ankka", "kana", "lammas", "vuohi", "koira", "susi", "sammakko", "kissa"]

word_cards = []
word_index = 0
for row in range(grid_size):
    for col in range(grid_size):
        if word_index < len(words):
            word = words[word_index]
            card = Card_word(card_width * col, card_height * (row + 2) + bar_height, card_width, card_height, word, img)
            word_cards.append(card)
            word_index += 1
        

pic_cards = []
pic_index = 1
num_of_pics = 8
for row in range(grid_size):
    for col in range(grid_size):
        if pic_index <= num_of_pics:
            pic = "images/" + str(pic_index) + ".png"
            card = Card_img(card_width * col, card_height * row + bar_height, card_width, card_height, pic, "nice")
            pic_cards.append(card)
            pic_index += 1

#find grid lines
vertical_lines = [(card_width * col, bar_height, card_width * col, screen_height) for col in range(1, grid_size)]
horizontal_lines = [(0, card_height * row + bar_height, screen_width, card_height * row + bar_height) for row in range(1, grid_size)]

#Game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0,0,0))
    
    #The top bar
    
    top_bar_rect = pygame.Rect(0, 0, screen_width, bar_height)
    pygame.draw.rect(screen, (0,0,255), top_bar_rect)
    
    
    random.shuffle(word_cards)
    random.shuffle(pic_cards)
    card_list = word_cards + pic_cards
    for card in card_list:
        card.draw()
        
    # for card in word_cards:
    #     card.draw()
    
    # for card in pic_cards:
    #     card.draw()
    
    #Draw the break lines
    for line in vertical_lines + horizontal_lines:
        pygame.draw.line(screen, (0,0,0), line[0:2], line[2:], 2)
    
    pygame.display.flip()
    
pygame.quit()