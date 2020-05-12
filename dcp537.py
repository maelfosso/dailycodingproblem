"""
This is your coding interview problem for today.

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
"""

def collatz(n):
  s = n
  seq = [s]
  while s != 1:
    if s % 2 == 0:
      s = s / 2
    else:
      s = 3 * s + 1

    seq.append(int(s))

  return seq

def longest(max):
  min = 0
  value = 0
  seq_len = dict()

  for n in range(2, max + 1):
    s = n
    seq = [s]
    while s != 1:
      if s in seq_len:
        seq_len[n] = len(seq) + seq_len[s]
        break
      else:
        if s % 2 == 0:
          s = s / 2
        else:
          s = 3 * s + 1

        seq.append(int(s))
    
    if s == 1:
      seq_len[n] = len(seq)

    if min < len(seq):
      min = len(seq)
      value = n

  return n, min

    

