import random
from PIL import Image, ImageDraw, ImageFont

colors =['#f44336', '#e81e63', '#9c27b0', '#673ab7', '#3f51b5', '#2196f3', '#03a9f4', '#00bcd4', '#009688', '#4caf50', '#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff9800', '#ff5722', '#795548', '#607d8b',]

image = Image.new('RGBA', (100, 100), random.choice(colors))
draw = ImageDraw.Draw(image)

font_size = 19
font_path = 'NotoSansJP-Medium.ttf ファイルパス'

font = ImageFont.truetype(font_path, font_size)
draw.text((50, 50), 'user_name', fill='#ffffff', font=font, anchor='mm')

image.save('保存先 ファイルパス')
