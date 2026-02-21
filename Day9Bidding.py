def highest_bid(bid_dictionary):
    highest_price = 0
    winner = ""

    for bidder in bid_dictionary:
        price = bid_dictionary[bidder]
        if price > highest_price:
            highest_price = price
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_price}")


# TODO-1: Ask the user for input
end = False
bid = {}

while not end:
    name = input("Name of the user: ")
    price = int(input("The price of the bid $ "))

    bid[name] = price
    continuing = input("Do you want to continue? yes or no ").lower()

    if continuing == "no":
        end = True
        highest_bid(bid)