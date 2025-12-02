import time
import sys

def langsam(text,tempo=0.0001):
    for zeichen in text:
        print(zeichen, end="", flush = True)
        time.sleep(tempo)
    return ""

print(langsam("""Du öffnest deine Augen und siehst einen klaren Nachthimmel über dir. 'Das kann nicht sein!',denkst du dir.
Das letzte woran du dich erinnern kannst, ist das du dich Schlafen gelegt hast nach einem langen Tag, bei der Arbeit.
Du stehst auf und verschaffst dir einen Überblick wo du dich überhaupt befindest.
Du befindest dich in einem Wald. Die Fauna ist dir nicht bekannt, aber es erinnert dich an eine Mischung aus
mitteleuropäischem Wald und südamerikanischen Dschungel.
Es fällt dir auf das es ziemlich hell ist obwohl es nachts ist, ist etwa Vollmond?
Du schaust erneut in den Himmel und kannst deinen Augen nicht trauen!
Du siehst DREI Monde am Nachthimmel!
Zwei sind so groß wie der Mond und sind in ihrer Halbmondphase.
Der letzte Mond ist mindestens doppelt so groß und ist auf Vollmond.
Kein Wunder, dass du so gut in der Nacht sehen kannst!
Entweder bist du noch am träumen oder du wurdest auf einen komplett anderen Planeten transportiert!
Nachdem du den ersten Schock verdaut hast, entschließt du dich erstmal mehr Informationen zu sammeln.

Auf einmal hörst du etwas im Gebüsch rascheln!
Gehst du in Deckung oder bewegst du dich Richtung Gebüsch?"""))
entscheidung1 = input(langsam("Gib entweder 'Deckung' oder 'Gebüsch' ein: "))#.lower()

