from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:\Kotlin\chromedriver.exe')

def imdb():

    driver.get('https://www.imdb.com/list/ls052283250/')

    names = driver.find_elements_by_css_selector('.lister-item-header a')
    masters_in = [driver.find_element_by_xpath(f'//*[@id="main"]/div/div[3]/div[3]/div[{i}]/div[2]/p[1]').text.split(' |')[0] for i in range(1, 101)]
    bios = [driver.find_element_by_xpath(f'//*[@id="main"]/div/div[3]/div[3]/div[{i}]/div[2]/p[2]').text for i in range(1, 101)]
    data = {
        'Artist': [i.text for i in names],
        'Profession | Best work': masters_in,
        'Bio': bios
    }
    df = pd.DataFrame(data, columns=['Artist', 'Profession | Best work', 'Bio'])
    df.to_csv('worldwide-tops.csv', index=True)


imdb()