
image solid_snow_small = Transform(Solid("FFF", xysize=(3, 3)), rotate=45)
image solid_snow_normal = Transform(Solid("FFF", xysize=(5, 5)), rotate=45)
image solid_snow_large = Transform(Solid("FFF", xysize=(7, 7)), rotate=45)


image snowing = Fixed(
    Snowing("solid_snow_large", speed=(5.0, 5.8), slow_start=(7, (0.6, 0.9))),
    Snowing("solid_snow_normal", speed=(4.8, 5.2), slow_start=(7, (0.8, 1.2))),
    Snowing("solid_snow_small", speed=(4.3, 4.7), slow_start=(5, (0.5, 0.7))))


transform particle(d, delay, startpos, endpos, speed):
    subpixel True
    pause delay
    d
    pos startpos
    linear speed pos endpos

layeredimage snow:
    if game.season == 3:
        "snowing"

init python:
    
    class Snowing(renpy.Displayable, NoRollback):
        def __init__(self, d, interval=(0.2, 0.3), start_pos=((-200, config.screen_width), 0), end_pos=({"offset": (100, 200)}, config.screen_height), speed=4.0, slow_start=False, transform=particle, **kwargs):
            """Creates a 'stream' of displayable...

            @params:
            -d: Anything that can shown in Ren'Py.
            -interval: Time to wait before adding a new particle. Expects a tuple with two floats.
            -start_pos: x, y starting positions. This expects a tuple of two elements containing either a tuple or an int each.
            -end_pos: x, y end positions. Same rule as above but in addition a dict can be used, in such a case:
                *empty dict will result in straight movement
                *a dict containing an "offset" key will offset the ending position by the value. Expects an int or a tuple of two ints. Default is (100, 200) and attempts to simulate a slight wind to the right (east).
            -speed: A time before particle reaches the end_pos. Expects float or a tuple of floats.
            -slow_start: If not the default False, this will expect a tuple of (time, (new_interval_min, new_interval_max)):
                *This will override the normal interval when the Displayable is first shown for the "time" seconds with the new_interval.
            -transform: ATL function to use for the particles.

            The idea behind the design is to enable large amounts of the same displayable guided by instructions from a specified ATL function to
            reach end_pos from start_pos in speed amount of seconds (randomized if needs be). For any rotation, "fluff" or any additional effects different ATL funcs with parallel can be used to achieve the desired effect.
            """
            super(Snowing, self).__init__(**kwargs)
            self.d = renpy.easy.displayable(d)
            self.interval = interval
            self.start_pos = start_pos
            self.end_pos = end_pos
            self.speed = speed
            self.slow_start = slow_start
            self.transform = transform
            
            self.next = 0
            self.shown = {}
        
        def render(self, width, height, st, at):
            
            rp = store.renpy
            
            if not st:
                self.next = 0
                self.shown = {}
            
            render = rp.Render(width, height)
            
            if self.next <= st:
                speed = rp.random.uniform(self.speed[0], self.speed[1]) if isinstance(self.speed, (list, tuple)) else self.speed
                
                posx = self.start_pos[0]
                posx = rp.random.randint(posx[0], posx[1]) if isinstance(posx, (list, tuple)) else posx
                
                posy = self.start_pos[1]
                posy = rp.random.randint(posy[0], posy[1]) if isinstance(posy, (list, tuple)) else posy
                
                endposx = self.end_pos[0]
                if isinstance(endposx, dict):
                    offset = endposx.get("offset", 0)
                    endposx = posx + rp.random.randint(offset[0], offset[1]) if isinstance(offset, (list, tuple)) else offset
                else:
                    endposx = rp.random.randint(endposx[0], endposx[1]) if isinstance(endposx, (list, tuple)) else endposx
                
                endposy = self.end_pos[1]
                if isinstance(endposy, dict):
                    offset = endposy.get("offset", 0)
                    endposy = posy + randint.randint(offset[0], offset[1]) if isinstance(offset, (list, tuple)) else offset
                else:
                    endposy = rp.random.randint(endposy[0], endposy[1]) if isinstance(endposy, (list, tuple)) else endposy
                
                self.shown[st + speed] = self.transform(self.d, st, (posx, posy), (endposx, endposy), speed)
                if self.slow_start and st < self.slow_start[0]:
                    interval = self.slow_start[1]
                    self.next = st + rp.random.uniform(interval[0], interval[1])
                else:
                    self.next = st + rp.random.uniform(self.interval[0], self.interval[1])
            
            tmp_pos = list(self.shown.keys())
            for d in copy.copy(tmp_pos):
                if d < st:
                    del(self.shown[d])
                else:
                    d = self.shown[d]
                    if not d.xpos:
                      d.xpos = 0
                    if not d.ypos:
                      d.ypos = 0
                    render.blit(d.render(width, height, st, at), (d.xpos, d.ypos))
            
            rp.redraw(self, 0)
            
            return render
        
        def visit(self):
            return [self.d]

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
