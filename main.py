import requests


def main():
    result = requests.get('https://svt.se')
    print(result.text)

    
if __name__ == '__main__':
    main()
