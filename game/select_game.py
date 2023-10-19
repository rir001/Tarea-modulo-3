import pygame
import random
import os


pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Selection Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 30)


correct_images_folder = "correct_images"
incorrect_images_folder = "incorrect_images"
correct_images = [pygame.image.load(os.path.join(correct_images_folder, filename)) for filename in os.listdir(correct_images_folder)]
incorrect_images = [pygame.image.load(os.path.join(incorrect_images_folder, filename)) for filename in os.listdir(incorrect_images_folder)]

image1 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
image2 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
image3 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
image4 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))

correct_image = random.choice([image1, image2, image3, image4])

score = 0
start_time = None
game_over = False
state = "start_menu"
option = -1


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if state == "start_menu":
                if start_button.collidepoint(event.pos):
                    state = "playing"
                    score = 0
                    start_time = pygame.time.get_ticks()
                    option = random.randint(1, 4)
            if state == "playing":
                if correct_image_rect.collidepoint(event.pos):
                    score += 1
                    if score == 10:
                        with open("ranking.txt", "a") as f:
                            f.write(str(pygame.time.get_ticks() / 1000 - start_time / 1000) + "\n")
                        game_over = True

                option = random.randint(1, 4)
                correct_images = [image for image in correct_images if image != correct_image]
                incorrect_images = [image for image in incorrect_images if image != correct_image]
                correct_image = random.choice(correct_images)
                correct_image = pygame.transform.scale(correct_image, (WIDTH/2, HEIGHT/2))
                correct_images.append(correct_image)

                image1 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
                image2 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
                image3 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))
                image4 = pygame.transform.scale(random.choice(incorrect_images), (WIDTH/2, HEIGHT/2))

                if option == 1:
                    image1 = random.choice(correct_images)
                    image1 = pygame.transform.scale(image1, (WIDTH/2, HEIGHT/2))
                if option == 2:
                    image2 = random.choice(correct_images)
                    image2 = pygame.transform.scale(image2, (WIDTH/2, HEIGHT/2))
                if option == 3:
                    image3 = random.choice(correct_images)
                    image3 = pygame.transform.scale(image3, (WIDTH/2, HEIGHT/2))
                if option == 4:
                    image4 = random.choice(correct_images)
                    image4 = pygame.transform.scale(image4, (WIDTH/2, HEIGHT/2))


    screen.fill(WHITE)

    image1_rect = image1.get_rect()
    image1_rect.x = 0
    image1_rect.y = 0
    screen.blit(image1, image1_rect)

    image2_rect = image2.get_rect()
    image2_rect.x = WIDTH/2
    image2_rect.y = 0
    screen.blit(image2, image2_rect)

    image3_rect = image3.get_rect()
    image3_rect.x = 0
    image3_rect.y = HEIGHT/2
    screen.blit(image3, image3_rect)

    image4_rect = image4.get_rect()
    image4_rect.x = WIDTH/2
    image4_rect.y = HEIGHT/2
    screen.blit(image4, image4_rect)


    correct_image_rect = correct_image.get_rect()
    if option == 1:
        correct_image_rect.x = 0
        correct_image_rect.y = 0
    if option == 2:
        correct_image_rect.x = WIDTH/2
        correct_image_rect.y = 0
    if option == 3:
        correct_image_rect.x = 0
        correct_image_rect.y = HEIGHT/2
    if option == 4:
        correct_image_rect.x = WIDTH/2
        correct_image_rect.y = HEIGHT/2
    pygame.draw.rect(screen, BLACK, correct_image_rect, 2)




    if state == "start_menu":
        start_button = pygame.draw.rect(screen, WHITE, (WIDTH//2 - 50, HEIGHT//2 - 25, 100, 50))
        start_text = font.render("Start", True, BLACK)
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2 - start_text.get_height()//2))
    elif state == "playing":
        score_text = font.render("Score: {}".format(score), True, BLACK)
        screen.blit(score_text, (10, 10))

        time_text = font.render("Time: {:.2f}".format(pygame.time.get_ticks() / 1000 - start_time / 1000), True, BLACK)
        screen.blit(time_text, (10, 50))

    pygame.display.update()

    clock.tick(60)

pygame.quit()



with open("ranking.txt", "r") as f:
    ranking = f.readlines()
    ranking = [float(time.strip()) for time in ranking]
    ranking.sort()
    print("Ranking:")
    for i, time in enumerate(ranking):
        print(str(i + 1) + ". " + str(round(time, 2)) + " seconds")
