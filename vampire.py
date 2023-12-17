import pygame
import sys
import random
import math
import time
from PIL import Image

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
KHAKI = (195, 176, 145)

# Constants
WIDTH, HEIGHT = 800, 650
PLAYER_SIZE = 150
VAMPIRE_SIZE = 30
FPS = 60
HEALTH_BAR_HEIGHT = 10
HEALTH_BAR_COLOR = GREEN  # Green color for a healthy bar
BACKGROUND = []
CHARACTER = []
VAMPIRE = []

# Variables
selected_character = None

def ability_movement(weapon, move_type, vampire_rect):
    if move_type == "random" or move_type == "nearest":
        weapon_image = weapons[weapon][-1]
        weapon_image = pygame.transform.scale(weapon_image, (vampire.rect.width * 2, vampire.rect.height))
        for i in range(1, 360 + 1, 3):
            rotated_image = pygame.transform.rotate(weapon_image, i)
            weapon_rect = weapon_image.get_rect(center=vampire_rect.center)
            screen.blit(rotated_image, weapon_rect)
            pygame.display.flip()
    elif move_type == "all":
        weapon_image = weapons[weapon][-1]
        weapon_image = pygame.transform.scale(weapon_image, (player.rect.width * 5, player.rect.height * 5))
        for _ in range(2):    
            for i in range(1, 360 + 1, 100):
                rotated_image = pygame.transform.rotate(weapon_image, i)
                weapon_rect1 = weapon_image.get_rect(center=vampire_rect.center)
                screen.blit(rotated_image, weapon_rect1)

                weapon_rect2 = weapon_image.get_rect(topleft=vampires[random.randint(0, len(vampires) - 1)].rect.center)
                screen.blit(rotated_image, weapon_rect2)
                pygame.display.flip()
    elif move_type == "nearest" and weapon != "axe":
        pass
        # # Calculate the direction vector towards the player
        # direction = pygame.math.Vector2(vampire_rect.x - player.rect.x, vampire_rect.y - player.rect.y)

        # # Check if the length of the direction vector is greater than zero
        # if direction.length() > 0:
        #     direction.normalize_ip()
        # else:
        #     # If the length is zero, add a small random perturbation to the direction
        #     perturbation = pygame.math.Vector2(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        #     direction = direction + perturbation
        #     direction.normalize_ip()
        
        # weapon_image = weapons[weapon][-1]
        # weapon_image = pygame.transform.scale(weapon_image, (vampire.rect.width * 2, vampire.rect.height))
        # weapon_rect = weapon_image.get_rect(center=player.rect.center)

        # # Update the vampire's position based on the direction and speed
        # weapon_x_touching = False
        # weapon_y_touching = False
        # while not(weapon_x_touching) and not(weapon_y_touching):
        #     if not weapon_rect.x in range(vampire_rect.x - 10, vampire_rect.x + 10,):
        #         weapon_rect.x += direction.x * 4
        #     else:
        #         weapon_x_touching = True
        #     if not weapon_rect.x in range(vampire_rect.x - 10, vampire_rect.x + 10,):
        #         weapon_rect.y += direction.y * 4
        #     else:
        #         weapon_y_touching = True
        #     screen.blit(rotated_image, weapon_rect)
        #     pygame.display.flip()
    elif move_type == "LR":
        weapon_image = weapons[weapon][-1]
        weapon_image = pygame.transform.scale(weapon_image, (player.rect.width, player.rect.height))
        weapon_rect = weapon_image.get_rect(topleft=(player.rect.x, player.rect.y))
        angle = 100
        for i in range(5):
            angle *= -1
            # Rotate image
            rotated_image = pygame.transform.rotate(weapon_image, angle)
            rotated_rect = rotated_image.get_rect(center=player.rect.center)
            pygame.time.delay(20)
            #pygame.draw.rect(screen, WHITE, rotated_rect)
            screen.blit(rotated_image, rotated_rect.topleft)
            pygame.display.flip()
    else:
        weapon_image = weapons[weapon][-1]
        weapon_image = pygame.transform.scale(weapon_image, (player.rect.width, player.rect.height))
        weapon_rect = weapon_image.get_rect(topleft=(player.rect.x, player.rect.y))
        for i in range(1, 360 + 1, 5):
            # Rotate image
            rotated_image = pygame.transform.rotate(weapon_image, i)
            rotated_rect = rotated_image.get_rect(center=player.rect.center)
            #pygame.time.delay(50)
            #pygame.draw.rect(screen, WHITE, rotated_rect)
            screen.blit(rotated_image, rotated_rect.topleft)
            pygame.display.flip()

