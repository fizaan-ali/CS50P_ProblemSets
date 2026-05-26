# first, last = input("What's your name? ").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]


# print(total(coins[0], coins[1], coins[2]), 'knuts')

# print(total(*coins), "knuts") 
# passing a list with * means to unpack we are still passing each item of list not a single item that is list 
# * means to unpack that list 
# in funct parameters total(*coins) == total(coin[0], coin[1], coin[2]), sequence is this just spreads positionally
# so list should contain items that's equal to number of parameters in function


coins = {
    'galleons' : 100,
    'sickles': 50,
    'knuts' : 25,
}

# print(total(galleons=100, sickles=50, knuts=25))
# we can also pass a dictionary to unpack if the keys are  the parameters of that  function then position won't affect
# but  here  with ** to unpack a dict

print(total(**coins))

# total(**coins)==total(coins['galleons'], coins['sickles], coins['knuts])
# but size should be equal in both cases