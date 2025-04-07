#add import
import question_a

def get_fahrenheit_table(row, col):
    r = 0
    while (r < row):
        c = 0
        while (c < col):
            num = 0
            while (num < 21):
                print(str(num).rjust(3, " "), end = " ")
                result = question_a.get_fahrenheit(num)
                print(str(result).rjust(3, " "), end = "\n")
                num += 1
                c += 1
        r += 1

def main():
    get_fahrenheit_table(1, 20)

main()