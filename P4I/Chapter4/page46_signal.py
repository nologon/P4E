#!/usr/bin/python
import math
signal_power = 10
noise_power = 9
ratio = signal_power // noise_power
decibels = 10 * math.log10(ratio)
print decibels
