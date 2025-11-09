# Day-2
Calculate age based on birth date

####################################################################
from datetime import date

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day   = int(input("Enter your birth day (1-31): "))

today = date.today()
age = today.year - birth_year
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print(f"You are {age} years old.")

Explanation about the code
###################################################################

Explanation of the Code

This program begins by importing the date class from Python’s datetime library, which is used for working with dates. The input() function then prompts the user to enter their birth year, birth month (1–12) and birth day (1–31); each input is captured as text. The int() function converts that text into an integer value. The variables birth_year, birth_month, and birth_day store the user’s details: year, month and day of birth, respectively.

Next, the line today = date.today() obtains the current date (year, month, day) and assigns it to the variable today. We calculate a preliminary age by subtracting birth_year from the current year (age = today.year - birth_year). To determine if the user has already celebrated their birthday this year, the condition if (today.month, today.day) < (birth_month, birth_day): compares the tuple of (current month, current day) with the tuple of (birth month, birth day). If today’s date is earlier than the user’s birthday, the program decrements the age by one (age -= 1), since the anniversary has not yet occurred.

Finally, the program displays the result with print(f"You are {age} years old."). The f string notation allows the insertion of the variable age directly into the output message.

Note: A tuple is fundamentally a grouping of values.

Thank you for reviewing my code and this explanation.

###################################################################

O primeiro item está basicamente importando da biblioteca datetime a classe date, que serve justamente para trabalhar com datas.
A função input() aguarda que o usuário digite algo; esse algo aparece como texto (uma string).
A função int() converte esse texto para um número inteiro.
A variável birth_year receberá esse inteiro; a variável birth_month segue a mesma lógica, mas agora o inteiro representa o mês em vez do ano. Do mesmo modo a variável birth_day armazenará o dia (entre 1-31).
A linha today = date.today() faz com que a classe date pegue a data atual (ano, mês e dia) e armazene em today.
Em age = today.year - birth_year, pegamos o ano atual (today.year) e subtraímos o ano de nascimento (birth_year). Isso nos dá uma base de quantos anos se passaram entre o nascimento e o ano atual.
A condição if (today.month, today.day) < (birth_month, birth_day): verifica se o mês/dia de hoje ainda é anterior ao mês/dia de nascimento. (today.month, today.day) forma uma tupla com os valores de hoje, e (birth_month, birth_day) outra tupla com os valores de nascimento. Se a tupla de hoje for menor, significa que a pessoa ainda não fez aniversário neste ano.
Se for esse o caso, age -= 1 reduz a idade em 1, porque a base calculada contava o ano inteiro, mas o aniversário ainda não ocorreu.
Por fim, print(f"You are {age} years old.") imprime uma mensagem dizendo “You are X years old.” O prefixo f antes da string indica uma f-string, que permite inserir variáveis dentro das chaves {} na string. 

Obs: *Tupla é basicamente um agrupamento de valores*

Enfim: foi meio longo, mas achei uma forma de explicar meu código. Obrigado caso tenha lido até aqui ;)

