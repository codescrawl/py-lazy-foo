import sys

from sdl2 import *  # pylint: disable=W0614

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(
        b"Example 1",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SDL_WINDOW_SHOWN,
    )
    screen_surface = SDL_GetWindowSurface(window)
    SDL_FillRect(
        screen_surface, None, SDL_MapRGB(screen_surface.contents.format, 0xFF, 0xFF, 0xFF)
    )
    SDL_UpdateWindowSurface(window)
    SDL_Delay(2000)
    SDL_DestroyWindow(window)
    SDL_Quit()


if __name__ == "__main__":
    sys.exit(main())
