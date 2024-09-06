from Data import Data

calendario = Data(1, 12, 2024)

print('\n\t\t\t -- Data -- ')

if calendario.checarData() == False:
    print('Data Inválida!')
else:
    print(calendario)