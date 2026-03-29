def input_string():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    return string1, string2
def uncommonConcat(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    uncommon_s1 = set1 - set2
    uncommon_s2 = set2 - set1
    result = ''.join(uncommon_s1.union(uncommon_s2))
    return result
string1, string2 = input_string()
result = uncommonConcat(string1, string2)
print("Output: ", result)
