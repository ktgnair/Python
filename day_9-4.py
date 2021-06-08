# Blind Auction Program


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
flag = True

while flag:
    user_name = input("What is your name?  ")
    bid_price = int(input("What is your bid?  Rs"))
    bids[user_name] = bid_price
    next_bid = input("If any other bids are there then type 'Yes' else type 'No': ").lower()
    # To clear the screen after 1 bid so that the next can put the bid(just a hack without using the system calls)
    # clear = "\n" * 100
    # print(clear)
    if next_bid == "no":
        flag = False
        highest_bid = 0
        for bid in bids:
            if bids[bid] > highest_bid:
                highest_bid = bids[bid]
                winner_bid = bid
        print(f"The Winner is {winner_bid} with a bid of {highest_bid} ")