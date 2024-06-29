text = "X-DSPAM-Confidence:     0.8475"

pos = text.find(':')

next = text[pos+5:]
print(float(next))