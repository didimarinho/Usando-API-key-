
import requests
import pandas as pd


url = 'https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=dqD4uiFKPxaZmW59cXzuNnGPftC5qtsN'

response = requests.get(url)

dframe = pd.DataFrame(response)



#? Salvando arquivo txt
if response.status_code == 200:
    with open('urltext.txt', 'w') as filetxt:
        filetxt.write(response.text)
else:
    print('A resposta da url não foi bem sucedida. Código status: ', response.status_code)
    



# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame.from_dict(data['rates'], orient='index', columns=['exchange_rate'])
    df.index.name = 'currency'
    df.reset_index(inplace=True)
    
    #* Salvando o data frame em um arquivo txt
    df.to_csv('dataf.txt', sep='\t', index=False)
else:
    print("A resposta da URL não foi bem-sucedida. Código de status:", response.status_code)