if entscheidung1 == "Deckung":
    print(langsam("""Du rennst hinter den nächstgelegenen Baum und versuchst so leise wie möglich zu sein.
Du siehst wie ein katzenähnliches Wesen mit 3 Schwänzen, einem grünbraunem Fell langsam in die Lichtung schlendert.
Es sieht aus wie eine Mischung aus Leopard, Gepard und Schimpanse. 
Es ist fast so groß wie ein Löwe mit sehr langen Fangzähnen. Es schaut sich um und streckt seine Nase in die Luft.
Versucht es etwa meine Fährte aufzunehmen? Es ist nur eine Frage der Zeit bis du entdeckt wirst!
Was machst du?"""))
    entscheidung11 = input(langsam("'Verstecken' oder 'angreifen'?: "))#.lower()
    if entscheidung11 == "Verstecken":
        print(langsam("""Du versuchst dich langsam von der Lichtung zu entfernen, ohne die Aufmerksamkeit des Wesens
auf dich zu ziehen. Schritt für Schritt  entfernst du dich, als du auf einmal ein Mischung aus Grollen und Lachen hinter dir hörst!
Du drehst dich um und siehst das Wesen nur 2 Meter hinter dir!
Du springst einen Satz zurück und schaust in die dunkelgelbenen Augen des wesen dir gegenüber.
Es beobachtet dich mit neugierigen Blick und einem schelmischen Grinsen?
Du hast noch nie so einen 'menschlichen Gesichtsausdruck an einem Nicht-Menschen gesehen!
"""))
        entscheidung111 = input(langsam("Was machst du? 'Ansprechen', 'angreifen' oder wegrennen?:"))
        if entscheidung111 == "Ansprechen":
            print(langsam("""Du siehst Intelligenz in den dunkelgelben Augen, vielleicht kannst du ja mit dem Wesen kommunizieren?
Spricht es vielleicht sogar eine Sprache? Anscheinend hat dich die Situation echt verrückt gemacht, wenn du in deiner Verzweiflung 
überlegst ein Tier anzusprechen.
'Ich bin kein Tier!' sagt eine tiefe Stimme.
Deine Augen weiten sich in Schock! Das Wesen hat seinen Mund nicht bewegt! 
'Ich kommuniziere direkt mit dir. Ich weiß ,dass euch Zweibeinern Telepathie etwas schwer fällt.'
Telepathie? Und hat das Wesen deine Gedanken gelesen?
'Ja das habe ich, anscheinend hattest du noch nicht deine Manaerweckung. Ansonsten wäre es nicht so einfach deine Gedanken zu lesen.'
Manaerweckung? Telepathie? Sprechende Fabelwesen und drei Monde am Nachthimmel?!? Wo zum teufel bist du aufgewacht?!
'Ah jetzt verstehe ich du bist ein Interdimensionaler Wanderer. Lass mich raten du bist hier aufgewacht und deine letzte Erinnerung
ist das du dich Schlafen gelegt hast?'
Ich nicke langsam.
'Mein Beileid, du bist ziemlich weit weg von der nächsten Menschensiedlung gelandet. Du bist nicht der erste Weltenhüpfer dem ich 
begegne.'
Eine andere Welt? Deine Befürchtungen sind also wahr! Wie kommst du nach Hause? Wie sollst du in einer dir nicht bekannten Welt überleben?
Das Wesen richtet sich auf,'Ich habe mich entschieden, da wir uns unter den Schicksalsmonden getroffen habe werde ich die Tradition der
Nekomata ehren und dir helfen.
Folge mir zu meiner Unterkunft! Dort kannst du dich erstmal ausruhen und auf dem Weg kannst du mir Fragen stellen.'
Du schluckst langsam und sagst: 'Vielen Dank Nekomata! Ich nehme deine Hilfe an.'
'Ich heiße Musato. Nekomata ist der Name des Volkes von dem ich Mitglied bin. Nun lass uns gehen, es ist angenehmer in meinem Haus
das gespräch weiterzuführen.' Es dreht sich um und fängt langsam an loszulaufen.
Ich laufe los und folge dem Wesen. Ich hatte wohl Glück das meine erste Begegnung, in einer neuen Welt,
mit einem freundlichen Wesen war. Eine neue Welt sprechende Fabelwesen, was wird mich noch hier erwarten? Aber das wichtigste ist, 
werde ich jemals mein zuhause wiedersehen?
FORTSETZUNG FOLGT!!
"""))
        elif entscheidung111 == "angreifen":
            print(langsam("""Du brüllst laut und rennst auf das Wesen zu. Du versuchst es mit Fußkick am Kopf zu treffen!
Das Wesen springt im letzten Moment aus dem Weg! Es repositioniert sich und springt mit ausgefahrenen Krallen auf dich!
Du versuchst auszuweichen, aber es ist zu schnell! Du siehst die Krallen immer näher kommen und spürst einen Schmerz an deiner Kehle!
Du siehst wie eine große Menge Blut aus deinem Hals strömt, dein Blick verdunkelt sich. Du drehst dich in die Richtung des Wesen.
Bevor du dich voll drehen kannst, siehst du die Krallen wieder genau vor deinen Augen! Deine Augen schwärzen sich.....  
DU BIST TOT!
ENDE"""))
        elif entscheidung111 == "wegrennen":
            print(langsam("""Du drehst dich wieder um un rennst so schnell wie dich deine Beine tragen können!
'Warte! Ich komme in Frieden!' Du hörst eine Stimme in deinem Kopf, spricht das Wesen etwas telepathisch in dir?
Es kommt in Frieden? Du rennst weiter! Das Risiko gehst du bei den langen Fangzähnen nicht ein! 
Du rennst tiefer in den Wald. Ohne Wegpunkt oder irgend eine Art von Orientierung hast du keine Ahnung wohin du läufst.
Das wesen scheint dich nicht zu verfolgen. Glück gehabt! 
Was wird dich in dieser verrückten Nacht noch erwarten?
FORTSETZUNG FOLGT!"""))
        else:
            print("Ungültige Eingabe!")
    elif entscheidung11 == "angreifen":
        print(langsam("""Du bist tot!"""))
        print("""Was hast du dir denn dabei gedacht? Dachtest du wirklich das du eine Chance hast gegen ein löwenähnliches Wesen im 1 vs 1?
Du hast wohl zu viel Rocky oder 300 gesehen""")
    else:
        print("Ungültige Eingabe!")
elif entscheidung1 == "Gebüsch":
    print(langsam("""Du bewegst dich vorsichtig in die Richtung aus der das Rascheln kommt. 
Das Geräusch wird immer lauter und du siehst dunkelgelbe Augen, die dich beobachten!
Oh nein! Es hat dich schon längst entdeckt!
Die Gestalt springt aus dem Gebüsch in deine Richtung!
Was machst du?"""))
    entscheidung12 = input(langsam("'Wegspringen' oder 'zuschlagen'?: "))#.lower()
    if entscheidung12 == "Wegspringen":
        print(langsam("""D"""))
        entscheidung122 = input(langsam("'Wegspringen' oder 'zuschlagen'?: "))#.lower()
        if entscheidung122 == "Wegspringen":
            print(langsam("""D"""))
        elif entscheidung122 == "zuschlagen":
            print(langsam("""Du bist tot!"""))
        else:
            print("Ungültige Eingabe!")
    elif entscheidung12 == "zuschlagen":
        print(langsam("""Du bist tot!"""))
        entscheidung123 = input(langsam("'Wegspringen' oder 'zuschlagen'?: "))#.lower()
        if entscheidung123 == "Wegspringen":
            print(langsam("""D"""))
        elif entscheidung123 == "zuschlagen":
            print(langsam("""Du bist tot!"""))
        else:
            print("Ungültige Eingabe!")
else:
    print("Ungültige Eingabe!")
print()