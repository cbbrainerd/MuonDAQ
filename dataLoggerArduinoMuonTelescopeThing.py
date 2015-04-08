import serial
import sys
#import numpy
#from pyqtgraph import QtCore, QtGui
#from pyqtgraph import multiprocess as mp
#import pyqtgraph as pg
import time
import datetime
#from collections import deque
#from matplotlib import pyplot as pltar

port = sys.argv[1];
#outputFile = open('goodData.txt', 'a');
#latchFile = open('rates.txt', 'a');

try:
  ser = serial.Serial(port, 115200, timeout=1)
except IOError:
  print port, ' CANNOT BE OPENED. TERMINATING SCRIPT';
  sys.exit();

aFile = open('logFile', 'w')
#inputFile = open('runs.txt', 'r')

#serialEvent(ser)               

initTime = time.time()

while (1):
    line = ser.readline();
    if len(line) > 0:
        timeNow = time.time();
        timeNowStr = str(timeNow);
        printMe = timeNowStr+":"+line;
        aFile.write(printMe);
        sys.stdout.write(printMe);
    	#sys.stdout.write(line);
	#words = line.split();
	#print(words);
	#print("\n");
#	if words[0] == "CD":
#		try:		
#			dataInt = int(words[1], 16);
#		except ValueError:
#			sys.stdout.write("Value Error\n")		
#        elif words[0] == "NR":
#		del words[0];
#		for holder in words:
#			try:		
#				badRead = int(holder, 16);
#				if badRead != dataInt:
#					totalBad = totalBad + 1;
#			except ValueError:
#				sys.stdout.write("Value Error\n")						
#		
#		if totalBad == (len(words)):
#			latches = latches + 1

#		else:
#			upsets = upsets + len(words) + 1
#		totalBad = 0;

#    	if (time.time() - initTime) > 5.0:
#		upsets = upsets / 5.0;
#		latches = latches / 5.0;
#		netLatchesString = "LATCH RATE: " + str(latches) + "\n";
#		sys.stdout.write(netLatchesString)
#		netLatchesString = str(time.time()) + ": " + netLatchesString;
#		
#		latchFile.write(netLatchesString)

#		netUpsetsString = "UPSET RATE: " + str(latches) + "\n";
#		sys.stdout.write(netUpsetsString);
#		netUpsetsString  = str(time.time()) + ": " + netUpsetsString;
#		latchFile.write(netUpsetsString);
#		initTime = time.time();	
#    		latches = 0;
#    		upsets = 0;
#    
#    holderString = str(time.time()) + ": " + line;
#    	    
#    outputFile.write(holderString);
#    outputFile.write('\n');

ser.close()