def set_images():
    global BACKGROUND, CHARACTER, VAMPIRE, VAMP_CHIM

    background = pygame.image.load("background.jpg") 
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect(topleft=(0, 0))
    screen.blit(background, background_rect)


    # Draw player
    character_image = pygame.image.load(f"{selected_character}.png")  # Replace with actual image path

    # New ratios
    new_height = PLAYER_SIZE
    new_width = int(new_height * (character_image.get_width() / character_image.get_height()))

    character_image = pygame.transform.scale(character_image, (new_width, new_height))  # Resize images
    character_rect = character_image.get_rect(topleft=(player.rect.x, player.rect.y))
    character_rect.width /= 1.5
    #character_rect.height /= 
    player.rect = character_rect
    screen.blit(character_image, character_rect)

    # Draw Chim
    chim_image = pygame.image.load("Chim.png")
    chim_image = pygame.transform.scale(chim_image, (new_width, new_height))  # Resize images
    chim_rect = chim_image.get_rect(topleft=(vampires[0].rect.x, vampires[0].rect.y))
    chim_rect.width *= 1.25
    #character_rect.height /= 
    screen.blit(chim_image, chim_rect)

    # Draw vampire
    vampire_height = new_height / 2
    vampire_image = pygame.image.load("goblin.png")
    new_width = int(vampire_height * (vampire_image.get_width() / vampire_image.get_height()))
    vampire_image = pygame.transform.scale(vampire_image, (new_width, vampire_height))  # Resize images
    vampire_rect = character_image.get_rect(topleft=(vampires[0].rect.x, vampires[0].rect.y))
    vampire_rect.width /= 3
    vampire_rect.height /= 3



    BACKGROUND = [background, background_rect]
    CHARACTER = [character_image, character_rect]
    VAMPIRE = [vampire_image, vampire_rect]
    VAMP_CHIM = [chim_image, chim_rect]


# Draw everything
def draw_everything():
    global BACKGROUND, CHARACTER, VAMPIRE

    screen.fill(WHITE)

    BACKGROUND[1] = BACKGROUND[0].get_rect(topleft=(BACKGROUND[1].x, BACKGROUND[1].y))
    screen.blit(BACKGROUND[0], BACKGROUND[1])

    # Draw health bar
    health_bar_width = int((player.health / 100) * (WIDTH / 2.1))
    pygame.draw.rect(screen, BLACK, pygame.Rect(5, 5, health_bar_width + 5, HEALTH_BAR_HEIGHT + 5))
    pygame.draw.rect(screen, HEALTH_BAR_COLOR, pygame.Rect(7, 7, health_bar_width, HEALTH_BAR_HEIGHT))

    # Draw powerup bar
    powerup_bar_width = int((len(player.points) / Player.powerup_level) * (WIDTH / 2.1))
    pygame.draw.rect(screen, BLACK, pygame.Rect(WIDTH / 2, 5, powerup_bar_width + 5, HEALTH_BAR_HEIGHT + 5))
    pygame.draw.rect(screen, BLUE, pygame.Rect((WIDTH / 2) + 2, 7, powerup_bar_width, HEALTH_BAR_HEIGHT))


    # New ratios
    new_height = 100

    #player.rect = CHARACTER[0].get_rect(topleft=(player.rect.x, player.rect.y))
    player.rect.width = CHARACTER[1].width
    player.rect.height = CHARACTER[1].height
    #test
    #pygame.draw.rect(screen, WHITE, player.rect)
    screen.blit(CHARACTER[0], player.rect)
    
    

    # Draw vampires
    for vamp in vampires:
        if vamp.isChim:
            image = VAMP_CHIM[0]
            rect = VAMP_CHIM[1]
        else:
            image = VAMPIRE[0]
            rect = VAMPIRE[1]
        vamp_rect = image.get_rect(topleft=(vamp.rect.x, vamp.rect.y))
        vamp.rect = vamp_rect
        vamp.rect.height = rect.height
        vamp.rect.width = rect.width
        screen.blit(image, vamp_rect)
        #test
        #pygame.draw.rect(screen, BLUE, vamp.rect)

    #Draw  points
    for point in points:
        pygame.draw.rect(screen, point.color, point.rect)
    
    pygame.display.flip()


