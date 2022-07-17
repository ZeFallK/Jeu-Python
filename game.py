# from distutils.spawn import spawn
# import pygame
# import pytmx
# import pyscroll

# from player import Player

# class Game:
#     def __init__(self):
#         # Démarrage
#         self.running = True
#         self.map = "world"
#         #creer la fenetre du jeu
#         self.screen = pygame.display.set_mode((800,600))
#         pygame.display.set_caption("PythGame- Adventure")#titre de la fenetre
#         #charger la carte
#         tmx_data= pytmx.util_pygame.load_pygame('carte.tmx')
#         map_data= pyscroll.data.TiledMapData(tmx_data)
#         map_layer= pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
#         map_layer.zoom = 2
#         #genere un joueur
#         player_position = tmx_data.get_object_by_name("Player")
#         self.player = Player(player_position.x ,player_position.y)
#         #definir une liste qui va stocker les collisions
#         self.walls = []

#         for obj in tmx_data.objects:
#             if obj.name == "collision":
#                 self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


#         #dessinner le grp de calque
#         self.group= pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
#         self.group.add(self.player)                                             #ajt un joueur
    
#         #definir le rect de collisionpour entrer dans la maison
#         enter_house =tmx_data.get_object_by_name('enter_house')
#         self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)




#     def handle_input(self):
#         pressed = pygame.key.get_pressed()

#         if pressed[pygame.K_UP]:
#             self.player.move_up()
#             self.player.change_animation('up')
#         elif pressed[pygame.K_DOWN]:
#             self.player.move_down()
#             self.player.change_animation('down')
#         elif pressed[pygame.K_LEFT]:
#             self.player.move_left()
#             self.player.change_animation('left')
#         elif pressed[pygame.K_RIGHT]:
#             self.player.move_right()
#             self.player.change_animation('right')

#     def switch_house(self):
#         self.map = 'house'
#         #charger la carte
#         tmx_data= pytmx.util_pygame.load_pygame('maison.tmx')
#         map_data= pyscroll.data.TiledMapData(tmx_data)
#         map_layer= pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
#         map_layer.zoom = 2

#         #definir une liste qui va stocker les collisions
#         self.walls = []

#         for obj in tmx_data.objects:
#             if obj.name == "collision":
#                 self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


#         #dessinner le grp de calque
#         self.group= pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
#         self.group.add(self.player)                                             #ajt un joueur
    
#         #definir le rect de collisionpour entrer dans la maison
#         enter_house =tmx_data.get_object_by_name('exit_house')
#         self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

#         #recup le spawn
#         spawn_house_point = tmx_data.get_object_by_name('spawn_house')
#         self.player.position[0] = spawn_house_point.x
#         self.player.position[1] = spawn_house_point.y - 20

#     def switch_world(self):
#         self.map = 'world'
#         #charger la carte
#         tmx_data= pytmx.util_pygame.load_pygame('carte.tmx')
#         map_data= pyscroll.data.TiledMapData(tmx_data)
#         map_layer= pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
#         map_layer.zoom = 2

#         #definir une liste qui va stocker les collisions
#         self.walls = []

#         for obj in tmx_data.objects:
#             if obj.name == "collision":
#                 self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


#         #dessinner le grp de calque
#         self.group= pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
#         self.group.add(self.player)                                             #ajt un joueur
    
#         #definir le rect de collisionpour entrer dans la maison
#         enter_house =tmx_data.get_object_by_name('enter_house_exit')
#         self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

#         #recup le spawn
#         spawn_house_point = tmx_data.get_object_by_name('spawn_house')
#         self.player.position[0] = spawn_house_point.x
#         self.player.position[1] = spawn_house_point.y + 20

#     def update(self):
        
#         self.group.update()
#         #verif entrée maison
#         if self.map =='world' and self.player.feet.colliderect(self.enter_house_rect):
#             self.switch_house()
           
#         if self.map =='house' and self.player.feet.colliderect(self.enter_house_rect):
#             self.switch_world()
            
#         #verif collision
#         for sprite in self.group.sprites():
#             if sprite.feet.collidelist(self.walls) > -1:
#                 sprite.move_back()


#     def run(self):
#         #fps du jeu
#         clock = pygame.time.Clock()
#         #boucle du jeu
#         running = True

#         while running:

#             self.player.save_location()
#             self.handle_input()
#             self.update()
#             self.group.center(self.player.rect.center)
#             self.group.draw(self.screen)
#             pygame.display.flip()
#             for event in pygame.event.get():
#                 if event.type ==pygame.QUIT:
#                     running = False
            
#             clock.tick(60)
#         pygame.quit()
import pygame
import pytmx
import pyscroll

from player import Player


class Game:

    def __init__(self):
        # Démarrage
        self.running = True
        self.map = "world"

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("BasiqueGame")

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Générer le joeur
        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y)



        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    # def handle_input(self):
    #     pressed = pygame.key.get_pressed()


    #     if pressed[pygame.K_UP]:
    #         self.player.move_player("up")
    #     elif pressed[pygame.K_DOWN]:
    #         self.player.move_player("down")
    #     elif pressed[pygame.K_RIGHT]:
    #         self.player.move_player("right")
    #     elif pressed[pygame.K_LEFT]:
    #         self.player.move_player("left")
    
    def handle_input(self):
         pressed = pygame.key.get_pressed()

         if pressed[pygame.K_UP]:
             self.player.move_up()
             self.player.change_animation('up')
         elif pressed[pygame.K_DOWN]:
             self.player.move_down()
             self.player.change_animation('down')
         elif pressed[pygame.K_LEFT]:
             self.player.move_left()
             self.player.change_animation('left')
         elif pressed[pygame.K_RIGHT]:
             self.player.move_right()
             self.player.change_animation('right')           

    def switch_house(self):
        self.map = "house"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("maison.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("exit_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        self.map = "world"

        # Charger la carte clasique
        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Les collisions
        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # Dessiner les différents calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # Porte de la maison
        enter_house = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # Intérieur
        spawn_house_point = tmx_data.get_object_by_name("enter_house_exit")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20

    def update(self):
        self.group.update()

        # Vérifier l'entrer de la maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()

        if self.map == "house" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
           
        # Vérification des collisions
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()

        # Clock
        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            clock.tick(60)

        pygame.quit()