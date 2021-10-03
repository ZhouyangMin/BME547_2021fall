def interface():

    print('Blood Calculators')
    keep_running = True
    while keep_running:
        print('\nMake a choice')
        print('1 - HDL_Analysis')
        print('2 - LDL_Analysis')
        print('3 - Total cholesterol Analysis')
        print('9 - Quit')


    choice = input('make a choice: ')
    print(choice)
    return choice
interface()

#***********HDL***********
def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_vlue, HDL_character)

def hdl_input():
    hdl_value = int(input('Enter HDL Value'))
    return hdl_value
    
def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return 'Normal'
    elif 40 <= HDL_value < 60:
        return 'Borderline Low'
    else:
        return 'Low'

def hdl_output(HDL_value, HDL_answer):
    print('The HDL value of {} is condisered{}'.format())
    return


#***********LDL**************
def total_output(ldl_input):
    if ldl_input < 130:
        return "Normal"
    elif 130 <= ldl_input < 160:
        return "Borderline high"
    elif 160 <= ldl_input < 190:
        return "High"
    else:
        return "Very High"
    
    return


if __name__=='__main__':
    interface()

def check_input(in_string):
    if len(in_string)<3:
        return False
    else:
        return True



