from os.path import exists
from text_holder import *
from tkinter import filedialog, font
import pygame
import data_holder
import tkinter

def draw_text(display,text : text_holder,draw_cursor : bool):
    for turn in range(0,len(text.lines)):
        display.blit(data_holder.font.render(str(turn + 1) + '-' + text.lines[turn],True,data_holder.text_color)
        ,(0,(data_holder.font_size * turn) + text.scroll_amount))
        if (turn == text.current_char[0] and draw_cursor):
            surface = data_holder.font.render(str(turn + 1) + '-' + text.lines[turn][0:text.current_char[1]+1]
            ,True,data_holder.text_color)
            rected = surface.get_rect()
            pygame.draw.line(display,(200,200,200,)
            ,[rected.right,rected.bottom + turn * data_holder.font_size + text.scroll_amount]
            ,[rected.right,turn*data_holder.font_size + text.scroll_amount],
            5)
def control_text(text : text_holder,e):
    if (e.key == pygame.K_UP):
        text.move(directions["up"])
    elif (e.key == pygame.K_DOWN):
        text.move(directions["down"])
    elif (e.key == pygame.K_LEFT):
        text.move(directions["left"])
    elif (e.key == pygame.K_RIGHT):
        text.move(directions["right"])
    elif (e.key == pygame.K_BACKSPACE):
        text.delete()
    elif (e.key == pygame.K_RETURN):
        text.new_line()
    elif (len(e.unicode) != 0 and e.key != pygame.K_ESCAPE):
        text.write(e.unicode)

