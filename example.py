#!/usr/bin/env python

import time
import numpy
from sos_connection import SOSConnection

###############################################################################
# Number of seconds to show the flights image
IMAGE_DURATION = 120

# Name of image to display
IMAGE_NAME = "/shared/sos/json/dataset/flights.png"

# Fade step size
FADE_STEP_SIZE = 0.005
###############################################################################

# alpha_start: Start of alpha value for fade. Valid values are [0.0-1.0].
# alpha_end: End of alpha value for fade. Valid values are [0.0-1.0].
# step: How much to change alpha at each iteration. (Negative value should be
#       used if decrementing (i.e. fading out)).

log = open("/shared/sos/json/logs/AVedge.txt","a")
log.writelines("-----CONNECTION Attempting----" + timestr +"\n")
log.close()

def fade(alpha_start, alpha_end, step):
    for i in numpy.arange(alpha_start, alpha_end, step):
        conn.send("layer top alpha {0}".format(i))


if __name__ == '__main__':

    # Connect to SOS.
    conn = SOSConnection()
    conn.connect()

    # Load clip.
    conn.send("play 1")

    while True:
        # Load overlay.
        conn.send("overlay {0}".format(IMAGE_NAME))

        # Fade in overlay from 0.0 to 1.0 using fade step size.
        fade(0.0, 1.0, FADE_STEP_SIZE)

        # Sleep n seconds until next frame arrives
        time.sleep(IMAGE_DURATION)

        # Fade out overlay from 1.0 to 0.0 using fade step size.
        fade(1.0, 0.0, -FADE_STEP_SIZE)

        # Delete overlay.
        conn.send("layer top delete")
