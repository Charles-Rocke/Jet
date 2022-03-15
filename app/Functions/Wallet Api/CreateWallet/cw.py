from app.Constants.constants import API_KEY
from trinsic.service_clients import WalletClient, ServiceClientCredentials


# Wallet API
wallet_client = WalletClient(ServiceClientCredentials(API_KEY))
wallet_client.config.retry_policy.retries = 0

owner_name = None  # Can be None
wallet_id = None  # Can be None
wallet = wallet_client.create_wallet({
  "ownerName": owner_name,
  "wallet_id": wallet_id
})