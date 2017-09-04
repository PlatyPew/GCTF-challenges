#!/usr/bin/env python

import hashpumpy

#file = str(',' + raw_input('> '))
file = ',/proc/self/environ';
new_hash, msg = hashpumpy.hashpump('5dcd3edd3680496a165bfd2a1b3fec397cde0a12','filelocation,list.txt', file ,20)
print 'File:', msg.encode('hex')
print 'Hash:', new_hash
