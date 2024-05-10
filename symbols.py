from colors import RGB, BLACK
from PIL import Image, ImageDraw, ImageFont
from random import choice

import numpy

SYMBOL_SIZE = 12

WIDTH = 10 * SYMBOL_SIZE
HEIGHT = 10 * SYMBOL_SIZE

BACKGROUND_COLOR = BLACK
RESIZE_TO = (WIDTH*4, HEIGHT*4)

# Enter your symbols pattern here SYMBOLS = '123'
SYMBOLS = \
    "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKL" + \
    "MNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxy" + \
    "z{|}~⌂ ¡¢£¤¥¦§¨©ª«¬-®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆ" + \
    "ÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòó" + \
    "ôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠ" + \
    "ġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌō" + \
    "ŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹź" + \
    "ŻżŽžſƒơƷǺǻǼǽǾǿȘșȚțɑɸˆˇˉ˘˙˚˛˜˝;΄΅Ά·ΈΉΊΌΎΏΐΑΒΓΔ" + \
    "ΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξοπρς" + \
    "στυφχψωϊϋόύώϐϴЀЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНО" + \
    "ПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъы" + \
    "ьэюяѐёђѓєѕіїјљњћќѝўџҐґ־אבגדהוזחטיךכלםמןנסעףפץ" + \
    "צקרשתװױײ׳״ᴛᴦᴨẀẁẂẃẄẅẟỲỳ‐‒–—―‗‘’‚‛“”„‟†‡•…‧‰′″‵" + \
    "‹›‼‾‿⁀⁄⁔⁴⁵⁶⁷⁸⁹⁺⁻ⁿ₁₂₃₄₅₆₇₈₉₊₋₣₤₧₪€℅ℓ№™Ω℮⅐⅑⅓⅔⅕⅖" + \
    "⅗⅘⅙⅚⅛⅜⅝⅞←↑→↓↔↕↨∂∅∆∈∏∑−∕∙√∞∟∩∫≈≠≡≤≥⊙⌀⌂⌐⌠⌡─│┌┐└" + \
    "┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬▀▁▄█▌▐░▒▓■" + \
    "□▪▫▬▲►▼◄◊○●◘◙◦☺☻☼♀♂♠♣♥♦♪♫✓ﬁﬂ�╪╫"
# SYMBOLS = '▲►▼◄●'
# SYMBOLS = '☺☻'
# SYMBOLS = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm{};\/:|<>?/~`[]()*&^%$#@!'
# SYMBOLS = '─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬'
# SYMBOLS = '═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬'
# SYMBOLS = '╔╗╚╝'
# SYMBOLS = '┌┐└┘'
# SYMBOLS = '[](){}'
# SYMBOLS = '0123456789'
# SYMBOLS = '01'
# SYMBOLS = 'ĆćĈĉĊċČčcC'

data = numpy.zeros((HEIGHT, WIDTH, 3), dtype=numpy.uint8)
data[:][:] = BACKGROUND_COLOR
image = Image.fromarray(data)

def random_color(): 
    return RGB[choice(tuple(RGB.keys()))]

draw = ImageDraw.Draw(image)
for x in range(WIDTH // SYMBOL_SIZE):
    for y in range(HEIGHT // SYMBOL_SIZE):
        draw.text((x*SYMBOL_SIZE + 2, y*SYMBOL_SIZE + 2), choice(SYMBOLS), font=ImageFont.truetype("fonts/MetaFont.ttf"), fill=random_color())

image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save('image.png')
image.show()
