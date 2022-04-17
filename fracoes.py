import pygame as pg
from pygame.locals import *
from fractions import gcd
import time

class Setup:
    def __init__(self) -> None:
        pg.init()
        self.index = 0
        self.values = [2,4,2,4]
        self.dimensions()
        self.colors()
        self.pos()

    def dimensions(self, width = 1400, height = 700):
        self.width = width
        self.height = height
        self.size = 80
        return (self.width, self.height)

    def pos(self, x1=100, x2=550, x3=1000, y=200):
        self.x_diagram_1 = x1
        self.x_diagram_2 = x2
        self.x_diagram_3 = x3
        self.y_diagrams = y
        self.diagram_size = 580

    def colors(self):
        self.blue = (0,0,220)
        self.red = (220,0,0)
        self.black = (0,0,0)
        self.green = (0,220,0)
        self.grey = (200,200,200)
        self.white = (250,250,250)

class Window:
    def __init__(self, text_, width_=1400, height_=800, fps_=2):
        self.screen(width_, height_)
        self.fps(fps_)
        self.title(text_)

    def screen(self, width, height):
        self._display = pg.display.set_mode( (width, height) )

    def fps(self, fps):
        _fps = pg.time.Clock().tick(fps)

    def title(self, text):
        _display = pg.display.set_caption(text)

class Render(Setup, Window):
    def __init__(self):
        Setup.__init__(self)
        Window.__init__(self, 'Frações')
        pg.font.init()

    def render_text(self, x, y, text, type, size):
        font_ = pg.font.SysFont(type, size)
        self._display.blit(font_.render(text, True, self.black), (x, y))
    
    def render_fraction(self, numerator, denominator, x_diagram):
        text = ''        
        if len(str(numerator)) >= len(str(denominator)):
            for n in range(len(str(numerator))):
                text = text + '_'
            self.render_text(x_diagram + 100, self.y_diagrams - 150, '{}'.format(numerator), 'arial', 30)
            self.render_text(x_diagram + 100 + 7*abs(len(str(numerator))-len(str(denominator))), self.y_diagrams - 123, '{}'.format(denominator), 'arial', 30)
        else:
            for n in range(len(str(denominator))):
                text = text + '_'
            self.render_text(x_diagram + 100 + 7*abs(len(str(numerator))-len(str(denominator))), self.y_diagrams - 150, '{}'.format(numerator), 'arial', 30)
            self.render_text(x_diagram + 100, self.y_diagrams - 123, '{}'.format(denominator), 'arial', 30)
        self.render_text(x_diagram + 100, self.y_diagrams - 150, text, 'arial', 30)

    def simplification(self, numerator, denominator, x_diagram):
        numerator = abs(numerator)
        denominator = abs(denominator)
        x = gcd(numerator, denominator)
        if x != 1:
            numerator = int(numerator / x)
            denominator = int(denominator / x)
            self.render_text(x_diagram + 160, self.y_diagrams-150, '÷{}'.format(x), 'arial', 30)
            self.render_text(x_diagram + 160, self.y_diagrams-123, '÷{}'.format(x), 'arial', 30)
            self.render_text(x_diagram + 210, self.y_diagrams-135, '='.format(x), 'arial', 30)
            self.render_fraction(numerator, denominator, x_diagram + 130)

    def draw(self, window, xi, yi, xf, yf, color, border=0):
        pg.draw.rect(window, self.black, (xi, yi, xf, yf), border_radius= 0)
        pg.draw.rect(window, color, (xi+2, yi+2, xf-4, yf-4), border_radius= border)

    def slice(self, x_diagram, denominator):
        _denominator = abs(denominator)
        for n in range(_denominator-1):
            pg.draw.line(self._display, self.black, (x_diagram, (n+1)*self.diagram_size/_denominator + self.y_diagrams),(x_diagram + 299,(n+1)*self.diagram_size/_denominator + self.y_diagrams), 2)

    def diagram(self, numerator, denominator, x_diagram, color):
        if numerator*denominator<0:

            color = (100, 0, 100)
        numerator = abs(numerator)
        denominator = abs(denominator)
        interger = int(numerator / denominator)
        remainder = numerator - interger * denominator
        if numerator >= denominator:
            for n in range(interger):
                self.draw(self._display, x_diagram - 50, self.y_diagrams + (self.size + 3) * n, self.size - self.size / 2, self.size, color)
            numerator = numerator - interger
        self.draw(self._display, x_diagram, self.y_diagrams, 300, self.diagram_size, self.white)
        pg.draw.rect(self._display, color, (x_diagram + 2, self.y_diagrams + 2, 296, remainder * self.diagram_size/denominator -2))
        self.slice(x_diagram, denominator)

    def agroup(self, numerator, denominator, x_diagram, color):
        Render.render_fraction(self, numerator, denominator, x_diagram)
        Render.simplification(self, numerator, denominator, x_diagram)
        Render.render_text(self, x_diagram + 130, self.y_diagrams - 50, str(round(numerator/denominator, 7)), 'arial', 30)
        Render.diagram(self, numerator, denominator, x_diagram, color)

    def agroup_simplification(self, numerator, denominator, x_diagram, color):
        Render.render_fraction(self, numerator, denominator, x_diagram)
        Render.simplification(self, numerator, denominator, x_diagram)
        numerator = abs(numerator)
        denominator = abs(denominator)
        x = gcd(numerator, denominator)
        if x != 1:
            numerator = int(numerator / x)
            denominator = int(denominator / x)
        Render.render_text(self, x_diagram + 130, self.y_diagrams - 50, str(round(numerator/denominator, 7)), 'arial', 30)
        Render.diagram(self, numerator, denominator, x_diagram, color)

    def pointer(self):
        if self.index == 0:
            pg.draw.circle(self._display, self.blue, (self.x_diagram_1 + 90, self.y_diagrams - 132), 10)
        if self.index == 1:
            pg.draw.circle(self._display, self.blue, (self.x_diagram_1 + 90, self.y_diagrams - 105), 10)
        if self.index == 2:
            pg.draw.circle(self._display, self.red, (self.x_diagram_2 + 90, self.y_diagrams - 132), 10)
        if self.index == 3:
            pg.draw.circle(self._display, self.red, (self.x_diagram_2 + 90, self.y_diagrams - 105), 10)

