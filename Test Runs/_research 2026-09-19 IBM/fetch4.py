import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch2 import grab
grab('0001558370-23-002376','ibm-20221231xex13.htm','AR_FY2022.txt')
grab('0001558370-22-001584','ibm-20211231xex13.htm','AR_FY2021.txt')
