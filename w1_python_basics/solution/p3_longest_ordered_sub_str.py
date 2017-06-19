class W1P3Solution:
    empty_str = ''

    @staticmethod
    def get_longest_ordered_sub_str(s):
        longest = W1P3Solution.empty_str
        s_len = len(s)
        current_len = len(s)

        # applying guess-and-check strategy
        # starting from the longest string and decrease it gradually
        while current_len > 0:
            start_idx = 0
            end_idx = start_idx + current_len
            while end_idx <= s_len:
                sub_str = s[start_idx:end_idx]
                is_ordered = True
                # check if the substring is in order
                for i in range(len(sub_str) - 1):
                    if sub_str[i] > sub_str[i + 1]:
                        is_ordered = False
                        break

                if is_ordered:
                    longest = sub_str
                    break

                start_idx += 1
                end_idx = start_idx + current_len

            if longest != W1P3Solution.empty_str:
                break

            current_len -= 1

        print('Longest substring in alphabetical order is:', longest)

        return longest
