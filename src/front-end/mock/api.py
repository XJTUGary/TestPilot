from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/case-list', methods=['GET'])
def get_test_data():
    data = [
        {
            "id": "1",
            "task_id": "abc",
            "test_name": "test 1",
            "script": "browser = p.chromium.launch()"
        },
        {
            "id": "2",
            "task_id": "abc",
            "test_name": "test 2",
            "script": """
            page = browser.new_page()
            page.goto('https://www.baidu.com')
            print(page.title())
            browser.close()"""
        }
    ]

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
