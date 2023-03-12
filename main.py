# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def chatbot_ui():
    messages = ['Hello', 'How are you?', 'Goodbye']
    return render_template('chat.html', messages=messages)


@app.route('/chat', methods=['POST'])
def process_chat():
    # get the user input from the request body
    message = request.json['message']
    print(message)
    # do some processing with the user input (e.g. pass it to a bot)
    chat_response = process_message(message)

    # return the bot's response as a JSON object
    return jsonify({'chat_response': chat_response})


def process_message(message):
    # do some processing with the user input (e.g. pass it to a bot)
    # return the bot's response
    return message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
