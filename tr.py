vowels = {
"a" : 'అ', #a
"aa" : 'ఆ', #aa
"i" :  'ఇ',#i
"ii" :  'ఈ',#ii
"u" :  'ఉ',#u
"uu" :  'ఊ',#uu
"ṛ"  : 'ఋ',#ṛ
"e" :  'ఎ',#e
"ee" :  'ఏ',#ee
"ay" : 'ఐ', #ay
"o" :  'ఒ',#o
"oo" :  'ఓ',#oo
"aw" :  'ఔ',#ow
}

cons = {
"ka": "క",
"kha": "ఖ",
"ga": "గ",
"gha":"ఘ",
"ŋ": "ఙ",
"ca":"చ",
"cha":"ఛ",
"ja":"జ",
"jha":"ఝ",
"ña":"ఙ",
"Ta":"ట",
"Tha":"ఠ",
"Da": "డ",
"Dha":"ఢ",
"Na":"ణ",
"ta":"త",
"tha":"థ",
"da":"ద",
"dha":"ధ",
"na":"న",
"pa":"ప",
"pha":"ఫ",
"ba":"బ",
"bha":"భ",
"ma":"మ",
"ya":"య",
"ra":'ర',
"la":"ల",
"wa":"వ",
"śa": "శ",
"Sa":"ష",
"sa":"స",
"ha":"హ",
"La":"ళ",
"kSa":"క్ష",
}

con_cut = {
"k": "క",
"kh": "ఖ",
"g": "గ",
"gh":"ఘ",
"ŋ": "ఙ",
"c":"చ",
"ch":"ఛ",
"j":"జ",
"jh":"ఝ",
"ñ":"ఙ",
"T":"ట",
"Th":"ఠ",
"D": "డ",
"Dh":"ఢ",
"N":"ణ",
"t":"త",
"th":"థ",
"d":"ద",
"dh":"ధ",
"n":"న",
"p":"ప",
"ph":"ఫ",
"b":"బ",
"bh":"భ",
"m":"మ",
"y":"య",
"r":'ర',
"l":"ల",
"w":"వ",
"ś": "శ",
"S":"ష",
"s":"స",
"h":"హ",
"L":"ళ",
"kS":"క్ష",
}

deps = {
"a" : 'ా', #a
"i" :  'ి',#i
"ii" :  'ీ',#ii
"u" :  'ు',#u
"uu" :  'ూ',#uu
"ṛ"  : 'ృ',#ṛ
"e" :  'ె',#e
"ee" :  'ే',#ee
"E": 'ె',
"EE": 'ే',
"ay" : 'ై', #ay
"o" :  'ొ',#o
"oo" :  'ో',#oo
"aw" :  'ౌ',#ow
}
#string = input("Enter text: ")
VV = 'aeiouṛ'
V = 'eiouEIOUṛ'
C = 'bcdghjklmnpqrstvwxyzśñDLMNST'

yw = "yw"
space_comma_fullstop = '!.,? '



def first_letter_vowel():
    global x,count,length
    if i+1 < length:
        if string[i+1] in VV:
            z = string[i]+string[i+1]
            x+=vowels.get(z)
            count = count+len(z)
        elif string[i+1] in yw and string[i] == 'a':
            z = string[i]+string[i+1]
            x+=vowels.get(z)
            count = count+len(z)
        else:
            z = string[i]
            x+=vowels.get(z)
            count = count+len(z)
    else:
        z = string[i]
        x+=vowels.get(z)
        count = count+len(z)

def conson_h():
    global x, count, length

def conson_a():
    global x, count, length
    if i+2 < length:
        if string[i+2] =='a':
            z = string[i]+string[i+1]
            x+=cons.get(z)+deps.get(string[i+2])
            count = count+len(z)+1
        else:
            z = string[i]+string[i+1]
            x+=cons.get(z)
            count = count+len(z)
    else:
        z = string[i]+string[i+1]
        x+=cons.get(z)
        count = count+len(z)

def conson_no_a():
    global x, count, length
    if i+2 < length:
        if string[i+2] in V:
            z = string[i]
            y = string[i+1]+string[i+2]
            #print(y)
            x+=con_cut.get(z)+deps.get(string[i+1]+string[i+2])
            count = count+len(z)+2
        else:
            z = string[i]
            x+=con_cut.get(z)+deps.get(string[i+1])
            count = count+len(z)+1
    else:
        z = string[i]
        x+=con_cut.get(z)+deps.get(string[i+1])
        count = count+len(z)+1

