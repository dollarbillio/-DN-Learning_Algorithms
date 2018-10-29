----------------------------------------------
# Create all trade_combo by BitWise Algorithm
----------------------------------------------
def trade_combo(list_1):
    '''Return a combo of possible buy and sell between currency
       the trade combo return an iterable by using yield
    '''
    N = len(list_1)
    currency_dict = {}
    for i in range(N):
        # Associate a number index to a currency
        currency_dict[i] = list_1[i] 
	
    for i in range(2**N):
        Combo = []
        for j in range(N):
            # Each index of number corresponds to a currency position
            # Shift
            if (i // 2**j) % 2 == 1:
                Combo.append("- " + currency_dict[j])
            else:
                Combo.append("+ " + currency_dict[j])

        yield Combo

all_combo = []
for i in trade_combo(['EUR', 'USD', 'JPY', 'GBP', 'AUD', 'CAD']):
    all_combo.append(i)

---------------------------------------------------
# Modify so that currency possibilities are chosen
---------------------------------------------------
modified = []
for i in all_combo:
    dict_sign = {}
    '''Get the maximum sign in currency combo situation'''
    for j in i:
        dict_sign[j[0]] = dict_sign.get(j[0], 0) + 1
	
    # Find the market leading currency
    min_value = min(list(dict_sign.values()))
    # Find the currencies with leading power 
    if min_value in [1,2]:
        for keys, values in dict_sign.items():
            if values in [1,2]:
                modified.append([a for a in i if keys in a])
    # If there are no clear currency direction
    else:
        modified.append([0])

print ("Here is our trade")

--------------------------------
# Most Possible Currency Trades
--------------------------------
for i in range (len(modified)):
    if modified[i] != [0]:
        print (str (all_combo[i]) + ' >>> ' + str(modified[i]))
-------------------------------
			

			
	
