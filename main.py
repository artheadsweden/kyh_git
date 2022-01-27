import requests


def main():
    result = requests.get('https://svt.se')
    title_part1 = result.text.split('<title data-react-helmet="true">')[1]
    title = title_part1.split('</title>')[0]
    print('title:', title)


if __name__ == '__main__':
    main()
