import pygame
import random

def main():
    pygame.init()


    screen_width = 600
    screen_height = 700

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Memory Game")

    #defining game variables


    #Card image
    class Card_img():
        def __init__(self, x, y, width, height, image_path, translate):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.image = pygame.image.load(image_path)
            self.translate = translate
            self.is_face_up = False
            self.card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            
        def draw(self):
            # card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, (255,255,255), self.card_rect)
            img_rect = self.image.get_rect(center = self.card_rect.center)
            if not self.is_face_up:
                pygame.draw.rect(screen, (100,100,100), self.card_rect)
            else:
                screen.blit(self.image, img_rect)

    #Card word
    class Card_word():
        def __init__(self, x, y, width, height, translate, image):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.font = pygame.font.Font(None, 32)
            self.color = (255, 255, 255)
            self.translate = translate
            self.image = image
            self.is_face_up = False
            self.card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            
        def draw(self):
            # card_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, self.card_rect)
            
            #Draw the word on the card
            text_surface = self.font.render(self.translate, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center = self.card_rect.center)
            
            if not self.is_face_up:
                pygame.draw.rect(screen, (100,100,100), self.card_rect)
            else:
                screen.blit(text_surface, text_rect)
                

    img = pygame.image.load("images/1.png")
    # card = Card_word(0,100,150,150, "Hello", img)
    # card2 = Card_img(0, 251, 150, 150, "images/1.png", "Hello")


    #Create the grid and the size of the cards
    bar_height = 100
    grid_size = 4
    card_width = screen_width // grid_size
    card_height = (screen_height - bar_height) // grid_size


    #Create the coordinates for the cards
    coordinates = []
    for row in range(grid_size):
        for column in range(grid_size):
            coordinates.append((column * card_width, row * card_height + bar_height))

    random.shuffle(coordinates)

    #Create the word-picture pairs

    pairs = []
    number_of_pairs = 8
    words = ["ankka", "kana", "lammas", "vuohi", "koira", "susi", "sammakko", "kissa"]
    for i in range(number_of_pairs):
        pairs.append((words[i], "images/" + str(i+1) + ".png"))


    #Create the cards

    word_cards = []
    word_index = 0
    for row in range(grid_size):
        for col in range(grid_size):
            if word_index < len(words):
                word = words[word_index]
                x, y = coordinates[word_index]
                word, image = pairs[word_index]
                card = Card_word(x, y, card_width, card_height, word, image)
                word_cards.append(card)
                word_index += 1

    pic_cards = []
    pic_index = 0
    for row in range(grid_size):
        for col in range(grid_size):
            if pic_index < number_of_pairs:
                pic = "images/" + str(pic_index) + ".png"
                x, y = coordinates[(pic_index)+number_of_pairs]
                word, image = pairs[(pic_index)]
                card = Card_img(x, y, card_width, card_height, image, word)
                pic_cards.append(card)
                pic_index += 1

    #find grid lines
    vertical_lines = [(card_width * col, bar_height, card_width * col, screen_height) for col in range(1, grid_size)]
    horizontal_lines = [(0, card_height * row + bar_height, screen_width, card_height * row + bar_height) for row in range(1, grid_size)]


    selected_cards = []
    matched_cards = []
    points = 0
    message_text = ""
    number_matched_pairs = 0



    def check_win_condition():
        return number_matched_pairs == number_of_pairs

    #Buttons
    button_width = 200
    button_height = 50
    button_color = (0, 255, 0) #green
    button_text_color = (255,255,255)

    def handle_button_click(button_rect, action):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                action()
                
    def start_new_game():
        main()
    def quit_game():
        pygame.quit()    

    #drawing buttons:
    new_game_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 - button_height, button_width, button_height)
    quit_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 + button_height, button_width, button_height)

    button_font = pygame.font.Font(None, 24)
    new_game_text = button_font.render("New Game", True, button_text_color)
    quit_text = button_font.render("Quit", True, button_text_color)
    

    

    #Game loop

    running = True
    while running:
        
        #if win
        if check_win_condition():
            #Display the winner screen
            screen.fill((0,0,0))
            winner_font = pygame.font.Font(None, 48)
            winner_text = winner_font.render("Congrats! You've won!", True, (255, 255, 255))
            winner_rect = winner_text.get_rect(center=(screen_width//2, screen_height//2 - 50))
            screen.blit(winner_text, winner_rect)
            
            
            #button positions
            button_y = screen_height // 2 + 50
            new_game_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, button_y, button_width, button_height)
            quit_button_rect = pygame.Rect(screen_width // 2 - button_width // 2, button_y + button_height + 10, button_width, button_height)
            
            #Check for clicks
            handle_button_click(new_game_button_rect, start_new_game)
            handle_button_click(quit_button_rect, quit_game)
            
            # Draw the buttons
            pygame.draw.rect(screen, button_color, new_game_button_rect)
            pygame.draw.rect(screen, button_color, quit_button_rect)

            # Render the button text
            new_game_text_rect = new_game_text.get_rect(center = new_game_button_rect.center)
            quit_text_rect = quit_text.get_rect(center = quit_button_rect.center)
            screen.blit(new_game_text, new_game_text_rect)
            screen.blit(quit_text, quit_text_rect)
            
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check for button clicks
                    handle_button_click(new_game_button_rect, start_new_game)
                    handle_button_click(quit_button_rect, quit_game)

            
            
        else:
            #if not win
            #Check for events
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #left mouse button
                        message_text = ""
                        mouse_pos = pygame.mouse.get_pos()
                        #check if the mouse click is on any of the cards:
                        for card in card_list:
                            if card.is_face_up:
                                continue
                            if card.card_rect.collidepoint(mouse_pos) and len(selected_cards) < 2:
                                card.is_face_up = True
                                selected_cards.append(card)
                                break
                    
                        
                    
                        
            screen.fill((0,0,0))
            
            #The top bar
            message_font = pygame.font.Font(None, 24)
            message_surface = message_font.render(message_text, True, (255,255,255))
            message_rect = message_surface.get_rect(center=(screen_width//2, bar_height //2))
            points_font = pygame.font.Font(None, 24)
            points_surface = message_font.render("Points: " + str(points), True, (255,255,255))
            points_rect = points_surface.get_rect(topright=(screen_width-10, bar_height//2))
            
            
            top_bar_rect = pygame.Rect(0, 0, screen_width, bar_height)
            pygame.draw.rect(screen, (0,0,255), top_bar_rect)
            screen.blit(message_surface, message_rect)
            screen.blit(points_surface, points_rect)
            
            
            
            card_list = word_cards + pic_cards
            
            for card in card_list:
                card.draw()
                
            #Draw the break lines
            for line in vertical_lines + horizontal_lines:
                pygame.draw.line(screen, (0,0,0), line[0:2], line[2:], 2)
            
            pygame.display.flip()
            
            if len(selected_cards) == 2:
                if selected_cards[0].translate == selected_cards[1].translate:
                    selected_cards[0].is_face_up = True
                    selected_cards[1].is_face_up = True
                    message_text = "Match found!"
                    points += 10
                    number_matched_pairs +=1
                    matched_cards.extend(selected_cards)
                    selected_cards = []
                    if number_matched_pairs == number_of_pairs:
                        pygame.time.wait(2000)
                else:
                    pygame.time.wait(1000)
                    selected_cards[0].is_face_up = False
                    selected_cards[1].is_face_up = False
                    message_text = "No match, try again!"
                    selected_cards = []
        
        pygame.display.flip()
        
    pygame.quit()

main()