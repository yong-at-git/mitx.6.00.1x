class W1P1Solution:
    @staticmethod
    def count_vowel(s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        idx = 0
        vowels_num = 0

        len_s = len(s)

        while idx < len_s:
            if s[idx] in vowels:
                vowels_num += 1
            idx += 1

        print("Number of vowels:", vowels_num)
        return vowels_num
