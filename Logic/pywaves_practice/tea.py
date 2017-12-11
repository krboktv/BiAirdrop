import pywaves as pw


# myAddress = pw.Address(privateKey='CtMQWJZqfc7PRzSWiMKaGmWFm4q2VN5fMcYyKDBPDx6S')
# otherAddress = pw.Address('3PNTcNiUzppQXDL9RZrK3BcftbujiFqrAfM')
# myAddress.sendWaves(otherAddress, 10000000)
# myToken = myAddress.issueAsset('Token1', 'My Token', 1000, 0)
# while not myToken.status():
# 	pass
# myAddress.sendAsset(otherAddress, myToken, 50)

# Point on node we're gonna work with
pw.setNode('https://testnode1.wavesnodes.com','testnet')
myAddress = pw.Address(privateKey='7XSgNdnwNF6mcQxPLggFsgxWvJCVG2pige2i8qhWxpfv')
print(pw.Address.balance(myAddress))
otherAddress = pw.Address('3MqSUG4WePmQBEVqreAMc3FrYJuR1Jm3vRZ')
print(pw.Address.balance(otherAddress))
myAddress.sendWaves(otherAddress,1)
print(pw.Address.balance(myAddress))
print(pw.Address.balance(otherAddress))
BiairdropTocken = pw.Asset('32kTPfXsUSWwjquT4NcXa52sLt9wWNngzY9SVvQbowH1')
# myToken = myAddress.issueAsset('Biairdrop2', 'Tocken created via api', 1337, 10)
# while not myToken.status():
# 	pass
# myAddress.sendAsset(otherAddress, myToken, 50)

myAddress.sendAsset(recipient=otherAddress, asset=BiairdropTocken, amount = 100000000)