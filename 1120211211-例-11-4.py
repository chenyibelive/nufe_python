import random
def zhufuyu():
	word_list =["万事如意","事事顺心","福寿安康","笑口常开","恭喜发财","步步高升","笑口常开"]
	word = random.choice(word_list)
	return word
zhufu= zhufuyu()
print("过年好，祝您{}".format(zhufu))
