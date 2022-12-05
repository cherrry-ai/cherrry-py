from cherrry import CherrryClient

client = CherrryClient("your_api_key")

def createTableTest():
    [success, error] = client.create_table("blogs-4")
    print("create table::", success, error)

def insertTest():

    [data, error] = client.table("blogs-3").insert({
        "text": {
            "title": "Grey's Anatomy"
        },
        "image": {
            "banner": "https://i.imgur.com/rCi9ooQ.jpeg"
        },
        "metadata": {
            "author_name": "Kermit The Frog",
            "author_email": "frog@dog.com"
        }
    })

    print(data, error)

    [data, error] = client.table("blogs-3").insert({
        "text": {
            "title": "Octopus Cherry Pie"
        },
        "image": {
            "banner": "https://i.imgur.com/lFC8p0L.jpeg"
        },
        "data": {
            "author_name": "Davy Jones",
            "author_email": "octo@pus.com"
        }
    })

    print(data, error)

def searchTest():
    [data, error] = client.table("blogs-3").search({ "prompt": "muppet doctor", "size": 1, "search_type": "image" })
    print(data, error)

def docTest():
    [data, error] = client.table("blogs-3").doc("31501682")
    print(data, error)

def deleteTest():
    [ success, error ] = client.table("blogs-3").delete("31501682")
    print(success, error)

def main():
    # createTableTest()
    # insertTest()
    searchTest()
    # docTest()
    # deleteTest()


if __name__ == "__main__":
    main()