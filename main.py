import numpy as np

class Crypt:
    word = None
    arr = None
    encarr = None

    def __init__(self, word, arr): # Конструктор
        self.word = word
        self.arr = arr
        self.encarr = []

    def FindSymbolCoord(self, letter): # Вспомогательная функция поиска коорд
        for i in range(0, len(self.arr)): #                              символа
            for j in range(0, len(self.arr[i])):
                if a[i][j] == letter:
                    return (i, j)

    def Encrypt(self): # Функция шифровки
        k = 0
        for i in range(0, len(word)):
            res = self.FindSymbolCoord(self.word[k])
            (self.encarr).append((res))
            k += 1

    def Decrypt(self): # Функция расшифровки
        decrarr = []
        for i in range(len(self.encarr)):
            temp = self.arr[self.encarr[i][0]][self.encarr[i][1]]
            decrarr.append(temp)
        return decrarr

    def Print(self):
        print("Слово: " ,self.word)
        print("Массив кодировки:\n", self.arr)
        print("Зашифрованное слово:\n", self.encarr)

a = np.array([["а", "б", "в", "г", "д", "е", "ё", "ж", "з"],
              ["и", "й", "к", "л", "м", "н", "о", "п", "р"],
              ["с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ"],
              ["ъ", "ы", "ь", "э", "ю", "я", "А", "Б", "В"],
              ["Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К"],
              ["Л", "М", "Н", "О", "П", "Р", "С", "Т", "У"],
              ["Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь"],
              ["Э", "Ю", "Я", " ", ".", ":", "!", "?", ","]])
word = "Криптография"

crypt1 = Crypt(word, a)
crypt1.Encrypt()
decryptedword = crypt1.Decrypt()
crypt1.Print()
print("Расшифрованное слово:\n", decryptedword)