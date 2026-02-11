#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    string_param = sys.argv[1]
    
    z_count = string_param.count('z')
    
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)