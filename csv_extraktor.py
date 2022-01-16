import json
import csv


raw_data_list_and_label = {'raw/merged_bild_data.json': "bild",
           "raw/merged_bildnews_data.json": "bildNews",
           'raw/merged_glasauge_data.json': "glasauge",
           'raw/merged_postillon_data.json': "postillon",
           'raw/merged_spiegel_data.json': "spiegel",
           'raw/merged_spiegelonline_data.json': "spiegelonline",
           'raw/merged_sz_data.json': "sueddeutscheZ",
           'raw/merged_titanic_data.json': "titanic",
           'raw/merged_welt_data.json': "welt",
           'raw/merged_zeitonline_data.json': "zeitonline"}



def feedliste(rawdatalist):
    for key, value in raw_data_list_and_label.items():
        with open(key) as acces_json:
            read_content = json.load(acces_json)

            saved_csv_data = open('csv_data_text&label.csv', 'a', encoding='utf-8')
            length = len(read_content)
            x = 0
        with saved_csv_data:
            writer = csv.writer(saved_csv_data)
            header = ['text', 'label']
            writer.writerow(header)

            while x <= length:
                for key in range(length):
                    a = read_content[key]
                    id = a['data'][x]['id']
                    text = str(a['data'][x]['text'])

                    # Bereinigung von Leerzeichen
                    text=text.replace("\n", " ").replace("\t", " ")

                    size = len(text)

                    # Bereinigung von dem Link am Ende
                    return_csv = writer.writerow([text[:size - 23]] + [value])
                x = x + 1
    else:
        pass

    return (return_csv)


feedliste(raw_data_list_and_label)

