#!/usr/bin/python


print('Willkommen zu Tabeas kleinem Akustik-Quiz')
print('Welche Antwort/en sind richtig?')
print('''Schreibe immer den richtigen Buchstaben der Antwortmoeglichkeiten als Antwort in das entsprechende Feld!
    Sind mehrere Antworten richtig, schreibe die jeweiligen Buchstaben mit einem Leerzeichen getrennt in das Feld.''')
answer=input('''Bist du bereit?
A: Ja
B: Nein
Answer:''')
score=0
total_questions=6
 
if answer.lower()=='a' or answer.lower()=='ja':
    answer=input('''Welches Geraet wandelt Strom in akustische Energie um?
    A: Mikrofon
    B: Kopfhoerer
    C: Verstaerker
    D: Vorverstaerker
    Antwort:''')
    
    if answer.lower()=='b':
        score += 1
        print('Richtig! Kopfhoerer sind elektroakustische Wandler, die ein elektrisches Signal in einen Ton umwandeln.')
    else:
        print('Leider falsch... Richtig waere B: Kopfhoerer')
 
    answer=input('''Zwischen welchen Frquenzen nimmt das menschliche Ohr Geraeusche wahr?
    A: 100-10.000Hz
    B: 50-50.000Hz
    C: 20-20.000Hz
    D: 120-12.000Hz
    Antwort:''')
    if answer.lower()=='c':
        score += 1
        print('Richtig! Menschen koennen Frequenzen zwischen 20 - 20.000Hz hoeren, wobei der genaue Bereich auch von alter und anderen persoenlichen Umstaenden abhaengt.')
    else:
        print('Leider falsch... Richtig waere C: 20-20.000Hz')
        
    answer=input('''Welches Objekt ist keine Schallquelle?
    A: Trompete
    B: Handy
    C: Ohr
    D: Wecker
    Antwort:''')
    if answer.lower()=='c':
        score += 1
        print('Richtig! Das Ohr ist keine Schallquelle')
    else:
        print('Leider falsch... Richtig waere C: Das Ohr')
        
    answer=input('''Wann hoeren wir keinen Schall?
    A: in einem Vakuum
    B: im Wasser
    C: in der Luft
    D: wenn die Schallquelle in einem Schaumstoff ist
    Antwort:''')
    if answer.lower()=='a':
        score += 1
        print('Richtig! In einem Vakuum hoeren wir keinen Schall')
    else:
        print('Leider falsch... Richtig waere A: in einem Vakuum')
        
    answer=input('''Wie entsteht Schall?
    A: dadurch, dass Objekte schnell schwingen
    B: dadurch, dass Objekte sichtbar sind
    C: dadurch, dass Objekte eine Membran besitzen
    Antwort:''')
    if answer.lower()=='a':
        score += 1
        print('Richtig! Dadurch, dass Objekte schnell schwingen')
    else:
        print('Leider falsch... Richtig waere A: Dadurch, dass Objekte schnell schwingen')
    
    answer=input('''Im Vergleich zu einem leisen Ton hat ein lauter Ton eine...?
    A: groessere Frequenz
    B: kleine Frequenz
    C: groessere Amplitude
    D: kleinere Amplitude
    Antwort:''')
    if answer.lower()=='c':
        score += 1
        print('Richtig! Ein lauterer Ton hat eine groessere Amplitude')
    else:
        print('Leider falsch... Richtig waere C: groessere Amplitude')
        

print('Danke, dass du bei dem kleinen Quiz mitgemacht hast. Dein Score ist:',score)
percent=(score/total_questions)*100
print('Du hast insgesamt ',percent, 'Prozent richtig!')
