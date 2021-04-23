import pygame
import os

class Animation:
    
    def __init__(self, img_name, kolom, baris):
        # ambil alamat directory (absolute)
        basepath = os.path.dirname(__file__)

        # ambil spritesheet dari folder assets
        self.sheet = pygame.image.load(os.path.join(basepath, os.pardir, "assets", img_name)).convert_alpha()
        
        # index frame yang sedang di draw
        self.__current_frame = 0

        self.__target_frame = self.__current_frame

        # list frame yang dapat dari spritesheet
        self.frames = []
        spreadsheet_size = self.sheet.get_size()
        # parsing frames dari spritesheet
        self.frame_size = (spreadsheet_size[0] // kolom , spreadsheet_size[1] // baris)
        for j in range(baris):
            for i in range(kolom):
                pos = (self.frame_size[0] * i, self.frame_size[1] * j)
                frame = self.sheet.subsurface(pygame.Rect(pos, self.frame_size))
                frame = pygame.transform.scale(frame, (32, 48))
                self.frames.append(frame)
    

    
    # ganti frame yang di draw menjadi frame selanjutnya
    def next(self):
        self.__current_frame = ((self.__current_frame + 1) % (len(self.frames) - 1))
    
    # set current drawn frame
    def set_current_frame(self, idx):
        self.__current_frame = idx

    def set_target_frame(self, idx):
        self.__target_frame = idx
    # draw frame di pojok kiri atas
    def draw(self, window):
        window.layar.blit(self.frames[self.__current_frame], (0,0))

    # draw frame di pos
    def draw(self, window, pos):
        if self.__current_frame > self.__target_frame:
            self.__current_frame -= 1
        elif self.__current_frame < self.__target_frame:
            self.__current_frame += 1
            
        window.layar.blit(self.frames[self.__current_frame], pos)    
    
    