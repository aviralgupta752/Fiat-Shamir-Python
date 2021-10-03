# Fiat Shamir Protocol
Python implementation of Fiat-Shamir Protocol.

## Installation
```bash
git clone https://github.com/noob-aViral/Fiat-Shamir-Python.git
cd Fiat-Shamir-Python
pip3 install -r requirements.txt
```
## Description
1. A chooses a random r in the interval (1, n-1) and sends r<sup>2</sup>%n to B.
2. B randomly selects a bit e (0 or 1) and sends it to A.
3. A computes (r(v<sup>e</sup>))%n and sends it back to B.
4. Party B checks the equality y<sup>2</sup>=(x(v<sup>e</sup>))%n. If it is true, it proceeds to the next round of the protocol, otherwise the proof is not accepted.

## Usage
```bash
python3 code.py
```

## Sample Output
<b>Note: </b> Output will be different for different run.
![Sample](ss.jpg)
```python
Alice has the secret.
Message         =  5496901626695654754356153835892
Prime           =  647467
r               =  360265
x               =  282872
e               =  1
y               =  447574
y**2            =  80478
(x*(v**e))      =  80478
```