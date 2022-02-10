from requests import Request, Session
import json

contracts = [("0x3C2e501B08CF5C16061468c96b19b32bae451dA3",20,2663625579.139427),
            ("0xC001BBe2B87079294C63EcE98BdD0a88D761434e",646.79,663000000),
            ("0x51812403611fF41C37dC91D8C2A4Ab2a5FFfC827",500,10569325458.417233),
             ("0xDa6802BbEC06Ab447A68294A63DE47eD4506ACAA",11.10,268745146.6085738),
             ("0x17245F6C4f54B84Bb71AEAeEf38cec57b7F9a77b",20,23128312.813553713),
             ("0x17FAbAF66256fb40F350576bafA1807429708E34",20,2251786.7200585664),
             ("0x0cD022ddE27169b20895e0e2B2B8A33B25e63579",11.10,23280.4319),
             ("0x42981d0bfbAf196529376EE702F2a9Eb9092fcB5",55.49,10193.812786965)]


base_poo = "https://api.pancakeswap.info/api/v2/tokens/"


def pancake(contract_address):

    session = Session()
#     session.headers.update(headers)

    response = session.get(base_poo+contract_address)
    data = json.loads(response.text)['data']

    return (data)

net = 0
sum_invested = 0

for each in contracts:
    sum_invested+=each[1]
    temp = pancake(each[0])
    temp_amt = (float(temp['price'])*each[2])-each[1]
    net+=temp_amt
    print(f"{temp['name']} : {temp_amt}")

print(f"\n\nTotal Invested : {sum_invested}")
print(f"Total Gain/Loss : {net}")
print(f"Total Net : {sum_invested+net}")