from search_address import search_address


def main():
    # zipcode = "0294102"

    zipcode = input("郵便番号〈ハイフン無し〉は？ >> ")

    address = search_address(zipcode=zipcode)

    print(address)


if __name__ == '__main__':
    main()
