def longest_common_substring_length(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp_table = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    max_length = 0
    end_index = 0

    for row in range(1, len1 + 1):
        for col in range(1, len2 + 1):
            if str1[row - 1] == str2[col - 1]:
                dp_table[row][col] = dp_table[row - 1][col - 1] + 1
                if dp_table[row][col] > max_length:
                    max_length = dp_table[row][col]
                    end_index = row
            else:
                dp_table[row][col] = 0
    return max_length, end_index, dp_table


def extract_longest_common_substring(str1, end_index, max_length):
    return str1[end_index - max_length:end_index]


if __name__ == "__main__":
    test_cases = [
        ("temple", "simple"),
        ("python", "typhoon"),
        ("abcxyzdef", "xyzabcghi"),
        ("hello", "world"),
        ("", "anything"),
        ("code", ""),
        ("aaaa", "aaa"),
        ("dynamic", "algorithm"),
        ("common", "commonality"),
        ("ABCD", "BCDE"),
    ]

    for str1, str2 in test_cases:
        max_length, end_index, dp_table = longest_common_substring_length(
            str1, str2)
        common_substring = extract_longest_common_substring(
            str1, end_index, max_length) if max_length > 0 else ""
        print(f"Input String 1: '{str1}', String 2: '{str2}'")
        print(f"Longest Common Substring: '{common_substring}'")
        print(f"Length: {max_length}")
        print("DP Table:")
        for row in dp_table:
            print(row)
        print("-" * 50)
