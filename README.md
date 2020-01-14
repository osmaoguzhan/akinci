# akinci
The tool for getting ip addresses, mac addresses and opened ports on a network
# Usage
To Scan Ports:
python3 akinci.py -p <port>
  After -p you can put a port(-p 80), a range(-p 22-80), all ports(-p all) or common ports(-p common)
To list DB:
 python3 akinci.py -d <1,2,3,4>
  1: MAC
  2: IP Address
  3: Host IP
  4: All
 If u choose 1,2 or 3 you must type something.
