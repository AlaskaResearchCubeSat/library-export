#!/usr/bin/env python

import os
import subprocess

libraries=("ARClib","ErrorLib","I2Clib","SD-lib","UART-lib","commands","termlib")

#first export headers
for lib in libraries:
	print("Exporting "+lib)
	script=os.path.join(os.path.join("./",lib),"export.py")
	print("Running '"+script+"'")
	rc=subprocess.call(["python",script,"--only-headers"])
	#check return code
	if rc!=0:
		print("Error : failed to export headers")
		exit(rc)

#next export full libraries
for lib in libraries:
	script=os.path.join(os.path.join("./",lib),"export.py")
	rc=subprocess.call(["python",script])
	#check return code
	if rc!=0:
		print("Error : failed to export library")
		exit(rc)

print("All libraries exported successfully!")