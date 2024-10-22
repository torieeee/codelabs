import cairo
import math

#surface - white
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 900, 800)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()

#outline of house
ctx.move_to(100,400)
ctx.line_to(100, 470)
ctx.line_to(140, 470)
ctx.line_to(140, 780)
ctx.line_to(620, 780)
ctx.line_to(620, 470)
ctx.line_to(660, 470)
ctx.line_to(660, 400)
ctx.close_path()
ctx.set_line_width(3)
ctx.set_source_rgb(0,0,0.5)
ctx.stroke()

#windows and door
ctx.move_to(180, 550)
ctx.line_to(180, 650)
ctx.line_to(280, 650)
ctx.line_to(280, 550)
ctx.close_path()
ctx.move_to(180, 600)
ctx.line_to(280, 600)
ctx.move_to(230, 550)
ctx.line_to(230, 650)

ctx.move_to(580, 550)
ctx.line_to(580, 650)
ctx.line_to(480, 650)
ctx.line_to(480, 550)
ctx.close_path()
ctx.move_to(580, 600)
ctx.line_to(480, 600)
ctx.move_to(530, 550)
ctx.line_to(530, 650)

ctx.move_to(320, 780)
ctx.line_to(320, 550)
ctx.line_to(450, 550)
ctx.line_to(450, 780)

ctx.set_line_width(3)
ctx.set_source_rgb(0,0.3,0)
ctx.stroke()

#door knob
ctx.arc(435, 670, 5, 0, 2*math.pi)
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(7)
ctx.stroke()

#dome of house
ctx.arc(380, 400, 175, math.pi, 0)
ctx.set_source_rgb(0, 0, 0.5)
ctx.set_line_width(3)
ctx.stroke()

#moon
#ctx.arc(585, 200, 40, (math.pi/4), ((5*math.pi)/4))
#ctx.curve_to(590, 180, 590, 160, 570, 200)
#ctx.set_source_rgb(1, 0.8, 0.2)
#ctx.fill()
#ctx.fill_preserve()

# Draw the crescent moon
ctx.set_line_width(1)
ctx.arc_negative(650, 150, 40, 5*math.pi/4, math.pi/4)
ctx.curve_to(650,175,620,170,622,120)
ctx.set_source_rgb(0.8,0.8,0)
ctx.fill_preserve()
ctx.set_source_rgb(0,0,1)
ctx.stroke()

#ctx.arc(605, 180, 50, 0.45*math.pi, ((4.1*math.pi)/4))
#ctx.set_source_rgb(1, 1, 1)
#ctx.fill_preserve()

surface.write_to_png('2Dhouse.png')