#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""A simple script to generate a CSV with sine data."""

import csv
import math
import psutil
import datetime
import time
import requests
ROWS = 100
SECONDS_PER_STEP= 30
DATE_FORMAT = "%m/%d/%y %H:%M"
def run(filename="cpu.csv"):
  print "Generating sine data into %s" % filename
  fileHandle = open(filename,"w")
  writer = csv.writer(fileHandle)
  writer.writerow(["timestamp","cpu"])
  writer.writerow(["datetime","float"])
  writer.writerow(["",""])
   
  for i in range(ROWS):
              response = requests.get('http://admin:admin@192.168.99.105:9090/api/v1/query?query=sum( 100 - (avg by(node_name) (irate(node_cpu{mode="idle"}[1m]) * on(instance) group_left(node_name) node_meta * 100)))')
              results = response.json()
              a = results['data']['result'][0]['value']
              if len(a) > 0:
                timestamp = datetime.datetime.fromtimestamp(
                  float(a[0])).strftime('%m/%d/%y %H:%M')
                cpu_value = float(a[1])
                writer.writerow([timestamp, cpu_value])
              try:
                plt.pause(SECONDS_PER_STEP)
              except:
                pass
  fileHandle.close()
  print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
