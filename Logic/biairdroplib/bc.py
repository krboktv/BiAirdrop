"""by a37h@biairdrop, 11.11.17
that lib using users database in .txt file
and total pool for airdrop also in .txt creates
result file - waves_and_tokens.txt which has
a list of waves addresses and amount of tokens
we have to send them via our airdrop campaign

also 2 small functions for checking eth balance
using open API of etherscan.io
easly modifed for calculating balances of
eth accounts by having a local copy of full eth
node and some good C++ algorithm\node api
"""
import urllib.request
import re


""" Returns balance of (eth)*(10^18) """
def checkEthWalletBalance(address):
    response = urllib.request.urlopen("https://api.etherscan.io/api?"
                           "module=account&"
                           "action=balance&"
                           "address=" + address + "&tag=latest&"
                           "apikey=YourApiKeyToken").read()
    balance = int(re.split("\W+",str(response))[6])
    return balance


""" Prints out on screen request and balance """
def printEthWalletBalanace(address):
    balance = checkEthWalletBalance(address)
    print("Requested balance for: ", address)
    print("It's balance is      : ", balance, " or ", str(balance/(10**18)) + "eth")


""" Generating result file with eth accounts and their balances """
def parseAccsAndCalculateBalances(filein):
            # Parse the file users_db and get access to our users database via list called users_database
    users_database = [str(v).split() for v in open(filein)]
    balances_summary, waves_and_ethbalance = 0, []
            # Parse just user waves address and amount of his eth coins and save them in waves_and_ethbalance
    for account in users_database:
        balance = checkEthWalletBalance(account[1])
                # Keep the track of summary balances from all accs taking part in airdrop
        balances_summary += balance
        waves_and_ethbalance.append([account[2],balance])
            # We got summary of balances from all accs taking part in airdrop
            # Now we can get % of tokens which each one of them has to get
            # Keeping it in waves_and_percentage
    waves_and_percentage = [[pair[0],pair[1]/balances_summary] for pair in waves_and_ethbalance]
            # Now, getting amount of tokens each waves acc has to get
    giveaway_pool = int(open('pool_of_tockens_for_giveaway.txt').read())
    waves_and_tokens = [[pair[0],pair[1]*giveaway_pool] for pair in waves_and_percentage]
            # And save the result in waves_and_tokens.txt
    fileout = open('waves_and_tokens.txt', 'w')
    for pair in waves_and_tokens:
        outputstring = str(pair[0]) + " " + \
                       str(pair[1]) + "\n"
        fileout.write(outputstring)