##pip install googletrans #to install googletrans
##pip install googletrans==4.0.0-rc1  (solved)
  
  
##To check supported languages
# import googletrans

# l=googletrans.LANGUAGES
# for i in l:
#   print(f'{i} - {l[i]}')
  
  
##method-1
# import googletrans

# gt=googletrans.Translator()
# t=gt.translate('मेरा नाम एलेक्सा है')
# print(f'Source: {t.src}')
# print(f'Destination:  {t.dest}')
# print(f'{t.origin} -> {t.text}')
  
  
##method-2
# import googletrans

# gt=googletrans.Translator()
# t=gt.translate('my name is alexa', src='en', dest='hi')
# print(f'Source: {t.src}')
# print(f'Destination:  {t.dest}')
# print(f'{t.origin} -> {t.text}')
  
  
##method-3
# import googletrans

# gt=googletrans.Translator()
# t=gt.translate('मेरा नाम एलेक्सा है')
# data=t.text
# print(data)

  
##method-4
import googletrans

gt=googletrans.Translator()
t=gt.translate('what is your name?', src='en', dest='hi')
data=t.text
print(data)