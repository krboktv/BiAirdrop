import biairdroplib.bc
import biairdroplib.aird
#
# address = input()
# biairdroplib.bc.printEthWalletBalanace(address)

# biairdroplib.bc.parseAccsAndCalculateBalances('users_db.txt')
# print('firststagecompelte')
biairdroplib.aird.activateAirdrop(node_adress='https://testnode1.wavesnodes.com',
                                  node_type='testnet',
                                  waves_acc_and_tok_to_be_sent='waves_and_tokens.txt',
                                  token_info='token_owner_and_id_info.txt')
