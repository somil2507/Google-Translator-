from googletrans import Translator

translator = Translator()

out = translator.translate("Insomnia is a common sleep disorder that can make it hard to fall asleep, hard to stay asleep, or cause you to wake up too early and not be able to get back to sleep. You may still feel tired when you wake up. Insomnia can sap not only your energy level and mood but also your health, work performance and quality of life.", dest='hi')


print("Hindi -> English : ", out.text)
#
# print("\n")
# out1 = translator.translate(out, dest='en')
#
# print("English -> Hindi : ", out1.text)