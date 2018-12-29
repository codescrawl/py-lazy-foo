import sys

from sdl2 import *  # pylint: disable=W0614

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def init():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(
        b"Example 2",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SDL_WINDOW_SHOWN,
    )
    window_surface = SDL_GetWindowSurface(window)
    return window, window_surface


def close(bmp, window):
    SDL_FreeSurface(bmp)
    SDL_DestroyWindow(window)
    SDL_Quit()


def main():
    window, window_surface = init()
    bmp = SDL_LoadBMP(b"resources/hello_world.bmp")
    SDL_BlitSurface(bmp, None, window_surface, None)
    SDL_UpdateWindowSurface(window)
    SDL_Delay(2000)
    close(bmp, window)


if __name__ == "__main__":
    sys.exit(main())
