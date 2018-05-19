#!/usr/bin/env python
# Copyright 2018 Lucas Walter
#

import math
import random
import sys
import telnetlib

from time import sleep


class McPy:
    def __init__(self, player_name=None):
        self.tl = telnetlib.Telnet('mc.livingcomputers.org', 4711)
        # player_ids = mc.getPlayerEntityIds()
        # print player_ids
        # if player_name is None:
        print player_name
        if player_name is None:
            return

        while True:
            self.player_state(player_name)
            sleep(0.1)

        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print 'shutting down'
        self.tl.close()

    def player_state(self, player_name):
        pos = self.get_pos(player_name)
        sys.stdout.write("x %f, y %f, z %f\r" % (pos[0], pos[1], pos[2]))
        sys.stdout.flush()

    def get_pos(self, player_name):
        self.tl.read_very_eager()
        # self.tl.write('player.getTile(' + player_name + ')\n')
        self.tl.write('player.getPos(' + player_name + ')\n')
        rv = self.tl.read_until(b'\n')
        rv.rstrip('\n')
        pos = [float(x) for x in rv.split(',')]
        # print pos, len(pos), type(pos)
        return pos

    # get all blocks from point 0 to point 1 inclusive
    def get_blocks(x0, y0, z0, x1, y1, z1):
        pass
        # blocks = mc.getBlocks(x0, y0, z0, x1, y1, z1)
        # blocks = [int(x) for x in (blocks.rstrip('\n').split(','))]
        # return blocks

if __name__ == "__main__":
    player_name = None
    if len(sys.argv) > 1:
        player_name = sys.argv[1]

    with McPy(player_name) as mc:
        print 'test'
        # sleep(1.0)
