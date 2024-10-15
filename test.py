import random
import sys
import struct
import numpy as np
from threading import Timer
import time


fl = 4
chunk_len = 1024


def main ():
  chunks = np.zeros(chunk_len)
  counts = 0
  r = Timer(0.1, lambda x: print(counts), '1')
  r.start()  
  while True:
      value = random.uniform(-1, 1)
      chunks = np.append(chunks[1:len(chunks)], value)
      counts = counts + 1

      sys.stdout.buffer.flush()
      for v in chunks:
        sys.stdout.buffer.write(struct.pack("f", v))
    

main()

