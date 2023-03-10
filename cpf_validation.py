"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

def cpf_validation(cpf):

    """
    This function may check a CPF by going through a simple algohritm, which is described with an example above (in Portuguese).

    The cpf argument should be a 9 digits STRING. This function may not accept any value of other type or/and length.
    """

    # First going to calculate the first verification digit.

    counter_first_digit = 10
    total_first_digit = 0
    for number in cpf[0:-2]:
        total_first_digit += int(number)*counter_first_digit
        counter_first_digit -= 1

    total_first_digit *= 10

    total_first_digit %= 11

    # Finished calculating now it's going to attribute the value to the 'first_digit' variable.

    if total_first_digit > 9:
        first_digit = 0
    else:
        first_digit = total_first_digit


    # Now I'm going to calculate the second verification digit

    counter_second_digit = 11
    total_second_digit = 0
    for number in cpf[0:-1]:
        total_second_digit += int(number*counter_second_digit)
        counter_second_digit -= 1
    

    print(total_second_digit)
    total_second_digit *= 10
    print(total_second_digit)
    seconddigit = total_second_digit % 11
    print(total_second_digit)

    # Finished calculating now it's going to attribute the value to the 'second_digit' variable.


    if total_second_digit > 9:
        second_digit = 0
    else:
        second_digit = total_second_digit

    # Prints a message saying "The verification digits for the given CPF are {first_digit} and {second_digit}, in Portuguese."

    print(f"Os dígitos verificadores para o CPF informado são {first_digit} e {second_digit}.")


cpf_validation('05244450018')

# This module was made exclusively for me to exercise my skills as a Python begginer. I didn't put any work after finishing it simply.