def command_get_draw(display,inputed_text : str):
    pos_y = data_holder.target_screen_size[1] 
    pos_y -= int(data_holder.target_screen_size[1] / 5)
    pygame.draw.rect(display,data_holder.command_get_back_ground_color
    ,(0,pos_y,data_holder.target_screen_size[0]
    ,data_holder.target_screen_size[1]-pos_y))
    
    display.blit(data_holder.command_get_font.render("command:"+inputed_text,True,data_holder.command_get_text_color)
    ,(data_holder.target_screen_size[0]//50,pos_y))
def command_control(e,text : text_holder,current_text : str):
    if (e.key == pygame.K_BACKSPACE):
        current_text = current_text[:len(current_text)-1]
    elif (e.key == pygame.K_RETURN):
        current_text = current_text.split(" ")
        if (current_text[0] == "new_file"):
            text.file_path = "does_not_exists"
            text.lines = []
        elif (current_text[0] == "delete_all"):
            text.lines = []
        elif (current_text[0] == "cpp_template"):
            text.lines = [
                "#include<iostream>",
                "int main()",
                "{",
                "std::cout << " + '"' + "hello word" + '"' + " ;",
                "}"
            ]
        elif(current_text[0] == "c#_template"):
            text.lines = [
                "using System;",
                "class Program{",
                "   public static void main(string[] args){",
                "       System.Write(" + '"' + "hello word" + '"' + ");",
                "   }",
                "}"
            ]
        elif(current_text[0] == "python_template"):
            text.lines = [
                "print(" + '"' + "hello word" + '"' + ")"
            ]
        elif(current_text[0] == "js_template"):
            text.lines = [
                "idk javascript very well :("
            ]
        elif(current_text[0] == "assembly_template"):
            text.lines = [
                "are you a legend and very smart?",
                "or are you super dumm?"
            ]
        elif(current_text[0] == "html_template"):
            text.lines = [
                "html is not a programing langauge"
            ]
        elif(current_text[0] == "css_template"):
            text.lines = [
                "css is not a programing langauge"
            ]
        elif(current_text[0] == "brainFuck_template"):
            text.lines = [
                "f**k my brain hurts"
            ]
        elif(current_text[0] == "how_are_u"):
            text.lines = [
                "wow thanks for asking :)"
            ]
        elif(current_text[0] == "fuck_you"):
            text.lines = [
                "fuck you too"
            ]
        elif(current_text[0] == "im_sad"):
            text.lines = [
                "even tho im just a kid",
                "making a silly text editor",
                "i hope u are doing ok",
            ]
        elif (current_text[0] == "save"):
            f = None
            if (text.file_path != "does_not_exists"):
                f = open(text.file_path,'w')
            else:
                if (len(current_text) == 1):
                    return "please_insert_a_file directory"
                elif (not exists(current_text[1])):
                    return "file_directory_not_found"
                f = open(current_text[1])
            for turn in range(0,len(text.lines)):
                if (turn == len(text.lines)-1):
                    f.write(text.lines[turn])
                    continue
                f.write(text.lines[turn] + "\n")
            f.close()
        elif (current_text[0] == "save_as"):
            if (len(current_text) == 1):
                return "please_insert_a_file_directory"
            elif (not exists(current_text[1])):
                return "file_directory_not_found"
            f = open(current_text[1])
            for turn in range(0,len(text.lines)):
                if (turn == len(text.lines)-1):
                    f.write(text.lines[turn])
                    continue
                f.write(text.lines[turn] + "\n")
            f.close()
        elif (current_text[0] == "save_with_file_explorer"):
            if (len(current_text) == 1):
                return "please_insert_a_file_name"
            f = open(filedialog.askdirectory() + "/" + current_text[1],'w')
            for turn in range(0,len(text.lines)):
                if (turn == len(text.lines)-1):
                    f.write(text.lines[turn])
                    continue
                f.write(text.lines[turn] + "\n")
            f.close()
        elif (current_text[0] == "open"):
            if (len(current_text) == 1):
                return "please_insert_a_file_directory"
            if (not exists(current_text[1])):
                return "file_directoy_not_found"
            text.file_path = current_text[1]
            f = open(current_text[1],'r')
            text.lines = f.readlines()
            f.close()
        elif (current_text[0] == "open_with_file_explorer"):
            path = filedialog.askopenfilename()
            text.file_path = path
            f = open(path,'r')
            text.lines = f.readlines()
            f.close()
        elif(current_text[0] == "when_the_imposter_is_sus"):
            return "i_found_amongus"
        elif(current_text[0] == "change_screen_size"):
            if (len(current_text) < 3):
                return "please_insert_change_amount"
            data_holder.change_screen_size(int(current_text[1]),int(current_text[2]))
        elif(current_text[0] == "change_command_get_font_size"):
            if (len(current_text) == 1):
                return "pleass_insert_font_size"
            data_holder.change_commnad_get_font_size(int(current_text[1]))
        elif(current_text[0] == "change_font_size"):
            if (len(current_text) == 1):
                return "please_insert_new_size"
            data_holder.change_font_size(int(current_text[1]))
        elif(current_text[0] == "set_scroll_amount"):
            if (len(current_text) == 1):
                return "please_insert_scroll_amount"
            text.scroll_amount = int(current_text[1])
        else:
            return "wrong_command"
        current_text = ""
    elif (len(e.unicode) != 0):
        current_text += e.unicode
    return current_text

def start_menu(display):
    display.fill(data_holder.command_get_back_ground_color)

    draw = data_holder.command_get_font.render("welcom to ami's text editor",True,data_holder.command_get_text_color)
    rect = draw.get_rect()
    pos_x = data_holder.target_screen_size[0]/2
    pos_y = data_holder.target_screen_size[1]/2
    pos_x -= rect.right/2
    pos_y -= rect.bottom/2
    display.blit(draw,(pos_x,pos_y - data_holder.font_size*2))
    draw = data_holder.command_get_font.render("press n to create new file",True,data_holder.command_get_text_color)
    rect = draw.get_rect()
    pos_x = data_holder.target_screen_size[0]/2
    pos_y = data_holder.target_screen_size[1]/2
    pos_x -= rect.right/2
    pos_y -= rect.bottom/2
    display.blit(draw,(pos_x,pos_y))
    draw = data_holder.command_get_font.render("press o to open a file",True,data_holder.command_get_text_color)
    rect = draw.get_rect()
    pos_x = data_holder.target_screen_size[0]/2
    pos_y = data_holder.target_screen_size[1]/2
    pos_x -= rect.right/2
    pos_y -= rect.bottom/2
    display.blit(draw,(pos_x,pos_y + data_holder.font_size*2))
    pygame.display.update()
    while True:
        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN):
                if (e.key == pygame.K_n):
                    return text_holder("")
                if (e.key == pygame.K_o):
                    return text_holder(filedialog.askopenfilename())
            if (e.type == pygame.QUIT):
                return None

def main():
    pygame.init()
    data_holder.init()
    tkinter.Tk().withdraw()
    display = pygame.display.set_mode(data_holder.target_screen_size)
    pygame.display.set_caption("ami's text editor")
    pygame.display.set_icon(pygame.image.load(data_holder.path + "logo.png"))
    text = start_menu(display)
    if (text == None):
        return None
    getting_commands = False
    stop = False
    current_command = ""
    last_screen_size = data_holder.target_screen_size
    while not stop:
        if (last_screen_size[0] != data_holder.target_screen_size[0]
        or last_screen_size[1] != data_holder.target_screen_size[1]):
            display = pygame.display.set_mode(data_holder.target_screen_size)
            last_screen_size = data_holder.target_screen_size
        display.fill(data_holder.back_ground_color)
        for e in pygame.event.get():
            if (e.type == pygame.QUIT):
                stop = True
            if (e.type == pygame.KEYDOWN):
                if (not getting_commands):
                    control_text(text,e)
                else:
                    current_command = command_control(e,text,current_command)
                if (e.key == pygame.K_ESCAPE):
                    getting_commands = not getting_commands
        draw_text(display,text,not getting_commands)
        command_get_draw(display,current_command)
        pygame.display.update()
if __name__ == "__main__":
    main()

#make scrolling threw text(bouth horizontal and vertical)