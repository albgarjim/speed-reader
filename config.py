from enum import Enum


class Format(Enum):
    PDF_ONE = 1
    PDF_TWO = 2
    TEXT = 3
    URL = 4


page_words = []

# ===================== Back mode config =====================
refresh_slow = 470
refresh_fast = 350
back_words = 30  # equivalent of going back 6 seconds at 600 wpm

# ===================== Layout modifiers =====================
w_width = 350
w_height = 60
font_siz = 22
bg_color = "#413c58"
font_color = '#9a8c98'
# bg_color = "#2d2f37"
# font_color = '#797596'

# ===================== Content =====================
refresh = 350
max_width = 12

p_start = 46  # inclusive
p_end = 66  # no inclusive
book_path = './my_txt.txt'

format_type = Format.TEXT
