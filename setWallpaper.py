# Module for setting an image as the wallpaper in Windows

import ctypes
from ctypes import wintypes

def set_wallpaper(image_path):
    """
    Sets a given image as the wallpaper
    """

    SPI_SETDESKWALLPAPER    = 0x0014
    SPIF_UPDATEINFILE       = 0x0001
    SPIF_SENDWININICHANGE   = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    # print(SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINFILE | SPIF_SENDWININICHANGE))
    return SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINFILE | SPIF_SENDWININICHANGE)
