def interface():

    print('Blood Calculators')
    print('Make a choice')
    print('9 - Quit')
    choice = input('make a choice: ')
    print(choice)
    return choice
interface()


def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_vlue, HDL_character)

def hdl_input():
    hdl_value = int(input())