SCROLL_SPEED = 80
SCROLL_AREA_HEIGHT = 400

# Character selection screen
def character_selection():
    global selected_character
    font2 = pygame.font.Font(None, 20)

    scroll_offset = 0  # Initial scroll offset
    scrolling = False

    screen.fill(BLACK)

    choose_character_text = font.render("Choose Your Character", True, WHITE)
    choose_character_rect = choose_character_text.get_rect(center=(WIDTH // 2, 40))
    screen.blit(choose_character_text, choose_character_rect)

    character_options = list(characters.keys())
    option_x, option_y = WIDTH // 2, HEIGHT // 2
    spacing = 350  # Increased spacing
    characters_per_row = 2  # Two characters per row
    row_count = 0

    character_images = {}  # Dictionary to store character images and their rects

    for character in character_options:
        character_image = pygame.image.load(f"{character}.png")  # original image not resized
        # New ratios
        new_height = 300
        new_width = int(new_height * (character_image.get_width() / character_image.get_height()))

        character_image = pygame.transform.scale(character_image, (new_width, new_height))  # Resize images
        character_rect = character_image.get_rect(topleft=(option_x - 50, option_y - 100))
        screen.blit(character_image, character_rect)
        character_images[character] = (character_image, character_rect)  # Store character image and rect

        # Draw text below character images
        option_text = font2.render(f"{character}, {descriptions[character]}", True, WHITE)
        option_rect = option_text.get_rect(center=(option_x, option_y + 200))
        screen.blit(option_text, (option_rect.x, option_rect.y + scroll_offset))

        abilities_text = font2.render(f"Abilities: {characters[character]}", True, WHITE)
        abilities_rect = abilities_text.get_rect(center=(option_x, option_y + 220))
        screen.blit(abilities_text, (abilities_rect.x, abilities_rect.y + scroll_offset))

        option_x += spacing

        if option_x >= WIDTH - (WIDTH // 2) + 20:
            option_x = (WIDTH // 2) + 20
            option_y += spacing + 30
            row_count += 1

    # Calculate the total height needed for characters
    total_height = option_y - HEIGHT // 4

    pygame.display.flip()

    while selected_character is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for character, (character_image, character_rect) in character_images.items():
                    if character_rect.collidepoint(mouse_x, mouse_y):
                        selected_character = character
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    scroll_offset += SCROLL_SPEED
                    scrolling = True
                elif event.key == pygame.K_DOWN:
                    scroll_offset -= SCROLL_SPEED
                    scrolling = True

        # Add scrolling effect
        if scrolling:
            if scroll_offset > 0:
                scroll_offset = 0
            elif scroll_offset < -(total_height - HEIGHT // 1.5):
                scroll_offset = -(total_height - HEIGHT // 1.5)
            scrolling = False

        # Draw everything
        screen.fill(BLACK)
        choose_character_text = font.render("Choose Your Character", True, WHITE)
        choose_character_rect = choose_character_text.get_rect(center=(WIDTH // 2, 40))
        screen.blit(choose_character_text, choose_character_rect)

        option_x, option_y = (WIDTH // 4) + 20, HEIGHT // 4
        for character in character_options:
            character_image, character_rect = character_images[character]
            character_rect.topleft = (option_x - 50, option_y - 100 + scroll_offset)
            screen.blit(character_image, character_rect)

            # Draw text below character images
            option_text = font2.render(f"{character}, {descriptions[character]}", True, WHITE)
            option_rect = option_text.get_rect(center=(option_x + 25, option_y + 220))
            screen.blit(option_text, (option_rect.x, option_rect.y + scroll_offset))

            abilities_text = font2.render(f"Abilities: {characters[character]}", True, WHITE)
            abilities_rect = abilities_text.get_rect(center=(option_x + 25, option_y + 240))
            screen.blit(abilities_text, (abilities_rect.x, abilities_rect.y + scroll_offset))

            option_x += spacing

            if option_x >= WIDTH - (WIDTH // 4) + 20:
                option_x = (WIDTH // 4) + 20
                option_y += spacing + 30

        # Draw the choose your character text
        choose_character_text = font.render("Choose Your Character", True, WHITE)
        choose_character_rect = choose_character_text.get_rect(center=(WIDTH // 2, 40))
        choose_background_rect = pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, WIDTH, 50))
        screen.blit(choose_character_text, choose_character_rect)
        
        # Draw a scroll bar
        pygame.draw.rect(screen, WHITE, (WIDTH - 20, 0, 10, HEIGHT))  # Adjusted the height
        scroll_bar_length = int((HEIGHT // 1.5) / total_height * (HEIGHT // 1.5))
        scroll_bar_pos = int((scroll_offset / -(total_height - HEIGHT // 1.5)) * (HEIGHT // 1.5))
        pygame.draw.rect(screen, BLUE, (WIDTH - 18, 50 + scroll_bar_pos, 6, scroll_bar_length))

        pygame.display.flip()
        clock.tick(FPS)
        pygame.time.delay(50)

                

def spawn_point(x, y):
    point = Point(x, y)
    points.append(point)

def remove(mylist, item, player):
    player.score += 1 * vampire_speed
    spawn_point(item.rect.x, item.rect.y)
    mylist.remove(item)

def collect_points():
    for point in points[:]:
        if point.detection_rect.colliderect(player.rect):
            player.score += 10  # Adjust the score based on your preference
            points.remove(point)
            player.points.append(point)

powerups = {
            "weapon_freq": 1,
            "weapon_num": 1.5,
            "health_regen": 1,
            "speed": 1,
            "weapon": 0
            }


weapons = {
            "knives": [.5, "LR", 100], 
            "sword": [1, "LR", 150],  
            "bombs": [2, "random", 20],
            "staff": [2, "circle", 200], 
            "enchantment": [4, "circle", 250], 
            "spell": [20, "all", None], 
            "axe": [10, "nearest", 2],
            "arrows": [1, "random", 10], 
            "familiar": [5, "nearest", 1],
            "necromancy": [20, "all", None]
            }


characters = {
    "Biba": "knives", 
    "Delilah": "bombs", 
    "Ethan": "axe", 
    "Kayte": "arrows", 
    "AJ": "spell", 
    "Rhema": "enchantment",        
    "Kiyel": "sword", 
    "Aanai": "staff", 
    "Viggo": "familiar",
    "Victoria": "necromancy"
    }

descriptions = {
    "Biba" : "the Rouge", 
    "Delilah" : "the Artificer", 
    "Ethan": "the Barbarian", 
    "Kayte": "the Archer", 
    "AJ" : "the Wizard", 
    "Rhema": "the Bard",        
    "Kiyel": "the Warrior", 
    "Aanai": "the Paladin", 
    "Viggo": "the Druid",
    "Victoria": "the Warlock"
    }

class Weapon:
    @staticmethod
    def execute_move(move_type, weapon_freq, weapon_num, player, vampires, weapon):
        
        if move_type == "LR":
            ability_movement(weapon, move_type, None)
            # Weapon attacks left to right to attack but remains close to the player
            #attack_range = range(player.rect.x + player.rect.width, player.rect.x + player.rect.width + weapon_freq * 2, 50)
            attack_rect = pygame.Rect(player.rect.x - 30, player.rect.y, player.rect.width + weapon_num, player.rect.height)
            #for x in attack_range:
            for vampire in vampires:
                if vampire.rect.colliderect(attack_rect):
                    #dissolve_effect(vampire)
                    remove(vampires, vampire, player)
                    break

        elif move_type == "random":
            # Weapon attacks a random position on the board not including the player
            for _ in range(weapon_num):
                x = random.randint(0, WIDTH - 1)
                y = random.randint(0, HEIGHT - 1)
                for vampire in vampires:
                    if vampire.rect.collidepoint(x, y):
                        #ability_movement(weapon, move_type, pygame.Rect(x, y, 50, 50))
                        remove(vampires, vampire, player)
                        ability_movement(weapon, move_type, vampire.rect)
                        #dissolve_effect(vampire)
                        break

        elif move_type == "circle":
            # Weapon attacks in a circular motion around the player
            #for angle in range(0, 360, weapon_num):
            #radian_angle = math.radians(angle)
            #x = int(player.rect.centerx * math.cos(radian_angle))
            #y = int(player.rect.centery * math.sin(radian_angle))

            ability_movement(weapon, move_type, vampires[0].rect)
            attack_rect = pygame.Rect(player.rect.x, player.rect.y, weapon_num, weapon_num)

            for vampire in vampires:
                if vampire.rect.colliderect(attack_rect):
                    remove(vampires, vampire, player)
                    break

        elif move_type == "all":
            # Weapon attacks all vampires on the screen
            for vampire in vampires:
                remove(vampires, vampire, player)
                ability_movement(weapon, move_type, vampire.rect)
                #dissolve_effect(vampire.rect)
            vampires.clear()

        elif move_type == "nearest":
            # Weapon attacks the nearest enemy
            for _ in range(weapon_num):
                if vampires:
                    p = player.rect
                    nearest_vampire = min(vampires, key=lambda v: pygame.math.Vector2(p.x, p.y).distance_to(pygame.math.Vector2(v.rect.x, v.rect.y)))
                    #dissolve_effect(nearest_vampire)
                    ability_movement(weapon, move_type, nearest_vampire.rect)
                    remove(vampires, nearest_vampire, player)
                    
    

class Player:
    powerup_level = 10
    max_health = 100

    def __init__(self, type="Biba", health=100, speed=5):
        self.type = type
        self.speed = speed
        self.abilities = {}
        self.health = health
        self.rect = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)
        self.add_intials()
        self.score = 0
        self.points = []
        self.regen = 1
    
    def add_intials(self):
        self.abilities[characters[self.type]] = weapons[characters[self.type]]
    
    # def add_ability(self, weapon):
    #     if weapon in self.abilities.keys():
    #         self.abilities[weapon][0] += 1
    #     else:
    #         self.abilities[weapon] = weapons[str]

    def level_up(self):
        if Player.powerup_level <= len(self.points):
            self.points = []
            Player.powerup_level += 1
            self.generate_powerups()
    
    def health_regen(self, curr_time, prev_time):
        if int(curr_time) - int(prev_time) > 1 & player.health < Player.max_health:
            player.health += self.regen

    def add_powerup(self, powerup, num, weapon=None):
        if powerup == "health_regen":
            self.regen += num
        elif powerup == "speed":
            self.speed = round(self.speed + num)
        elif weapon != None:
            
            if powerup == "weapon_freq":
                self.abilities[weapon] = [self.abilities[weapon][0] + num, weapon, self.abilities[weapon][2]]
            elif powerup == "weapon_num":
                self.abilities[weapon] = [self.abilities[weapon][0], weapon, round(self.abilities[weapon][2] * num)]
            elif powerup == "weapon":
                self.abilities[weapon] = weapons[weapon]
                
    def generate_powerups(self):
        list_choices = [random.choice(list(powerups.keys())) for _ in range(3)]
        new_abilities = [ability for ability in weapons if ability not in self.abilities]
        
        for i in range(len(list_choices)):
            if list_choices[i] == "weapon":
                new_weapon = random.choice(new_abilities)
                list_choices[i] = ["weapon", new_weapon]
            elif list_choices[i] == "weapon_freq" or list_choices[i] == "weapon_num":
                weapon_type = random.choice(list(self.abilities.keys()))
                list_choices[i] = [list_choices[i], weapon_type]
        return list_choices
    
    # Draw on screen so that it gives the user a choice to pick one of the three random powerups. If after 4 seconds, 
    # no powerup is picked, a random powerup from the list in picked and the game resumes. 
    def powerup_selection(self):
        list_choices = self.generate_powerups()
        selected_powerup = None
        start_time = pygame.time.get_ticks()

        while selected_powerup is None:
            screen.fill(WHITE)

            # Draw powerup options
            font1 = pygame.font.Font(None, 36)
            text1 = font1.render("You've leveled up!", True, BLACK)
            text2 = font1.render("Choose a Powerup", True, BLACK)
            text_rect1 = text1.get_rect(center=(WIDTH // 2, 40))
            text_rect2 = text2.get_rect(center=(WIDTH // 2, 80))
            screen.blit(text1, text_rect1)
            screen.blit(text2, text_rect2)

            option_x = WIDTH // 5 - 20
            option_y = HEIGHT // 2 - 100
            font2 = pygame.font.Font(None, 25)
            spacing = 50
            for powerup in list_choices:
                new_height = 150
                new_width = int(new_height * (150 / new_height))  # Adjust this ratio if needed
                option_rects = []
                if isinstance(powerup, list):
                    powerup_image = pygame.image.load(f"{powerup[0]}.png")  # original image not resized
                    if powerup[0] == "weapon_freq":
                        option_text = [f"Increase rate of", f"fire for {powerup[1]}"]
                        #option_rects = []
                        #option_text = font2.render(f"Increase rate of fire for {powerup[1]}", True, BLACK)
                    elif powerup[0] == "weapon_num":
                        option_text = [f"Increase rate of", f"weapons for {powerup[1]}"]
                        #option_text = font2.render(f"Increase number of weapons for {powerup[1]}", True, BLACK)
                    elif powerup[0] == "weapon":
                        option_text = [f"Add new ability:", f"{powerup[1]}"]
                        #option_text = font2.render(f"Add new ability: {powerup[1]}", True, BLACK)    
                else:
                    powerup_image = pygame.image.load(f"{powerup}.png")  # original image not resized
                    if powerup == "health_regen":
                        option_text = [f"Increase health"]
                    elif powerup == "speed":
                        option_text = [f"Increase speed"]
                #pygame.Rect(option_x - 20, option_y + 20, new_width + 20, new_height + 100)
                powerup_background = pygame.draw.rect(screen, KHAKI, pygame.Rect(option_x - 15, option_y, new_width + 25, new_height + 100))
                powerup_image = pygame.transform.scale(powerup_image, (new_width, new_height))
                powerup_rect = powerup_image.get_rect(topleft=(option_x, option_y))
                screen.blit(powerup_image, powerup_rect)

                # Add new line breaks for the text for each powerup
                text_option_y = option_y + new_height + 40
                for i, line in enumerate(option_text):
                    line_text = font2.render(line, True, BLACK)
                    line_rect = line_text.get_rect(center=(option_x + spacing + 20, text_option_y))  # Adjust spacing as needed
                    screen.blit(line_text, line_rect)
                    option_rects.append(line_rect)
                    text_option_y += 40

                #option_rect = option_text.get_rect(center=(option_x + spacing, option_y + new_height + 10))
                #screen.blit(option_text, option_rect)

                option_x += (WIDTH // 5) + spacing

            pygame.display.flip()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Check which option was clicked
                    option_y = HEIGHT // 2 - 50
                    for i, powerup in enumerate(list_choices):
                        option_rect = pygame.Rect(WIDTH // 3 * i, option_y, WIDTH // 3, new_height + 10)
                        if option_rect.collidepoint(mouse_x, mouse_y):
                            selected_powerup = powerup
                            break

                    

            # Check if 4 seconds have passed without a selection
            if pygame.time.get_ticks() - start_time > 4000:
                selected_powerup = random.choice(list_choices)

        self.call_add_powerup(selected_powerup)
        return selected_powerup

    def call_add_powerup(self, powerup):
        if isinstance(powerup, list):
            weapon = powerup[1]
            self.add_powerup(powerup[0], powerups[powerup[0]], weapon)  
        else:
            self.add_powerup(powerup, powerups[powerup])
  

    


class Vampire:
    def __init__(self, health=10, attack=1, isChim=False):
        self.attack = attack
        self.speed = 1
        self.health = health
        self.rect = pygame.Rect(random.randint(0, WIDTH - VAMPIRE_SIZE),
                                random.randint(0, HEIGHT - VAMPIRE_SIZE),
                                VAMPIRE_SIZE, VAMPIRE_SIZE)
        self.offense_rect = pygame.Rect(random.randint(0, WIDTH - VAMPIRE_SIZE),
                                random.randint(0, HEIGHT - VAMPIRE_SIZE),
                                VAMPIRE_SIZE, VAMPIRE_SIZE)
        self.isChim = isChim

    def spawn_chim(self):
        if self.isChim:
            self.rect.height = player.rect.height
            self.rect.width = player.rect.width

            vampires.append(self)
        
class Point:
    def __init__(self, x, y):
        self.detection_rect = pygame.Rect(x, y, 150, 150)
        self.rect = pygame.Rect(x, y, 10, 10)
        self.color = YELLOW  # Yellow color for points

# Dissolve effect function
def dissolve_effect(object):
    dissolve_duration = 1000  # in milliseconds
    dissolve_start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - dissolve_start_time < dissolve_duration:
        # Gradually change the color of the vampire to simulate dissolving
        progress = (pygame.time.get_ticks() - dissolve_start_time) / dissolve_duration
        object.color = interpolate_color(WHITE, RED, progress)
        pygame.draw.rect(screen, object.color, object.rect)
        
        # Draw everything
        draw_everything()

        

        # Cap the frame rate
        clock.tick(FPS)

# Color interpolation function
def interpolate_color(color_start, color_end, progress):
    r = int(color_start[0] + (color_end[0] - color_start[0]) * progress)
    g = int(color_start[1] + (color_end[1] - color_start[1]) * progress)
    b = int(color_start[2] + (color_end[2] - color_start[2]) * progress)
    return (r, g, b)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("background.jpg") 
pygame.display.set_caption("Dungeon Crawler")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 100)

# Set points
points = []

# Character selection screen
character_selection()
player = Player(selected_character)

# Create vampires
vampires = []

# Spawn new vampire function
def spawn_new_vampire():
    player_center = pygame.math.Vector2(player.rect.centerx, player.rect.centery)

    # Create a new vampire and add to the list, ensuring it spawns away from the player
    new_vampire = Vampire()
    vampire_center = pygame.math.Vector2(new_vampire.rect.centerx, new_vampire.rect.centery)
    
    # Set the minimum distance between player and vampire (adjust as needed)
    min_distance = 200

    while player_center.distance_to(vampire_center) < min_distance:
        new_vampire = Vampire()
        vampire_center = pygame.math.Vector2(new_vampire.rect.centerx, new_vampire.rect.centery)

    vampires.append(new_vampire)

for _ in range(10):  # Use list comprehension to create multiple vampires
    spawn_new_vampire()


# Timer variables
spawn_timer = pygame.time.get_ticks()
spawn_interval = 3000  # 3 seconds in milliseconds
speed_timer = pygame.time.get_ticks()
speed_interval = 60000
current_seconds = round(time.time())
move_executed = False

# Set initial vampire speed
vampire_speed = 1

# Set initial vampire numbers
vampires_num = 10

set_images()

# Add weapon images to weapons dictionary
for weapon in weapons.keys():
    weapon_image = pygame.image.load(f"{weapon}.png")  # Replace with actual image path
    #weapon_image = pygame.transform.scale(weapon_image, (player.rect.width(), new_height)) 
    weapons[weapon].append(weapon_image)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= player.speed
        if player.rect.right < 0:
            player.rect.x = WIDTH  # Wrap around to the right edge

    if keys[pygame.K_RIGHT]:
        player.rect.x += player.speed
        if player.rect.left > WIDTH:
            player.rect.x = -PLAYER_SIZE  # Wrap around to the left edge

    if keys[pygame.K_UP] and player.rect.top > 0:
        player.rect.y -= player.speed
    if keys[pygame.K_DOWN] and player.rect.bottom < HEIGHT:
        player.rect.y += player.speed

    # Spawn new vampire every 10 seconds
    current_time = pygame.time.get_ticks()
    if current_time - spawn_timer >= spawn_interval:  # time based
        spawn_timer = current_time

        spawn_new_vampire()

    if len(vampires) < vampires_num:
        vampires.append(Vampire())

    if current_time - speed_timer >= speed_interval:  # time based
        vampire_speed += 0.5
        vamp_chim = Vampire(10, 10, True)
        vamp_chim.spawn_chim()
        speed_timer = current_time

    # Collect points after vampire dies
    collect_points()

    # Check if the player has collected enough points to trigger powerup selection
    #player.level_up()

    # Check if the player should choose a powerup
    if len(player.points) >= Player.powerup_level:
        player.level_up()
        selected_powerup = player.powerup_selection()
        #player.add_powerup(selected_powerup)

    # Vampire movement
    for vampire in vampires:

        # Calculate the direction vector towards the player
        direction = pygame.math.Vector2(player.rect.x - vampire.rect.x, player.rect.y - vampire.rect.y)

        # Check if the length of the direction vector is greater than zero
        if direction.length() > 0:
            direction.normalize_ip()
        else:
            # If the length is zero, add a small random perturbation to the direction
            perturbation = pygame.math.Vector2(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
            direction = direction + perturbation
            direction.normalize_ip()

        # Update the vampire's position based on the direction and speed
        vampire.rect.x += direction.x * vampire_speed
        vampire.rect.y += direction.y * vampire_speed

        # Update offense_rect with the new position
        #vampire.offense_rect.topleft = vampire.rect.topleft

        # Check for collision with other vampires and adjust position if necessary
        for other_vampire in vampires:
            if vampire != other_vampire and vampire.rect.colliderect(other_vampire.rect):
                # Calculate the direction vector away from the colliding vampire
                avoid_direction = pygame.math.Vector2(vampire.rect.x - other_vampire.rect.x, vampire.rect.y - other_vampire.rect.y)
                avoid_direction.normalize_ip()

                # Adjust the vampire's position away from the colliding vampire
                vampire.rect.x += avoid_direction.x * vampire_speed + 5
                vampire.rect.y += avoid_direction.y * vampire_speed + 5

        # Check for collision with player
        if player.rect.colliderect(vampire.rect):
            player.health -= vampire.attack  # Set player health to 0


    # Check for collision with weapon
    if int(time.time()) - int(current_seconds) > 1:
        move_executed = False
        current_seconds = int(time.time())

    for key in player.abilities.keys():
        value = player.abilities[key]
        weapon_stats = value[0]
        move_type = value[1]
        weapon_num = value[2]
        if ((int(time.time()) % weapon_stats == 0) & (not(move_executed))):
            move_executed = True
            Weapon.execute_move(move_type, weapon_stats, weapon_num, player, vampires, key)

    # Draw everything
    draw_everything()

    # Check for game over
    if player.health <= 0:
        #restart_clicked = False
        # Game over screen
        #while not restart_clicked:
        screen.fill(BLACK)

        game_over_text = game_over_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)

        score_text = font.render("Your Score: {}".format(player.score), True, RED)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(score_text, score_rect)

        pygame.display.flip()
        pygame.time.wait(2000)

        # Restart button
        
        # restart_text = font.render("Restart...?", True, RED)
        # restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        # screen.blit(restart_text, restart_rect)
        # pygame.display.flip()
        # pygame.time.wait(1000)

        # # Check if restart button is clicked
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # mouse_click = pygame.event.get()
        # if restart_rect.colliderect(restart_rect):

        # Restart the game
        player = Player(selected_character)
        vampires = []
        vampires_num = 10
        vampire_speed = 1
        for _ in range(10):  # Use list comprehension to create multiple vampires
            spawn_new_vampire()
        points = []

        #     restart_clicked = True
        # pygame.display.flip()

        # Wait for a key press to exit
        #pygame.time.wait(1000)  # Wait for 2 seconds

        #pygame.display.flip()

        # Wait for a key press to exit
        #pygame.time.wait(2000)  # Wait for 2 seconds
        #pygame.quit()
        #sys.exit()

    # Cap the frame rate
    clock.tick(FPS)

