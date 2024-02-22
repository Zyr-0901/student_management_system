from jsonpath import jsonpath

JSON_DATA = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}


def test_demo():
    # print(f"获取书籍下的所有作者{jsonpath(JSON_DATA, '$.store..author')}")
    # print(f"获取所有作者{jsonpath(JSON_DATA, '$..author')}")
    # print(f"获取store下的所有内容{jsonpath(JSON_DATA, '$.store')}")
    # print(f"获取所有价格{jsonpath(JSON_DATA, '$..price')}")
    # print(f"获取第三本书{jsonpath(JSON_DATA, '$..book[2]')}")
    # print(f"获取包含isbn的书籍 {jsonpath(JSON_DATA, '$..book[?(@.isbn)]')}")
    # print(f"获取所有价格小于 10 的书 {jsonpath(JSON_DATA, '$..book[?(@.price < 10)]')}")
    print(f"获取所有书籍的数量 {len([item for i in jsonpath(JSON_DATA, '$..book') for item in i])}")
