import pygame
import requests
import sys
import os
print('Введите координаты и масштаб!')
response = None
try:
    x, y, z, c = float(input()), float(input()), float(input()), float(input())
    map_request = 'http://static-maps.yandex.ru/1.x/?ll='+str(x)+','+str(y)+'&spn='+str(z)+','+str(c)+'&l=sat'
    print(map_request)
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
except:
    print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
    sys.exit(1)
map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)
pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)