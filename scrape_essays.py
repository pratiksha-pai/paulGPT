import requests
from bs4 import BeautifulSoup

def get_essay_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def get_essay_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

def main():
    index_url = 'http://www.paulgraham.com/articles.html'
    essay_links = get_essay_links(index_url)
    print("Number of essays: ", len(essay_links))
    with open('input.txt', 'w') as f:
        for link in essay_links:
            essay_url = 'http://www.paulgraham.com/' + link
            print(essay_url)
            essay_text = get_essay_text(essay_url)
            f.write('===========================' + essay_url + '===========================' + '\n')
            f.write(essay_text + '\n')
            f.write('===========================' + essay_url + '===========================' + '\n')

if __name__ == '__main__':
    main()
