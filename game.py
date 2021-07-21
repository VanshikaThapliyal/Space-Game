import pygame
screen_size=[1280,720]
screen=pygame.display.set_mode(screen_size)
background=pygame.image.load("space_background(2).jpg")
bullet=pygame.image.load("bullet (2).png")
bullet_y=600
fired=False
spaceship=pygame.image.load("spaceship (4).png")
planets=["planet (2).png","planet-earth (1).png","venus.png"]
p_index=0
planet=pygame.image.load(planets[p_index])
planet_x=790
move_direction="right"
keep_alive=True
while keep_alive:
  clock=pygame.time.Clock()
  pygame.event.get()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_SPACE]==True:
    fired=True
  if move_direction=="right":
    planet_x=planet_x+5
    if planet_x==1150:
      move_direction="left"
  else:
    planet_x=planet_x-5
    if planet_x==500:
      move_direction="right"
  if fired is True:
    bullet_y=bullet_y-5
    if bullet_y==100:
      fired=False
      bullet_y=600
  if bullet_y<278 and planet_x>780 and planet_x<908:
    p_index=p_index+1
    if p_index<len(planets):
      planet=pygame.image.load(planets[p_index])
      planet_x=600
    else:
      print("you won")
      keep_alive=False
  screen.blit(background,[0,0])
  screen.blit(bullet,[850,bullet_y])
  screen.blit(spaceship,[780,550])
  screen.blit(planet,[planet_x,150])

  pygame.display.update()
  clock.tick(60)
