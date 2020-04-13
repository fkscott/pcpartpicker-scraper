#test scraping a parts list with a downloaded pcpartpicker page
from bs4 import BeautifulSoup
from csv import writer

#open the test file and read its contents into a soup objet
with open("pcpartpicker-test-page.html","r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents,'html.parser')

#find the partlist div and store as plaintext
components = soup.find_all(class_="tr__product")

#create csv file and its headers
with open('parts.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Component','Selection','Price','Links']
    csv_writer.writerow(headers)

    for part in components:
        #component list
        component_types = part.find(class_='td__component').get_text().replace('\n','')

        #specific component names (selections)
        component_names = part.find(class_='td__name').get_text().replace('\n','')

        #the price of the components 
        #using two 'replace()' here because the whitespace got really messy in the get_text() section
        component_prices = part.find(class_='td__price').get_text().replace('\n','').replace(' ','')
        
        csv_writer.writerow([component_types,component_names,component_prices])


    
        


        




            



        




