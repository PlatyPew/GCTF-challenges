def perform(level,box,options):
	for x in xrange(box.minx, box.maxx):
		for y in xrange(box.miny, box.maxy):
			for z in xrange(box.minz, box.maxz):
				if level.blockAt(x, y, z) != 23:
					level.setBlockAt(x,y,z,0)