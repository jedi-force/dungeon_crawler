import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CHARACTER_SIZE = 50
DOOR_SIZE = 50
ENEMY_SIZE = 50
BAR_WIDTH = 10
WALKWAY_WIDTH = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)

# Character class
class Character:
    def __init__(self, name, ability, x, y, health, image):
        self.name = name
        self.ability = ability
        self.x = x
        self.y = y
        self.health = health
        self.shielded = False  # Flag to indicate if the character is using the shield
        self.image = image

    def use_ability(self, target, allies):
        if self.ability == "super strength":
            print(f"{self.name} uses {self.ability} on the enemy!")
            target.reduce_health()
        elif self.ability == "shield":
            print(f"{self.name} activates {self.ability}!")
            self.shielded = True
            for ally in allies:
                if ally != self and ally.x > self.x:
                    ally.shielded = True
        else:
            print(f"{self.name} doesn't have the ability to attack enemies!")

    def reduce_health(self):
        self.health -= 20
        print(f"{self.name} health: {self.health}")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        font = pygame.font.Font(None, 24)
        text_health = font.render(f"{self.name}: {self.health} HP", True, WHITE)
        text_ability = font.render(f"Ability: {self.ability}", True, WHITE)
        screen.blit(text_health, (self.x, self.y - 2 * BAR_WIDTH))
        screen.blit(text_ability, (self.x, self.y - 3 * BAR_WIDTH))


# Enemy class
class Enemy:
    def __init__(self, x, y, health, image):
        self.x = x
        self.y = y
        self.health = health
        self.image = image

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        font = pygame.font.Font(None, 24)
        text_health = font.render(f"Enemy: {self.health} HP", True, WHITE)
        screen.blit(text_health, (self.x, self.y - 2 * BAR_WIDTH))

    def reduce_health(self):
        self.health -= 20
        print(f"Enemy health: {self.health}")

    def attack_player(self, player):
        if not player.shielded:
            print(f"{self} attacks {player.name}!")
            player.reduce_health()
        else:
            print(f"{self} attacks the shield!")

# Door class
class Door:
    def __init__(self, x, y, required_ability):
        self.x = x
        self.y = y
        self.required_ability = required_ability

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, DOOR_SIZE, DOOR_SIZE))

# Walkway class
class Walkway:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, self.width, self.height))

# ... (Previous code)

def draw_walkways(walkways):
    for walkway in walkways:
        walkway.draw()

def draw_characters(characters):
    for character in characters:
        character.draw()

def draw_doors(doors):
    for door in doors:
        door.draw()

def draw_enemies(enemies):
    for enemy in enemies:
        enemy.draw()

def draw_map():
    screen.fill(WHITE)
    draw_walkways(walkways)
    draw_characters(characters)
    draw_doors(doors)
    draw_enemies(enemies)
    pygame.display.flip()

#Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Family Adventure Game")

# Initialize keys_pressed dictionary
keys_pressed = {}

# Create walkways (defining the maze structure)
walkways = [
    Walkway(0, 0, WIDTH, WALKWAY_WIDTH),
    Walkway(0, 0, WALKWAY_WIDTH, HEIGHT),
    Walkway(WIDTH - WALKWAY_WIDTH, 0, WALKWAY_WIDTH, HEIGHT),
    Walkway(0, HEIGHT - WALKWAY_WIDTH, WIDTH, WALKWAY_WIDTH),
    Walkway(100, 0, WALKWAY_WIDTH, 300),
    Walkway(100, 300, 200, WALKWAY_WIDTH),
    Walkway(300, 300, WALKWAY_WIDTH, 200),
    Walkway(300, 500, 200, WALKWAY_WIDTH),
    Walkway(500, 300, WALKWAY_WIDTH, 200),
    Walkway(500, 0, WALKWAY_WIDTH, 300),
]

# Create doors
door1 = Door(200, 200, "teleportation")
door2 = Door(500, 500, "super strength")

doors = [door1, door2]

# Load images for characters and enemies
warrior_image = pygame.image.load("warrior.png")
wizard_image = pygame.image.load("wizard.png")
artificer_image = pygame.image.load("artificer.png")
goblin_image = pygame.image.load("goblin.png")

# Resize images to match CHARACTER_SIZE and ENEMY_SIZE
warrior_image = pygame.transform.scale(warrior_image, (CHARACTER_SIZE, CHARACTER_SIZE))
wizard_image = pygame.transform.scale(wizard_image, (CHARACTER_SIZE, CHARACTER_SIZE))
artificer_image = pygame.transform.scale(artificer_image, (CHARACTER_SIZE, CHARACTER_SIZE))
goblin_image = pygame.transform.scale(goblin_image, (ENEMY_SIZE, ENEMY_SIZE))

#Create characters
character1 = Character("Alice", "teleportation", 50, 50, 100, artificer_image)
character2 = Character("Bob", "super strength", 50, 50, 100, warrior_image)
character3 = Character("Charlie", "shield", 50, 50, 100, wizard_image)

characters = [character1, character2, character3]

#Create destination/goal
destination = random.choice([(100, 500), (500, 100), (700, 500), (500, 700)])

# Create enemies
enemy1 = Enemy(300, 300, 100, goblin_image)
enemy2 = Enemy(450, 450, 100, goblin_image)

enemies = [enemy1, enemy2]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for character in characters:
                if event.key == pygame.K_LEFT:
                    new_x = character.x - 10
                    new_y = character.y
                elif event.key == pygame.K_RIGHT:
                    new_x = character.x + 10
                    new_y = character.y
                elif event.key == pygame.K_UP:
                    new_x = character.x
                    new_y = character.y - 10
                elif event.key == pygame.K_DOWN:
                    new_x = character.x
                    new_y = character.y + 10

                # Check if the new position is within a walkway
                if any(
                    walkway.x < new_x < walkway.x + walkway.width
                    and walkway.y < new_y < walkway.y + walkway.height
                    for walkway in walkways
                ):
                    character.move(new_x - character.x, new_y - character.y)
                    
        print("Level up!")
        destination = random.choice([(100, 500), (500, 100), (700, 500), (500, 700)])

    # Update game logic here

    # Example: Characters attack enemies when they are nearby
    for character in characters:
        for enemy in enemies:
            distance = ((character.x - enemy.x) ** 2 + (character.y - enemy.y) ** 2) ** 0.5
            if distance < 50:  # Adjust this value based on your game's scale
                character.use_ability(enemy, characters)

    # Example: Enemies attack players when they are nearby
    for enemy in enemies:
        for character in characters:
            distance = ((enemy.x - character.x) ** 2 + (enemy.y - character.y) ** 2) ** 0.5
            if distance < 50:  # Adjust this value based on your game's scale
                enemy.attack_player(character)

    # Draw the map
    draw_map()

    # Introduce a short delay to control the speed of character movement
    pygame.time.delay(50)

# Quit Pygame
pygame.quit()
sys.exit()