# this file will be entry point of the project
from api.pixabay import get_pixabay_api_data

def main():
    query = input("Please enter your desired photo keyword: ")
    category = input("Please enter your category: ")
    if query != '' and category != '':
        get_pixabay_api_data(query=query,category=category)
    else:
        print("Please enter a valid keyword / catrgory !")


if __name__ == "__main__":
    main()