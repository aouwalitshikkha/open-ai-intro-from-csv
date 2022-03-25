import openai
import csv
openai.api_key = 'Your-API-Key'


def processKeyword(mykeyord):
        query ='Write an introductory processional article why you should read our review before buying ' + mykeyord
        return str(query)

def GrabIntro(stext):
        response = openai.Completion.create(
          engine="text-davinci-002",
          prompt=stext,
          temperature=0.7,
          max_tokens=200,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        return response['choices'][0]['text']


with open("keywordintro.csv","w",newline='') as fw:
        fieldnames=['keyword','intro']
        writer = csv.DictWriter(fw,delimiter=',',fieldnames=fieldnames)
        writer.writeheader()
        
        with open('keywords.csv', 'r') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                # print(row['Keyword'])
                StrKeyword = processKeyword(row['Keyword'])
                OutputText = GrabIntro(StrKeyword)
                # print(OutputText)
                to_write={'keyword':row['Keyword']}
                to_write['intro'] = str(OutputText)
                writer.writerow(to_write)

print("Done")
