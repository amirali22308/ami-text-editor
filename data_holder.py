import pygame
import os
path = ""
font_size = 0
command_get_font = 0
font = None
target_screen_size = (900,700)
currsor_line_lenght = 0
text_color = (0,0,0)
back_ground_color = (0,0,0)
command_get_back_ground_color = (0,0,0)
command_get_text_color = (0,0,0)
commnad_get_font_size = 20
def init():
    global path
    global font
    global font_size
    global currsor_line_lenght
    global text_color
    global back_ground_color
    global command_get_back_ground_color
    global command_get_text_color
    global command_get_font
    global commnad_get_font_size
    command_get_text_color = (70,70,100)
    command_get_back_ground_color = (10,20,30)
    back_ground_color = (10,10,20)
    full_path = os.path.realpath(__file__)
    path = os.path.dirname(full_path) + chr(92)
    font_size = 35
    command_get_font = pygame.font.Font(path + "font.ttf",commnad_get_font_size)
    font = pygame.font.Font(path + "font.ttf",font_size)
    currsor_line_lenght = 5
    text_color = (90,90,100)
def change_font_size(size : int):
    global font
    global font_size
    font_size = size
    font = pygame.font.Font(path + "font.ttf",size)
def change_commnad_get_font_size(size : int):
    global command_get_font
    global commnad_get_font_size
    commnad_get_font_size = size
    command_get_font = pygame.font.Font(path + "font.ttf",size)
def change_screen_size(change_amount_x : int,change_amount_y : int):
    global target_screen_size
    target_screen_size = (change_amount_x,change_amount_y)