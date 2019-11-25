import pickle
import sys


class SchoolFileReader:
    def schoolFileReader(self):
        f = open("data.txt", 'r')
        lines = f.readlines()
        for line in lines:

            item = line.split("   ")

            print("┌──────────────────────────┐")
            print("      이름 : "+item[0])
            print("      나이 : "+item[1])
            print("      학교 : "+item[2])
            print("      사이트 : "+item[3])
            print("└──────────────────────────┘")