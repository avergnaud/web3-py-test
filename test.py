from web3.auto import w3
from eth_account.messages import defunct_hash_message

public_address = "0xd2e42398e63a9c638444087b3d1e76c3cf1508fa"
print(public_address)

message_hash = defunct_hash_message(text="I am signing my one-time nonce: 4246")
signed_message = "0x51473c27def5921f18dfefb9dbb95f315f38f75a7b36b1f09f8b28d3f67cefdb3f5938e5e5c53f8ed4887995e85f476f5710d3b110453de4b624c7a0761b57481b"
address_recovered = w3.eth.account.recoverHash(message_hash, signature=signed_message)
print(address_recovered)