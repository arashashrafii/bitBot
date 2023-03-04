import requests
import json
import time

url = 'https://freebitco.in/ajax_mine.php'
cookie = {'Cookie': 'your_cookie_value_here'}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Set the parameters for the game
rounds = 1000
base_bet = 0.00000010
multiplier = 2
max_consecutive_losses = 10

# Define the bet and calculate the amount to wager
def define_bet(consecutive_losses):
    return base_bet * (multiplier ** consecutive_losses)

def calculate_wager(consecutive_losses):
    total_bet = 0
    for i in range(consecutive_losses):
        total_bet += define_bet(i)
    return total_bet

# Start the game
consecutive_losses = 0
total_wager = 0
total_profit = 0
for i in range(rounds):
    # Define the headers for the request
    headers = {
        'User-Agent': user_agent,
        'Referer': 'https://freebitco.in/',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    # Calculate the amount to wager
    wager = calculate_wager(consecutive_losses)
    total_wager += wager
    
    # Place the bet
    data = {
        'csrf_token': '',
        'bet': wager,
        'type': 'hi',
        'coin': 'btc'
    }
    response = requests.post(url, headers=headers, cookies=cookie, data=data)
    result = json.loads(response.text)
    
    # Handle the result
    if result['status'] == 'success':
        if result['winning_result']['is_win'] == 1:
            profit = wager * (multiplier - 1)
            consecutive_losses = 0
            total_profit += profit
        else:
            consecutive_losses += 1
            if consecutive_losses > max_consecutive_losses:
                print('Max consecutive losses reached. Exiting...')
                break
    else:
        print('Error placing bet. Exiting...')
        break
    
    # Sleep for a few seconds to avoid triggering anti-bot measures
    time.sleep(3)
    
    # Print the result of the round
    print('Round', i+1, '- Bet:', wager, '- Profit:', profit)
    
# Print the total result
print('Total Wager:', total_wager, '- Total Profit:', total_profit)
import requests
import json
import time

url = 'https://freebitco.in/ajax_mine.php'
cookie = {'Cookie': 'your_cookie_value_here'}
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# Set the parameters for the game
rounds = 1000
base_bet = 0.00000010
multiplier = 2
max_consecutive_losses = 10

# Define the bet and calculate the amount to wager
def define_bet(consecutive_losses):
    return base_bet * (multiplier ** consecutive_losses)

def calculate_wager(consecutive_losses):
    total_bet = 0
    for i in range(consecutive_losses):
        total_bet += define_bet(i)
    return total_bet

# Start the game
consecutive_losses = 0
total_wager = 0
total_profit = 0
for i in range(rounds):
    # Define the headers for the request
    headers = {
        'User-Agent': user_agent,
        'Referer': 'https://freebitco.in/',
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    # Calculate the amount to wager
    wager = calculate_wager(consecutive_losses)
    total_wager += wager
    
    # Place the bet
    data = {
        'csrf_token': '',
        'bet': wager,
        'type': 'hi',
        'coin': 'btc'
    }
    response = requests.post(url, headers=headers, cookies=cookie, data=data)
    result = json.loads(response.text)
    
    # Handle the result
    if result['status'] == 'success':
        if result['winning_result']['is_win'] == 1:
            profit = wager * (multiplier - 1)
            consecutive_losses = 0
            total_profit += profit
        else:
            consecutive_losses += 1
            if consecutive_losses > max_consecutive_losses:
                print('Max consecutive losses reached. Exiting...')
                break
    else:
        print('Error placing bet. Exiting...')
        break
    
    # Sleep for a few seconds to avoid triggering anti-bot measures
    time.sleep(3)
    
    # Print the result of the round
    print('Round', i+1, '- Bet:', wager, '- Profit:', profit)
    
# Print the total result
print('Total Wager:', total_wager, '- Total Profit:', total_profit)
