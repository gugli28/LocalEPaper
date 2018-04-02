first_name = u'\u092e' + u'\u0928' + u'\u094b' + u'\u091c'
last_name = u'\u0905' + u'\u0935' + u'\u0938' + u'\u094d' \
+ u'\u0925' + u'\u0940'
 
print first_name + ' ' + last_name

from googletrans import Translator
translator = Translator()
translator.translate("whats your name",dest='hi')
a = translator.translate("whats your name",dest='hi')
# print a.encode('utf-8') 

akhbaar = u'\u0905'  + u'\u0916' +  u'\u093c'+ u'\u092c' + u'\u093e' + u'\u0930'
dinakit =  u'\u0926' + u'\u093f'  +  u'\u0928'+ u'\u093e' + u'\u0902' + u'\u0915' + u'\u093f'  + u'\u0924'
print akhbaar +' ' +dinakit

akhbaar = u'\u0905'  + u'\u0916' +  u'\u093c'+ u'\u092c' + u'\u093e' + u'\u0930'
k = u'\u0915'  + u'\u0943' +  u'\u092a'+ u'\u092f' + u'\u093e' 
s = u'\u0938'  + u'\u0902' +  u'\u0932'+ u'\u0917' + u'\u094d' + u'\u0928'
d = u'\u0922'  + u'\u0942' +  u'\u0902'+ u'\u0922' + u'\u093f' + u'\u090f'


print k+ ' ' + s + ' ' +akhbaar+ ' ' + d