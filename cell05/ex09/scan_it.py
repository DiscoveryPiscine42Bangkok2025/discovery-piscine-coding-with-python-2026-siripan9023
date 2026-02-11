#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    string_to_search = sys.argv[2]
    
    count = string_to_search.count(keyword)
    
    if count == 0:
        print("none")
    else:
        print(count)