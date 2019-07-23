import sys
from getopt import getopt
# import logging

log_level = "INFO"
opts, args = getopt(sys.argv[1:], "l:", ["log="])
for opt, arg in opts:
    if opt in ("-l", "--log"):
        log_level = arg.upper()
print(log_level)
# color = 'red'
# # logging.basicConfig(filename: './app-log.log', level: logging.INFO);
# if color is 'red':
#     print('red color')
