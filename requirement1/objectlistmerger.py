"""
-------------------------------------------------------------------------------------------------
Developer: Harsh Munshi

Intent: Object list merger. Merging the contents of the list from readings from various sensors

Sensors: RGB, RGBD cameras
-------------------------------------------------------------------------------------------------
"""

import os, sys
import configparser
import math

class Defaults(object):
	"""A parent class that contains all the resquired defaults """
	def __init__(self, arg):
		super(Defaults, self).__init__()
		self.arg = arg


"""
Approach:

If the "class" detected by all the sensors (two in this case) is not the same:
	Go with the one with higher probability.
else if classes are the same:
	probabilistic approach

How do we determine the probabilities:
- Check if priors are given. Let's say we have an entry (spoon, 3, 33%)
- Do we know that is p(knife|spoon)?
- We do know that p(others|spoon) = 1-33 = 77%.
- Assuming every object is likely, p(knife) = p(scissor) = p(fork) = p(spoon) = p(keys) = 0.2
- With this assumption, p(object1|object2) = p(object2|object1)
- Now for the same object, the options are 33 and 99
- Which means that there was a 77% chance that it would have been other object.
- Using belief propogation, p(knife) = p(knife|knife,others).p(others|spoon)
- So in this example p(knife) = 0.77*0.99 = 0.7623
- And p(spoon) = 0.01*0.33 = 0.0033
- Adding a normalizer,
  * p(knife) = (1/(0.0033+0.7623))*0.7623 = 0.9956
  * p(spoon) = 1 - 0.9956 = 0.00xx
"""

