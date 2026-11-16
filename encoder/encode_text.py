from pathlib import Path
import unicodedata

cyril_symbols = ["п", "у", "з", "д", "л", "ж", "и", "ь", "й", "я", "б", "ъ", "ш", "ы", "ю", "г", "щ", "э", "ф", "ц", "н", "м", "т", "х", "р", "ч", "к", "е", "о", "с", "а", "в"]
latin_symbols = ["ê", "ì", "ä", "â", "é", "ã", "ç", "ù", "è", "ü", "à", "õ", "ó", "ö", "û", "á", "ô", "ú", "í", "ñ", "h", "m", "t", "x", "p", "4", "k", "e", "o", "c", "a", "b"]

for file in Path('files_for_encode').iterdir():
    encoded_text = []
    
    with open(file, 'r', encoding='utf-8') as f:
        
        for line in f:
            encoded_line = line.strip()
            encoded_line = unicodedata.normalize('NFC', encoded_line)
            
            for symbol in range(len(latin_symbols)):
                encoded_line = encoded_line.replace(cyril_symbols[symbol], latin_symbols[symbol])
                encoded_line = encoded_line.replace(cyril_symbols[symbol].upper(), latin_symbols[symbol].upper())
            
            encoded_text.append(encoded_line+"\n")
    
        with open('result/'+file.name, 'w', encoding='utf-8') as f:
            f.writelines(encoded_text)

input("The encoding was successful!")