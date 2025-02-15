# import pygame
# import random

# # Pygame-ni ishga tushiramiz
# pygame.init()

# # EKRAN O‘LCHAMLARI
# WIDTH, HEIGHT = 800, 400
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Dino Runner")

# # RANGLAR
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 200, 0)
# RED = (255, 0, 0)

# # SHAKLLAR VA SHAKSIZLAR
# clock = pygame.time.Clock()
# FONT = pygame.font.Font(None, 36)

# # DINOZAVR
# dino_size = 50
# dino_x = 100
# dino_y = HEIGHT - dino_size - 10
# dino_vel = 0
# gravity = 0.6
# jump_power = -12
# on_ground = True

# # TO‘SIQLAR
# obstacles = []
# obstacle_width = 20
# obstacle_height = 40
# obstacle_vel = 5
# spawn_rate = 1500  # Har 1.5 sekundda yangi to‘siq chiqadi
# last_spawn_time = pygame.time.get_ticks()

# # O‘YIN HOLATI
# running = True
# score = 0
# high_score = 0

# # O‘YIN TSIKLI
# while running:
#     SCREEN.fill(WHITE)

#     # Hodisalarni tekshiramiz
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and on_ground:
#                 dino_vel = jump_power
#                 on_ground = False

#     # Dinozavr FIZIKASI
#     dino_y += dino_vel
#     dino_vel += gravity

#     if dino_y >= HEIGHT - dino_size - 10:
#         dino_y = HEIGHT - dino_size - 10
#         on_ground = True

#     # TO‘SIQLARNI YARATISH
#     current_time = pygame.time.get_ticks()
#     if current_time - last_spawn_time > spawn_rate:
#         obstacle_x = WIDTH
#         obstacle_y = HEIGHT - obstacle_height - 10
#         obstacles.append([obstacle_x, obstacle_y])
#         last_spawn_time = current_time

#     # TO‘SIQLARNI HARAKATGA KELTIRISH
#     for obstacle in obstacles:
#         obstacle[0] -= obstacle_vel

#     # TO‘SIQLARNI TOZALASH
#     obstacles = [obs for obs in obstacles if obs[0] > -obstacle_width]

#     # URILISHNI TEKSHIRISH
#     for obstacle in obstacles:
#         if (dino_x + dino_size > obstacle[0] and dino_x < obstacle[0] + obstacle_width and
#                 dino_y + dino_size > obstacle[1]):
#             running = False  # Agar to‘siqqa urilsa, o‘yin tugaydi

#     # BALL HISOBINI OSHIRISH
#     score += 1
#     if score > high_score:
#         high_score = score

#     # DINOZAVRNI CHIZISH
#     pygame.draw.rect(SCREEN, GREEN, (dino_x, dino_y, dino_size, dino_size))

#     # TO‘SIQLARNI CHIZISH
#     for obstacle in obstacles:
#         pygame.draw.rect(SCREEN, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

#     # BALLNI EKRANGA CHIQARISH
#     score_text = FONT.render(f"Score: {score}", True, BLACK)
#     high_score_text = FONT.render(f"High Score: {high_score}", True, BLACK)
#     SCREEN.blit(score_text, (10, 10))
#     SCREEN.blit(high_score_text, (10, 40))

#     pygame.display.flip()
#     clock.tick(30)

# pygame.quit()
