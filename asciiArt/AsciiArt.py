import pyfiglet

def ascii_art(s,a):
    output = pyfiglet.figlet_format(s, a)
    print(output)
def supported_fonts():
    Fonts = pyfiglet.FigletFont.getFonts()
    for i in Fonts:
        print(i)
supported_fonts()
ascii_art("HELLO","slant")











