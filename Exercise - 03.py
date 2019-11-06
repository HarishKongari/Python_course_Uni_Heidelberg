# BITTE FOLGENDEN TEXT NICHT VERÄNDERN
corpus_text = """ENGLAND, Anno Domini 932 Halt ein! Halt! Wer geht dort?
Ich bin es, Artus, Sohn des Uther Pendragon, vom Schloss Camelot. König der
Briten, Sieger über die Sachsen. Herrscher über ganz England! Ich kenne
bessere Witze. Das bin ich aber, und dies ist mein treuer Diener Patsy. Wir
reiten quer durch das ganze Land, auf der Suche nach Rittern, die mir auf
meinen Hof in Camelot folgen. Ich muss deinen Herrn und Meister sehen. -Wie?
Auf einem Pferd geritten? -Ja. -Ihr benutzt Kokosnüsse! -Was? Ihr habt zwei
leere Kokosnusshälften und die klopft Ihr aneinander. Und? Wir reiten, seit
der Winterschnee die Lande zu bedecken begann. -Durch das Königreich
Mercia. -Wo habt ihr die Kokosnüsse her? Wir fanden sie. Fandet sie? In
Mercia? Die Kokosnuss ist eine tropische Frucht. -Was meint Ihr? -Dies ist
eine gemäßigte Klimazone. Die Schwalbe zieht mit der Sonne südwärts, die
Mehlschwalbe, der Kiebitz... mögen im Winter wärmere Gefilde suchen und doch
sind sie uns nicht unbekannt. -Wollt Ihr sagen, die Kokosnuss wandert?
-Keineswegs. Sie könnte getragen werden. -Was? Eine Schwalbe trägt ne
Kokosnuss? -Sie könnte sie an der Hülle packen. Die Frage ist nicht, wo sie
sie packt, sondern die der Gewichtsverhältnisse. Ein Vogel mit 150 Gramm
trägt keine 500-Gramm Kokosnuss. Das ist unwichtig. Geh und sag deinem
Herrn, dass Artus aus Camelot hier ist. Um ihre Fluggeschwindigkeit zu
gewährleisten, muss eine Schwalbe 43 Mal pro Sekunde mit den Flügeln schlagen,
stimmts? -Bitte! -Habe ich Recht? -Das interessiert mich nicht. -Ne
afrikanische Schwalbe kann es tragen. O ja! Eine afrikanische Schwalbe
vielleicht. Aber keine europäische. Das meine ich. Da stimme ich zu. Wirst du
deinen Meister fragen, ob er mich an meinen Hof in Camelot begleiten will?
Allerdings sind afrikanische Schwalben keine Zugvögel. -Oh, ja. -Die schaffen
sowieso keine Kokosnuss. Moment mal! Wenn aber zwei Schwalben eine Nuss
zusammen trügen? -Nein, sie bräuchten eine Schnur. -Ganz einfach. Ein Stück
Schlingpflanze. -Unter den Rückenleitfedern? -Warum nicht?"""

##############################################################################
# LÖSUNG AUFGABE 1
##############################################################################
#puntkte vom string entfernen
dot = corpus_text.replace(".","")
#fragezeichen entfernen
fragezeichen = dot.replace("?","")
#ausrufezeichen entfernen
ausrufezeichen = fragezeichen.replace("!","")
#commas entfernen
commas = ausrufezeichen.replace(",","")
#striche entfernen
striche = commas.replace("-","")
#zeilenumbrueche ersetzen
zeilenumbrueche = striche.replace("\n"," ")
#alles nur mit kleinen Buchstaben
kleinbuchstaben = zeilenumbrueche.lower()
#string zu eine andere Variable kopieren
corpus_text_cleaned = kleinbuchstaben
#Gesammtergebnis ausgeben
print(corpus_text_cleaned)

##############################################################################
# LÖSUNG AUFGABE 2
##############################################################################

print(len(corpus_text_cleaned.split()))

##############################################################################
# LÖSUNG AUFGABE 3
##############################################################################

d = {}
words = ["kokusnuss", "rückenleitfeder", "zugvogel", "england", "afrika"]
split_text = corpus_text_cleaned.split()

for i in (words):
boo = corpus_text_cleaned.find(i)
if boo == -1:
a = False
else:
a = True
d = {i : a}
print(d)


##############################################################################
# LÖSUNG AUFGABE 4
##############################################################################

x = {"Denethor", "Smaug", "Turambar"}
y = {"Smaug", "Tom Bombadil", "Varda"}
unique_elements=(x.difference(y), y.difference(x))
overlapping_elements=(x.intersection(y))
print((unique_elements), (overlapping_elements))

##############################################################################
# LÖSUNG AUFGABE 5
##############################################################################

sentence = "Zwölf laxe Typen qualmen verdächtig süße Objekte"
a = sentence.lower()
b = "".join(set(a))
abc = "".join(sorted(b))
print(abc)