class Fraction(Render):
    def __init__(self):
        Render.__init__(self)

    def _lcm(self, n, m):
        return int(n*m/gcd(n, m))

    def sum(self, numerator_1, denominator_1, numerator_2, denominator_2):
        denominator_3 = self._lcm(denominator_2, denominator_1)

        new_numerator_1 = (denominator_3/denominator_1)*numerator_1
        new_numerator_2 = (denominator_3/denominator_2)*numerator_2
        numerator_3 =  int(new_numerator_1 + new_numerator_2)

        self.agroup(numerator_1, denominator_1, self.x_diagram_1, self.blue)
        self.agroup(numerator_2, denominator_2, self.x_diagram_2, self.red)
        self.agroup(numerator_3, denominator_3, self.x_diagram_3, self.green)

    def subtration(self, numerator_1, denominator_1, numerator_2, denominator_2):
        denominator_3 = self._lcm(denominator_2, denominator_1)

        new_numerator_1 = (denominator_3/denominator_1)*numerator_1
        new_numerator_2 = (denominator_3/denominator_2)*numerator_2
        numerator_3 =  int(new_numerator_1 - new_numerator_2)

        self.agroup(numerator_1, denominator_1, self.x_diagram_1, self.blue)
        self.agroup(numerator_2, denominator_2, self.x_diagram_2, self.red)
        self.agroup(numerator_3, denominator_3, self.x_diagram_3, self.green)

    def multiplication(self, numerator_1, denominator_1, numerator_2, denominator_2):
        denominator_3 = denominator_1 * denominator_2
        numerator_3 =  numerator_1 * numerator_2

        self.agroup(numerator_1, denominator_1, self.x_diagram_1, self.blue)
        self.agroup(numerator_2, denominator_2, self.x_diagram_2, self.red)
        self.agroup(numerator_3, denominator_3, self.x_diagram_3, self.green)

    def division(self, numerator_1, denominator_1, numerator_2, denominator_2):
        denominator_3 = numerator_2 * denominator_1
        numerator_3 =  numerator_1 * denominator_2

        self.agroup(numerator_1, denominator_1, self.x_diagram_1, self.blue)
        self.agroup(numerator_2, denominator_2, self.x_diagram_2, self.red)
        self.agroup_simplification(numerator_3, denominator_3, self.x_diagram_3, self.green)

    def error(self,denominator_1, denominator_2):
        if denominator_1 == 0 or denominator_2 == 0:
            self.render_text(self.width/2 -350, self.height/2, 'não é possível dividir por 0', 'arial', 80)
            return True
        else:
            return False

class Main(Fraction, Render, Setup, Window):
    def __init__(self):
        Fraction.__init__(self)
        self.play()
    
    def coommands(self):
        if pg.key.get_pressed()[K_UP]:
            self.values[self.index] += 1
            time.sleep(0.2)
        if pg.key.get_pressed()[K_DOWN]:
            self.values[self.index] -= 1
            time.sleep(0.2)
        if pg.key.get_pressed()[K_LEFT]:
            self.index -= 1
            if self.index < 0:
                self.index = 3
            time.sleep(0.2)
        if pg.key.get_pressed()[K_RIGHT]:
            self.index += 1
            if self.index > 3:
                self.index = 0
            time.sleep(0.2)

    def play(self):

        while True:
            numerator_1 = self.values[0]
            denominator_1 = self.values[1]
            numerator_2 = self.values[2]
            denominator_2 = self.values[3]

            self._display.fill(self.grey)
            self.pointer()
            self.coommands()
            if self.error(denominator_1, denominator_2):
                self.error
            else:
                Render.agroup(self, numerator_1, denominator_1, self.x_diagram_1, self.blue)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            pg.display.update()

if __name__ == '__main__':
    play = Main()