def concon():
    global x, count, length
    if string[i+2] == 'a':
        if i+3 < length:
            if string[i+3] == 'a':
                z = string[i]
                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+3])
                count = count +len(z)+3
            else:
                z = string[i]
                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])
                count = count +len(z)+2
        else:
            z = string[i]
            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])
            count = count +len(z)+2
    elif string[i+2] in V:
        if i+3 < length:
            if string[i+3] in V:
                z = string[i]
                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2]+string[i+3])
                count = count +len(z)+3
            else:
                z = string[i]
                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2])
                count = count +len(z)+2
        else:
            z = string[i]
            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2])
            count = count +len(z)+2

data = open(r'G:\My Drive\Project\data.txt', encoding="utf8")
data = data.read().split('\n')
num = 1
for ven in data:
    x = ""
    string = ven
    length = len(string)
    count = 0

    while count<length:
        z =''
        i = count
        if string[i] in VV:
            first_letter_vowel()
        elif string[i] in C:
            if count == length-1:
                if string[i] == 'm' or string[i] == 'M':
                    z = string[i]
                    x+="\u0c02"
                    count = count+1
                    #print(1)
                else:
                    z = string[i]
                    x+=con_cut.get(z)+"\u0c4d"
                    count = count+1
            elif string[i+1] in space_comma_fullstop:
                if string[i] == 'm' or string[i] == 'M':
                    z = string[i]
                    x+="\u0c02"
                    count = count+1
                    #print(2)
                else:
                    z = string[i]
                    x+=con_cut.get(z)+"\u0c4d"
                    count = count+1
            elif string[i] == 'n' or string[i] == 'N':
                if string[i+1] == 'n' or string[i+1] == 'N':
                    concon()
                elif string[i+1] in C:
                    z = string[i]
                    x+="\u0c02"
                    count = count+1
                    #print(3)
                else:
                    if string[i+1] == 'a':
                        conson_a()
                    elif string[i+1] in V:
                        conson_no_a()
                    elif string[i+1] in C:
                        concon()
                    else:
                        print("Error")
                        break
            elif string[i] == 'm':
                if i+1 < length:
                    if string[i+1] in space_comma_fullstop:
                        z = string[i]
                        x+="\u0c02"
                        count = count+1
                        #print(4)
                    else:
                        if string[i+1] == 'a':
                            if i+2<length-1:
                                if string[i+2] in yw:
                                    z = string[i]
                                    x+=con_cut.get(z)+deps.get(string[i+1]+string[i+2])
                                    count = count+len(z)+2
                                else:
                                    conson_a()
                            else:
                                conson_a()
                        elif string[i+1] in V:
                            conson_no_a()
                        elif string[i+1] in C:
                            concon()
                else:
                    if count == length-1:
                        z = string[i]
                        x+="\u0c02"
                        count = count+1
                        #print(5)

            #if i+1 <= length:
            elif string[i+1] == 'h':
                if string[i+2] == 'a':
                    if i+3<length:
                        if string[i+3] == 'a':
                            z = string[i]+string[i+1]+string[i+2]
                            x+=cons.get(z)+deps.get(string[i+3])
                            count = count+len(z)+1
                        elif string[i+3] in yw:
                            if i+4<length:
                                if string[i+4] == 'a':
                                    z = string[i]+string[i+1]
                                    x+=con_cut.get(z)
                                    count = count+len(z)+1
                                elif string[i+4] in V:
                                    z = string[i]+string[i+1]
                                    x+=con_cut.get(z)
                                    count = count+len(z)+1
                                else:
                                    z = string[i]+string[i+1]
                                    x+=con_cut.get(z)+deps.get(string[i+2]+string[i+3])
                                    count = count+len(z)+2
                            else:
                                z = string[i]+string[i+1]
                                x+=con_cut.get(z)+deps.get(string[i+2]+string[i+3])
                                count = count+len(z)+2

                        else:
                            z = string[i]+string[i+1]+string[i+2]
                            x+=cons.get(z)
                            count = count+len(z)
                    else:
                        z = string[i]+string[i+1]+string[i+2]
                        x+=cons.get(z)
                        count = count+len(z)
                elif string[i+2] in V:
                    if i+3<length:
                        if string[i+3] in V:
                            z = string[i]+string[i+1]
                            x+=con_cut.get(z)+deps.get(string[i+2]+string[i+3])
                            count = count+len(z)+2
                        else:
                            z = string[i]+string[i+1]
                            x+=con_cut.get(z)+deps.get(string[i+2])
                            count = count+len(z)+1
                    else:
                        z = string[i]+string[i+1]
                        x+=con_cut.get(z)+deps.get(string[i+2])
                        count = count+len(z)+1
                elif string[i+2] in C:
                    if string[i+3] == 'a':
                        z = string[i]+string[i+1]
                        x+=con_cut.get(z)+"\u0c4d"+cons.get(string[i+2]+string[i+3])
                        count = count+len(z)+2
                    elif string[i+3] in V:
                        z = string[i]+string[i+1]
                        x+=con_cut.get(z)+"\u0c4d"+cons.get(string[i+2]+string[i+3])
                        count = count+len(z)+2
                    else:
                        print("Error")
                        break

            elif string[i+1] == 'a':
                if i+2 < length:
                    if string[i+2] =='a':
                        z = string[i]+string[i+1]
                        x+=cons.get(z)+deps.get(string[i+2])
                        count = count+len(z)+1
                    elif string[i+2] in yw:
                        if i+3<length:
                            if string[i+3] == 'a':
                                z = string[i]+string[i+1]
                                x+=cons.get(z)
                                count = count+len(z)
                            elif string[i+2] in V:
                                z = string[i]+string[i+1]
                                x+=cons.get(z)
                                count = count+len(z)
                            else:
                                z = string[i]
                                x+=con_cut.get(z)+deps.get(string[i+1]+string[i+2])
                                count = count+len(z)+2
                        else:
                            z = string[i]
                            x+=con_cut.get(z)+deps.get(string[i+1]+string[i+2])
                            count = count+len(z)+2
                    elif string[i+2] == 'm' and i+2 <length-1 and string[i+3] != 'y' and string[i+3] != 'r' and string[i+3] != 'a' and string[i+3] != 'e' and string[i+3] != 'i' and string[i+3] != 'o' and string[i+3] != 'u' and string[i+3] != 'E':
                        z = string[i]
                        x+=con_cut.get(z)+'\u0c02'
                        count = count+3

                    else:
                        z = string[i]+string[i+1]
                        x+=cons.get(z)
                        count = count+len(z)
                else:
                    z = string[i]+string[i+1]
                    x+=cons.get(z)
                    count = count+len(z)
            elif string[i+1] in V:
                if i+2 < length:
                    if string[i+2] in V:
                        z = string[i]
                        y = string[i+1]+string[i+2]
                        x+=con_cut.get(z)+deps.get(string[i+1]+string[i+2])
                        count = count+len(z)+2
                    elif string[i+2] == 'm' and i+2 <length-1 and string[i+3] != 'y' and string[i+3] != 'r' and string[i+3] != 'a' and string[i+3] != 'e' and string[i+3] != 'i' and string[i+3] != 'o' and string[i+3] != 'u' and string[i+3] != 'E':
                        z = string[i]
                        x+=con_cut.get(z)+deps.get(string[i+1])+'\u0c02'
                        count = count+3
                    else:
                        z = string[i]
                        x+=con_cut.get(z)+deps.get(string[i+1])
                        count = count+len(z)+1
                else:
                    z = string[i]
                    x+=con_cut.get(z)+deps.get(string[i+1])
                    count = count+len(z)+1

            elif string[i+1] in C: # ్ #for Votthulu
                if string[i+2] == 'a':
                    if i+3 < length:
                        if string[i+3] == 'a':
                            z = string[i]
                            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+3])
                            count = count +len(z)+3
                        else:
                            z = string[i]
                            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])
                            count = count +len(z)+2
                        
                    else:
                        z = string[i]
                        x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])
                        count = count +len(z)+2

                #ddha ddhaa     
                elif string[i+2] == 'h':
                    if string[i+3] == 'a':
                        if i+4 < length:
                            if string[i+4] == 'a':
                                z = string[i]
                                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])+deps.get(string[i+4])
                                count = count +len(z)+4
                            else:
                                z = string[i]
                                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])
                                count = count +len(z)+3
                        else:
                            z = string[i]
                            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])+deps.get(string[i+3])
                            count = count +len(z)+3
                    else:
                        if string[i+3] in V:
                            if i+4 < length:
                                if string[i+4] in V:
                                    z = string[i]
                                    x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])+deps.get(string[i+3]+string[i+4])
                                    count = count +len(z)+4
                                else:
                                    z = string[i]
                                    x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])+deps.get(string[i+3])
                                    count = count +len(z)+3                            
                            else:
                                z = string[i]
                                x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1]+string[i+2])+deps.get(string[i+3])
                                count = count +len(z)+3
                elif string[i+2] in V:
                    if i+3 < length:
                        if string[i+3] in V:
                            z = string[i]
                            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2]+string[i+3])
                            count = count +len(z)+3
                        else:
                            z = string[i]
                            x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2])
                            count = count +len(z)+2
                    else:
                        z = string[i]
                        x+=con_cut[z]+"\u0c4d"+con_cut.get(string[i+1])+deps.get(string[i+2])
                        count = count +len(z)+2

            elif string[i+1] == 'ṛ':
                z = string[i]
                x+=con_cut.get(z)+'\u0c43'
                count = count+2
            
                        
        else:
            x+=string[i]
            count = count + 1

    print(num, x)
    num+=1