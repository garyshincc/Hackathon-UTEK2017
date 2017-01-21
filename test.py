from multiprocessing import Process
import multiprocessing as mp
import os
import sys


def non_daemon():
	num = 0
	for i in xrange(10000):
		for j in xrange(1000):
			num = num + 1

	print "done"



def main():
	process = mp.Process(name = '0', target = non_daemon, args = ())
	process.daemon = False

	process_1 = mp.Process(name = '1', target = non_daemon, args = ())
	process_1.daemon = False


	process.start()
	process_1.start()

	process.join()
	process_1.join()



if __name__ ==  '__main__':
	main()
	sys.exit()
