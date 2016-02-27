import math
import Leap

class PalmControlListener(Leap.Listener):
	def __init__(self):
		super(PalmControlListener, self).__init__()

	def on_init(self, controller):
		print "Initialized"

	def on_connect(self, controller):
		print "Connected"

	def on_disconnect(self, controller):
		print "Disconnected"

	def on_disconnect(self, controller):
		print "Disconnected"

	def on_frame(self, controller):
		frame = controller.frame()
		if not frame.hands.is_empty:
			if len(frame.hands) < 2:
				self.one_hand_gesture_recognition(frame.hands[0])
			else:
				#right_hand = max(frame.hands, key=lambda hand: hand.palm_position.x)
				#left_hand = min(frame.hands, key=lambda hand: hand.palm_position.x)
				right_hand = frame.hands.rightmost
				left_hand = frame.hands.leftmost
				self.two_hand_gesture_recognition(left_hand, right_hand)

	def one_hand_gesture_recognition(self, hand):
		normal = hand.palm_normal
		print normal.x, normal.y, normal.z
