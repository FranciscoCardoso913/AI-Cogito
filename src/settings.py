# define display characteristics
WIDTH = 1280
HEIGHT = 720
FPS = 60
LEVELS_DIR = "levels/"
FONT_PATH = "assets/Comfortaa-Regular.ttf"

# define used colors in game:
BACKGROUND_COLOR = (255, 255, 255)
WHITE_COLOR = (230, 230, 230)
RED_COLOR = (255, 99, 99)
BLUE_COLOR = (100, 100, 255)
YELLOW_COLOR = (255, 235, 98)
GREEN_COLOR = (74, 200, 73)
BLACK_COLOR = (0,0,0)

# define view GAME
GAP = 3
OFFSET = 25
W_SQUARE = 30
H_SQUARE = 30
R_SQUARE = 6

Y_LEFT_MENU = 25
W_LEFT_MENU = int(WIDTH / 256 * 85)
X_LEFT_MENU = WIDTH - Y_LEFT_MENU - W_LEFT_MENU
H_LEFT_MENU = HEIGHT - Y_LEFT_MENU - Y_LEFT_MENU
R_LEFT_MENU = 23

X_3COLORS = X_LEFT_MENU + 20
Y_3COLORS = Y_LEFT_MENU + 20

W_MISS = 15
H_MISS = 42
R_MISS = 6

# define view MENU
W_BUTTON = 250
H_BUTTON = 50
R_BUTTON = 20

ARROW_W = 40
ARROW_H = 40
ARROW_R = 20
ARROW_FONT_S = 30
