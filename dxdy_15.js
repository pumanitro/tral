/**
 * Simple JavaScript example demonstrating authentication with private WebSockets channels.
 */

const { DydxClient } = require('@dydxprotocol/v3-client')
const Web3 = require('web3')

const HTTP_HOST = 'https://api.dydx.exchange'

// NOTE: Set up web3 however your prefer to authenticate to your Ethereum account.
web3 = new Web3()
web3.eth.accounts.wallet.add(PRIVATE_ETH_KEY_FROM_METAMASK)

;((async () => {

  client = new DydxClient(HTTP_HOST, { web3 })

  const apiCreds = await client.onboarding.recoverDefaultApiCredentials(METAMASK_ETH_ADDRESS)
  client.apiKeyCredentials = apiCreds

  const leaderboardPnls = await client.public.getLeaderboardPnls(
    {
      period: 'ALL_TIME',
      sortBy: 'ABSOLUTE',
      limit: '10',
    }
  );

  const userETHAddresses = leaderboardPnls.topPnls
    .map(el => el.ethereumAddress)
    .filter(el => el);

  console.log('leaderboardPnls', leaderboardPnls);
  console.log('userETHAddresses', userETHAddresses);

  // this endpoint is private because you can access only your accounts:
  /*const accountPromises = userETHAddresses.map(addr => client.private.getAccount(
    addr,
  ));

  const accounts = await Promise.all(accountPromises);

  console.log('accounts', accounts);*/

  /*const user = await client.private.getUser();

  console.log('user', user);*/

})()).then(() => console.log('Done')).catch(console.error)
