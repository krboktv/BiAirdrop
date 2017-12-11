"""by a37h@biairdrop, 11.11.17

"""
import pywaves as pw

# Point on node we're gonna work with
pw.setNode('https://testnode1.wavesnodes.com','testnet')
def activateAirdrop(node_adress, node_type, waves_acc_and_tok_to_be_sent, token_info):
    token_info = [x.split() for x in open(token_info)]
    waves_tokens_table = [x.split() for x in open(waves_acc_and_tok_to_be_sent)]
    # for x in token_info:
    #     print(x)
    # print()
    # print()
    # for x in waves_tokens_table:
    #     print(x)
    ownerAddress = pw.Address(privateKey=token_info[0][1])
    # print(token_info[0][1])
    # print(ownerAddress)
    ourToken = pw.Asset(token_info[1][1])
    ourTokenDecimals = ourToken.decimals
    for w_a_t_pairs in waves_tokens_table:
        otherAddress = pw.Address(w_a_t_pairs[0])
        ownerAddress.sendAsset(recipient=otherAddress, asset=ourToken,
                               amount=int(float(w_a_t_pairs[1])*(10**ourTokenDecimals)))
