import sys
import ctypes

from sdl2 import *  # pylint: disable=W0614

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def init():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(
        b"Example 3",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SDL_WINDOW_SHOWN,
    )
    window_surface = SDL_GetWindowSurface(window)
    return window, window_surface


def loadMedia():
    return SDL_LoadBMP(b"resources/x.bmp")


def close(bmp, window):
    SDL_FreeSurface(bmp)
    SDL_DestroyWindow(window)
    SDL_Quit()


def main():
    window, window_surface = init()
    bmp = loadMedia()
    quit = False
    event = SDL_Event()
    while not quit:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                quit = True

        SDL_BlitSurface(bmp, None, window_surface, None)
        SDL_UpdateWindowSurface(window)

    close(bmp, window)

    return 0

if __name__ == "__main__":
    sys.exit(main())