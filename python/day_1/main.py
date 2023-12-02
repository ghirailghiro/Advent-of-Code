lines = []
with open('input.txt', 'r') as file:
    # Read the entire contents of the file into a string
    lines = [line.strip() for line in file]
    # Now, 'content' contains the contents of the file as a string

aux = 0
list_of_digits = ["one","two","three","four","five","six","seven","eight","nine"]
dict_of_digits = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

for i in lines:
    first_digit = None
    last_digit = ""
    for j in range(len(i)):
        if i[j].isdigit():
            if first_digit is None:
                first_digit = i[j]
            last_digit = i[j]
                
    aux += int(first_digit + last_digit)
     
print(f"First part of the problem : {aux}")

aux = 0
for i in lines:
    first_digit = None
    last_digit = ""
    for j in range(len(i)):
        if i[j].isdigit():
            if first_digit is None:
                first_digit = i[j]
            last_digit = i[j]
        else:
            check_digit_string = None
            for k in list_of_digits:
                if k == i[j:len(k)+j]:
                    check_digit_string = dict_of_digits[k]
            if check_digit_string is not None:
                if first_digit is None:
                    first_digit = check_digit_string
                last_digit = check_digit_string
                
    aux += int(first_digit + last_digit)
     
print(f"Second part of the problem : {aux}")
