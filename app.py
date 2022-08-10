def decimal_to_binary(decimal):
    result = bin(decimal).replace("0b", "")
    return result


def exclusive_or(num1, num2):
    bin_list1 = list(decimal_to_binary(num1))
    bin_list2 = list(decimal_to_binary(num2))
    result = []
    i = 0
    while len(bin_list1) < len(bin_list2):
        bin_list1 = ["0"] + bin_list1
    while len(bin_list2) < len(bin_list1):
        bin_list2 = ["0"] + bin_list2

    while i < len(bin_list1):        
        if ((bin_list1[i]=="0") and (bin_list2[i]=="1")) or ((bin_list1[i]=="1") and (bin_list2[i]=="0")):
            i += 1
            result.append("1")
        else:
            i += 1
            result.append("0")

    return ("").join(result)


if __name__ == "__main__":
    bin_list = exclusive_or(3, 20)
    print(bin_list)