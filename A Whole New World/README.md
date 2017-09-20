# A Whole New World
A challenge to kill technically skilled people.

<i>Creators - @Platy &amp; @pauxy</i>

## Category
Misc

## Question
>I found this weird file in my computer and can't remember what it's for... :(
>
>PLEASE HALP ME SEDMAN :( *CRIES*

### Hint
I've been playing lots of games lately. I hope I can still score at least GPA 2.5

## Setup Guide
1. Run mcedit select an area. Run the `randomGen.py` filter.
2. Go into Minecraft and put a random dispenser with a book containing the flag.

## Distribution
A zip file containing Minecraft world save data
- A whole new world.zip
	- region
	- level.dat

## Solution
There are multiple ways to solve this challenge.

Firstly, you must know how that the zip files contain Minecraft world save data.

<b>Run Minecraft Commands and search for dispenser</b>

Create a entity to represent a pointer.

Use `/execute ~ ~ ~ detect ~ ~ ~ minecraft:dispenser /say Found Dispenser!` or `/fill <x1> <y1> <z1> <x2> <y2> <z2> air 0 replace <block id>`

Run and search blah blah blah <b>NOPE!</b>

<b>Brute force</b>

Find it manually in the quarter of a million possible blocks. Good luck with that

<b>Smart brute force</b>

Run a very old version of Minecraft to remove most of the blocks and search for dispenser.

<b>Use mcedit filter</b>

Just ~~steal~~ write a small mcedit filter to delete all blocks except dispensers

```python
def perform(level,box,options):
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if level.blockAt(x, y, z) != 23:
					level.setBlockAt(x,y,z,0)
```

This is stupid yet ingenious.

### Flag
`GCTF{0n3_1n_4_m1ll10n}`

## Credits
None.

## Recommended Reads
- https://github.com/mcedit/mcedit
- https://www.youtube.com/watch?v=NIRDHS3_xMQ&list=PL1nWzwiv3nc2dSOtVihY_AQE_1INse74T
