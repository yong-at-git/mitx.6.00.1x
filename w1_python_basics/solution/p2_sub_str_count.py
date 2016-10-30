class W1P2Solution:
    @staticmethod
    def count_sub_str_occurrence(s):
        occurrence = 0
        idx = 0
        sub_str = 'bob'

        len_s = len(s)
        len_sub_str = len(sub_str)

        while idx <= (len_s - len_sub_str):
            comparing_sub_str_end_idx = idx + len_sub_str
            tmp_sub_str = s[idx:comparing_sub_str_end_idx]
            if sub_str == tmp_sub_str:
                occurrence += 1
            idx += 1

        print("Number of times bob occurs is:", occurrence)
        return occurrence
