from search_address import search_address


def main():
    zipcode = "9800012"

    address = search_address(zipcode)

    assert "宮城県仙台市青葉区錦町" == address


if __name__ == '__main__':
    main()
