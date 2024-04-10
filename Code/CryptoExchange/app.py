from flask import Flask, request, jsonify
import hashlib
import time
import json

app = Flask(__name__)

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = self.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.data)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        block_string = json.dumps({"index": index, "previous_hash": previous_hash, "timestamp": timestamp, "data": data}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order):
        print('soso')

@app.route('/')
def home():
    return "Welcome to the Crypto Exchange Platform!"

users = {}

@app.route('/register', methods=['POST'])
def register():
    print('Register')
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'Username already exists'}), 400
    users[username] = password
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

wallets = {}

@app.route('/wallet/create', methods=['POST'])
def create_wallet():
    data = request.json
    username = data.get('username')
    if username not in wallets:
        wallets[username] = 100  # Starting balance, for example purposes
        return jsonify({'message': 'Wallet created successfully', 'balance': wallets[username]}), 201
    return jsonify({'message': 'Wallet already exists'}), 400

@app.route('/wallet/<username>', methods=['GET'])
def get_wallet(username):
    if username in wallets:
        return jsonify({'balance': wallets[username]}), 200
    return jsonify({'message': 'Wallet not found'}), 404

@app.route('/trade', methods=['POST'])
def trade():
    data = request.json
    buyer = data.get('buyer')
    seller = data.get('seller')
    amount = data.get('amount')
    if buyer in wallets and seller in wallets and wallets[seller] >= amount:
        wallets[buyer] += amount
        wallets[seller] -= amount
        return jsonify({'message': 'Trade successful'}), 200
    return jsonify({'message': 'Trade failed'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
