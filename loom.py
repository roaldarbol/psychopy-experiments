import numpy as np
from psychopy import visual, core, event

#create some stimuli
class loom:
	def __init__(self, win, size, expTime, iti, stimColor):

		# Window
		self.win = win

		# Stimulus
		self.startSize = 0
		self.endSize = size
		self.stimColor = stimColor
		self.loomObj = visual.Circle(win=self.win, fillColor=self.stimColor, pos=[0,0])
		self.loomObj.size = self.startSize

		# Timing
		self.expTime = expTime
		self.iti = iti
		self.fps = win.getActualFrameRate()
		self.expRateInit = self.endSize / (((1/1.02)*self.expTime) * self.fps)
		self.expRate = self.expRateInit


	def draw(self):
		self.loomObj.draw()

	def expand(self):
		if self.loomObj.size < self.endSize:
			self.expRate = 1.02 * self.expRate
			self.loomObj.size = self.loomObj.size + self.expRate
		else:
			self.loomObj.size = self.startSize
			self.expRate = self.expRateInit
			i = 0
			running = False


	def run_exp_loop(self):
		"""Run experimental loop"""
		running = False
		expanding = False

		while True:
			if running == True:
				if expanding == True:
					if self.loomObj.size < self.endSize:
						self.expRate = 1.02 * self.expRate
						self.loomObj.size = self.loomObj.size + self.expRate
					else:
						running = False

				if expanding == False:
					if self.loomObj.size > self.startSize:
						self.expRate = 1/1.02 * self.expRate
						self.loomObj.size = self.loomObj.size - self.expRate
					else:
						self.loomObj.size = self.startSize
						self.expRate = self.expRateInit
						running = False
						

			self.draw()
			self.win.flip()

			if event.getKeys(['space']):
				running = True
				if expanding == False:
					expanding = True
				else:
					expanding = False

			if event.getKeys(['q']):
				break
			event.clearEvents()

	def play(self):
		self.run_exp_loop()