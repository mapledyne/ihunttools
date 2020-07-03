
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from datetime import datetime
import random
import textwrap



BACKGROUND = (248, 248, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (150, 150, 150)
TRANSPARENT = (0, 0, 0, 0)


def get_template(name):
    try:
        im = Image.open('templates/' + name + ".png")
    except:
        im = Image.open(name).convert("RGBA")
    return im


def paste_image(image, name, x=0, y=0, w=0, h=0):
    im = get_template(name)
    if w + h > 0:
        if w == 0:
            w = im.width
        if h == 0:
            h = im.height
        im = im.resize((w, h))
    image.paste(im, (x, y), im)

def get_time(tm=None):
    if tm is not None:
        return tm
    now = datetime.now()
    return now.strftime("%-I:%M %p")

def star_set(qty, max_qty=5):
    rank = ""

    STAR = "★"
    HALF_STAR = "⯪"
    EMPTY_STAR = "☆"

    count = qty
    while count > 0:
        if count >= 1:
            rank += STAR
        else:
            rank += HALF_STAR
        count = count - 1
    while len(rank) < max_qty:
        rank += EMPTY_STAR
    return rank

class iHuntApp():
    def __init__(self, name, desc, img):
        self.name = name
        self.description = desc
        self.width = 768
        self.height = 1171
        self.image = img

        # random or arbitrary defaults
        self.price = random.randint(1, 18) * 500
        self.stars = random.randint(3, 8) * 0.5
        self.distance = random.uniform(5, 25)
        self.time = random.randint(1, 3)
        self.remaining = random.randint(3, 8)

        # generally reasonable defaults that can still be changed
        self.phonetime = get_time()
        self.cellservicename = "SanJayNet"
        self.currency = "$"
        self.distanceunit = "miles"
        self.timeunit = "days"
        self.remainingunit = "days"

    def screenshot(self, filename):
        phone = Image.new("RGBA", (self.width, self.height), TRANSPARENT)
        canvas = ImageDraw.Draw(phone)

        # Phone background color:
        canvas.rectangle((135, 80, self.width - 135, self.height - 80), BACKGROUND)

        ############ PHONE STUFF
        # cell signal:
        paste_image(phone, "signal", 155, 85)

        # Cell provider:
        arial20 = ImageFont.truetype("Arial.ttf", 20)
        canvas.text((190, 90), self.cellservicename, font=arial20, fill=BLACK)

        # Wifi:
        paste_image(phone, "wifi", 290, 85)

        # Time:
        canvas.text((350, 90), self.phonetime, font=arial20, fill=BLACK)

        ########### APP STUFF
        # Settings Gear:
        paste_image(phone, "gear", 150, 130)

        # Card dots:
        paste_image(phone, "dots", 320, 120)

        # Chat:
        paste_image(phone, "chat", 550, 120)

        # Buttons: Check
        paste_image(phone, "check", 340, 940)

        # Buttons: Cancel
        paste_image(phone, "cancel", 250, 920)

        # Buttons: Undo
        paste_image(phone, "undo", 160, 900)

        # Buttons: Heart
        paste_image(phone, "heart", 450, 920)

        # Buttons: Cash
        paste_image(phone, "cash", 540, 900)

        # job image

        BOX_WIDTH = 415
        paste_image(phone, self.image, 175, 200, BOX_WIDTH, BOX_WIDTH)

        # Card: Outline
        canvas.rectangle(((175, 200), (175 + BOX_WIDTH, 280 + BOX_WIDTH)),
                         outline=GREY, width=5)

        # Stars
        symbola = ImageFont.truetype("symbola.otf", 35)
        canvas.text((200, 210), star_set(self.stars), font=symbola, fill=WHITE)

        # Price
        arial30 = ImageFont.truetype("Arial Bold.ttf", 30)
        w, h = canvas.textsize(f"{self.currency}{self.price}", arial30)
        canvas.text((575 - w, 210), f"{self.currency}{self.price}", font=arial30, fill=WHITE)

        # Job name
        arial25 = ImageFont.truetype("Arial.ttf", 25)
        canvas.text((190, 620), self.name, font=arial25, fill=BLACK)

        # Job distance
        arial15 = ImageFont.truetype("Arial.ttf", 15)
        canvas.text((200, 650), f"{self.distance:.1f} {self.distanceunit} away, Posted {self.time:.0f} {self.timeunit} ago",
                    font=arial15, fill=BLACK)

        # Share button
        paste_image(phone, "share", 525, 630)

        # Time remaining
        canvas.text((200, 665), f"{self.remaining:.0f} {self.remainingunit} remaining",
                    font=arial15, fill=BLACK)

        # Description
        desc = textwrap.fill(self.description, 35)
        canvas.text((190, 710), desc, font=arial25, fill=BLACK)

        ############## PHONE
        # paste phone template overtop of what we've made:
        paste_image(phone, "phone")

        phone.save(filename)
