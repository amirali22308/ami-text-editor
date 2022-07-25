from os.path import exists
directions = {"up" : 1,"right" : 2,"left" : 3,"down" : 4}
class text_holder:
    #note: current_char[0] means what line are we on
    #note: current_char[1] means what character are we on (in the current line)
    def __init__(self,file_path):
        self.current_char = [0,-1]
        self.scroll_amount = 0
        if (not exists(file_path)):
            self.file_path = "does_not_exists"
            self.lines = [""]
            return None
        else:
            self.file_path = file_path
            file_stream = open(file_path,'r')
            self.lines = file_stream.readlines()
            if (len(self.lines) == 0):
                self.lines = [""]
                file_stream.close()
                return None
            if (self.lines[len(self.lines)-1] != "" and self.lines[len(self.lines)-1] != "\n"):
                self.lines[len(self.lines)-1] += '\n'
            file_stream.close()
        for turn in range(0,len(self.lines)):
            if (self.lines[turn][len(self.lines[turn])-1] == '\n'):
                self.lines[turn]  = self.lines[turn][0:len(self.lines[turn])-1]
    def move(self,direction : int):
        if (direction == directions["up"]):
            if (self.current_char[0] > 0):
                self.current_char[0] -= 1
        if (direction == directions["down"]):
            if (self.current_char[0] < len(self.lines)-1):
                self.current_char[0] += 1
        if (direction == directions["left"]):
            if (self.current_char[1] > -1):
                self.current_char[1] -= 1
        if (direction == directions["right"]):
            if (self.current_char[1]+1 < len(self.lines[self.current_char[0]])):
                self.current_char[1] += 1
    def new_line(self):
        new_lines = self.lines[0:self.current_char[0]]
        add = self.lines[self.current_char[0]][0:self.current_char[1]+1]
        new_lines += [add]
        add = self.lines[self.current_char[0]][self.current_char[1]+1:len(self.lines[self.current_char[0]])]
        new_lines += [add]
        new_lines += self.lines[self.current_char[0]+1:len(self.lines)]
        self.current_char[0] += 1
        self.current_char[1] = -1
        self.lines = new_lines
    def write(self,input_char : str):
        new_line = self.lines[self.current_char[0]][0:self.current_char[1]+1]
        new_line += input_char
        if (self.current_char[1]+1 < len(self.lines[self.current_char[0]])):
            new_line += self.lines[self.current_char[0]][self.current_char[1]+1:len(self.lines[self.current_char[0]])]
        self.current_char[1] += 1
        self.lines[self.current_char[0]] = new_line
    def delete(self):
        if (self.current_char[1] == -1):
            if (self.current_char[0] > 0):
                holder = self.lines[self.current_char[0]]
                self.lines.pop(self.current_char[0])
                self.current_char[0] -= 1
                self.lines[self.current_char[0]] += holder
        else:
            new_line = self.lines[self.current_char[0]][0:self.current_char[1]]
            new_line += self.lines[self.current_char[0]][self.current_char[1]+1:len(self.lines[self.current_char[0]])]
            self.lines[self.current_char[0]] = new_line
            self.current_char[1] -= 1