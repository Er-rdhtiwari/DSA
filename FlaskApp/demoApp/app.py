from imp import reload

from flask import Flask

app = Flask("__main__")

store = [
    {
        "name": "my Store",
        'item': [
            {
                "name": 'chai',
                "1": "item 1",
                "price": 99,
                'available':True,
                "stock":100
            }
        ]
    }
]

@app.get("/store")
def get_store():
    return {
        "store": store
    }
#
if __name__ == "__main__":
    app.run(debug=True, reload=True)