import datetime, os, gzip, shutil, random, re, sys
startTime = datetime.datetime.now()

src = "../arabicCorpus/up0600AH/"
trg = "../arabicCorpus_translit/up0600AH/"

def translitArabic(text):
    """
    Transliterated Arabic letters using modified Buckwalter
    Necessary for R, since it does not work with Arabic letters
    """
    buckFile = './BuckwalterSimplified.txt'
    buckFile = open(buckFile, 'r', encoding='utf-8').readlines()
    for translitPair in buckFile:
        translit = re.search('(.)\t(.)', translitPair)
        arLetter = translit.group(1)
        latEquiv = translit.group(2)
        text = re.sub(arLetter, latEquiv, text)
    return(text)

def processFolder():
    lof = os.listdir(src)
    for f in lof:
        if f.endswith("-ara1"):
            with open(src+f, "r", encoding="utf8") as f1:
                text = f1.read()
                text = translitArabic(text)
                with open(trg+f+".translit", "w", encoding="utf8") as f9:
                    f9.write(text)
                print(f)
                #input()


processFolder()


print("Processing time: " + str(datetime.datetime.now()-startTime))
print("Tada!")
