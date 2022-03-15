from app.Constants.constants import API_KEY
from trinsic.service_clients import CredentialsClient, WalletClient, ServiceClientCredentials


# Credentials API
credentials_client = CredentialsClient(ServiceClientCredentials(API_KEY))
credentials_client.config.retry_policy.retries = 0

# Wallet API
wallet_client = WalletClient(ServiceClientCredentials(API_KEY))
wallet_client.config.retry_policy.retries = 0