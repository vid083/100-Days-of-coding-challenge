from blind_action_logo import logo
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''

    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid} dollars")

while not bidding_finished:
    name = input("Enter bidder name: ")
    price = int(input("Enter bidding price: "))

    bids[name] = price

    should_continue = input("Are there any other bidder ? Yes or No: ")

    if should_continue == 'No':
        find_highest_bidder(bids)
        bidding_finished = True
    





