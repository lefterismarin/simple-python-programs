
import requests
food=input("ΠΛΗΚΤΡΟΛΟΓΗΣΤΕ ΣΤΑ ΑΓΓΛΙΚΑ ΤΟ ΦΑΓΗΤΟ ΠΟΥ ΕΠΙΘΥΜΕΙΤΕ: ")
link=('http://food2fork.com/api/search?key=07c976c6d603cd681bea1aab9816a0c3&count=1&q='+food)
r=requests.get(link)



print (r.text)
beer=('https://api.punkapi.com/v2/beers/random')
g=requests.get(beer)
if(r.text=='{"count": 0, "recipes": []}'):
    print("ΠΡΟΣΠΑΘΗΣΤΕ ΞΑΝΑ")
else:
    print ("ΟΡΙΣΤΕ ΚΑΙ ΜΙΑ ΜΠΥΡΑ ΓΙΑ ΝΑ ΤΟ ΣΥΝΟΔΕΨΕΤΕ: "+g.text)

