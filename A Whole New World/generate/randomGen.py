from random import choice 

blocks = [1,2,3,4,5,7,14,15,16,17,19,20,21,22,24,25,35,41,42,57,58,87,88,89,91,95,99,100,103,110,112,121,123,133,152,155,159,162,165,168,169,170,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250]

def perform(level,box,options):
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				randomBlock = choice(blocks)
				level.setBlockAt(x, y, z, randomBlock)
				