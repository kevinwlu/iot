# Lesson 10: Blockchain

* [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
  * [Distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger)
  * [Hyperledger](https://en.wikipedia.org/wiki/Hyperledger)
  * [Decentralized autonomous organization](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization) (DAO)
  * [Decentralized finance](https://en.wikipedia.org/wiki/Decentralized_finance) (DeFi)
  * [Hash function](https://en.wikipedia.org/wiki/Hash_function)
  * [Cryptographic hash function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
  * [SHA-2](https://en.wikipedia.org/wiki/SHA-2) (Secure Hash Algorithm 2)
  * [SHA-3](https://en.wikipedia.org/wiki/SHA-3) (Secure Hash Algorithm 3)
  * [Blockchain repositories](https://github.com/blockchain)
* [Cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency)
  * [List of cryptocurrencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)
  * [Cryptocurrency prices by maket cap](https://coinmarketcap.com/)
  * [Cryptocurrency exchange](https://en.wikipedia.org/wiki/Cryptocurrency_exchange)
  * [List of largest cryptocurrency exchanges](https://en.wikipedia.org/wiki/List_of_largest_cryptocurrency_exchanges)
  * [Crypto-wikipedia](https://crypto-wikipedia.com/)
* [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin)
  * [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto), "[Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)," [Oct. 31, 2008](https://archive.is/20121228025845/http://article.gmane.org/gmane.comp.encryption.general/12588/#selection-179.7-179.30)
  * [Double-spending problem](https://en.wikipedia.org/wiki/Double-spending)
  * [Proof of work](https://en.wikipedia.org/wiki/Proof_of_work)
  * [Mining](https://en.bitcoin.it/wiki/Mining)
  * [Nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce)
  * [Bitcoin network](https://en.wikipedia.org/wiki/Bitcoin_network)
  * [Blocks](https://www.blockchain.com/btc/blocks) by [Blockchain.com](https://www.blockchain.com/)
  * [Blocks list](https://btc.com/btc/blocks) by [BTC.com](https://btc.com/en)
  * [Genesis block](https://en.bitcoin.it/wiki/Genesis_block) on [2009-01-03](https://btc.com/btc/block/0)
  * [Cambridge Bitcoin Electricity Consumption Index](https://cbeci.org/) (CBECI)
  * [Lightening Network](https://en.wikipedia.org/wiki/Lightning_Network)
* [Altcoins](https://en.wikipedia.org/wiki/Cryptocurrency#Altcoins) (alternative cryptocurrencies) are tokens, cryptocurrencies, and other types of digital assets that are not bitcoin
* [Ethereum](https://en.wikipedia.org/wiki/Ethereum)
  * [Smart contract](https://en.wikipedia.org/wiki/Smart_contract)
  * [Blockchain oracle](https://en.wikipedia.org/wiki/Blockchain_oracle)
  * [Chainlink](https://en.wikipedia.org/wiki/Chainlink_(cryptocurrency))
  * [Polygon](https://polygon.technology/)
* [Algorand](https://en.wikipedia.org/wiki/Algorand_(cryptocurrency_platform))
* [Cardano](https://en.wikipedia.org/wiki/Cardano_(blockchain_platform))
* [Dash](https://en.wikipedia.org/wiki/Dash_(cryptocurrency))
* [Helium System](https://www.helium.com/)
* [Polkadot](https://en.wikipedia.org/wiki/Polkadot_(cryptocurrency))
* [Solana](https://en.wikipedia.org/wiki/Solana_(blockchain_platform))
* [Terra](https://www.terra.money/)
  * [Terra (currency)](https://en.wikipedia.org/wiki/Terra_(currency))
* [Uniswap](https://en.wikipedia.org/wiki/Uniswap)
* [Stablecoin](https://en.wikipedia.org/wiki/Stablecoin)
* [CBDC](https://en.wikipedia.org/wiki/Central_bank_digital_currency) (Central bank digital currency)
* [Diem](https://en.wikipedia.org/wiki/Diem_(digital_currency)) (rebraded from Libra in December 2020) proposed by [Meta Platforms](https://en.wikipedia.org/wiki/Meta_Platforms) (rebraded from Facebook on October 28, 2021)
  * [Diem Blockchain](https://developers.diem.com/main)
  * [Proof of stake](https://en.wikipedia.org/wiki/Proof_of_stake)
  * [Byzantine fault](https://en.wikipedia.org/wiki/Byzantine_fault) tolerance (BFT)
* [GNU Taler](https://en.wikipedia.org/wiki/GNU_Taler) (Taxable Anonymous Libre Economic Reserves)
* [IOTA](https://en.wikipedia.org/wiki/IOTA_(technology))
  * [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG)
  * [IOTA Tangle MainNet](http://tangle.glumb.de/)
  * [IOTA Tangle Explorer](https://thetangle.org/) by [Peter Willemsen](https://github.com/peterwilli) and contributors
* [Ruuvi](https://ruuvi.com/) Innovations Ltd ([Oy](https://en.wikipedia.org/wiki/Osakeyhti%C3%B6)), Finland
  * [Ruuvi](https://fi.wikipedia.org/wiki/Ruuvi) is the Finnish word for "screw"
  * [RuuviTag](https://ruuvi.com/ruuvitag/) wireless temperature sensor
  * Ruuvi GitHub [Repositories](https://github.com/ruuvi)
  * [RuuviLab](https://lab.ruuvi.com/) community
* [Non-fungible token](https://en.wikipedia.org/wiki/Non-fungible_token) (NFT)
  * [List of most expensive non-fungible tokens](https://en.wikipedia.org/wiki/List_of_most_expensive_non-fungible_tokens)
  * [GFT Exchange](https://www.gft.exchange/)
  * [OpenSea](https://en.wikipedia.org/wiki/OpenSea)
  * [Sfermion](https://www.sfermion.io/)
  * [SuperRare](https://superrare.com/)

## Lab 10A: Blockchain

### Hash function with randomization
* Run hash_value.py twice and compare results
```sh
$ cd ~/iot/lesson10
$ cat hash_value.py
$ python3 hash_value.py
$ python3 hash_value.py
```
### SHA-2 Secure Hash Algorithm
* SHA-256 hash values or digests are 256 [bits](https://en.wikipedia.org/wiki/Bit) or 32 [bytes](https://en.wikipedia.org/wiki/Byte)
* Each [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) digit represents four binary digits, a [nibble](https://en.wikipedia.org/wiki/Nibble), which is half a byte
```sh
$ python3
>>> import hashlib
>>> m = hashlib.sha256(b"hello, world")
>>> m.hexdigest()
>>> m.digest_size
>>> m.block_size
>>> exit()
```

### [Build the tiniest blockchain](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b) in [less than 50 lines of Python](https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2) by [Gerald Nash](https://github.com/aunyks) (2017-07-16)
```sh
$ cd ~/iot/lesson10
$ cat snakecoin.py
$ python3 snakecoin.py
```
### [Let’s Make the Tiniest Blockchain Bigger](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d) Part 2: [With More Lines of Python](https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173) by Gerald Nash (2017-07-23)
#### Terminal 1: Run the SnakeCoin server at http://127.0.0.1:5000/ (Press Ctrl+C to quit)
```sh
$ cat snakecoin-server-full-code.py
$ python3 snakecoin-server-full-code.py
$ cd
```
#### Terminal 2: Create a transaction and mine a new block at http://127.0.0.1:5000/mine
```sh
$ curl "localhost:5000/txion" \
     -H "Content-Type: application/json" \
     -d '{"from": "akjflw", "to":"fjlakdj", "amount": 3}'
$ curl localhost:5000/mine
```

![server.png](/lesson10/server.png)

![txion.png](/lesson10/txion.png)

### [Python blockchain app](https://github.com/satwikkansal/python_blockchain_app) by [Satwik Kansal](https://github.com/satwikkansal)
#### Terminal 1: Uncomment the last line (Line 257) of node_server.py (or search for port=8000) and run (Press Ctrl+C to quit)
* In the [GNU nano](https://en.wikipedia.org/wiki/GNU_nano) text editor, Ctrl+W (shown as as ^W) goes to the search menu
```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
$ cd ~/python_blockchain_app
$ nano node_server.py
$ python3 node_server.py
```
#### Terminal 2: Run run_app.py (Press Ctrl+C to quit)
```sh
$ vncserver
$ cd ~/python_blockchain_app
$ python3 run_app.py
```
* Via VNC viewer, open a browser on Raspberry Pi and go to YourNet running at http://127.0.0.1:5000/
* Enter content and name, click "Post," and click "Request to mine" that generate "Block #1 is mined" at http://127.0.0.1:8000/mine
* At YourNet, click "Resync" to view Block #1

![post.png](/lesson10/post.png)

![mine.png](/lesson10/mine.png)

![sync.png](/lesson10/sync.png)

## Lab 10B: PyOTA
* Demonstrated on Raspberry Pi OS and Ubuntu
* [PyOTA](https://github.com/iotaledger/iota.py) (IOTA Python Client Library)
* [IRI](https://docs.iota.org/docs/node-software/1.0/overview) (IOTA Reference Implementation)

```sh
$ sudo pip3 install pyota[ccurl]
$ cd ~/iot/lesson10
$ cat iri_node_info.py
$ python3 iri_node_info.py
$ cd
```

## Lab 10C: IOTA DevNet
* This lab requires Raspberry Pi and Node.js v8 or v10
* Only sensor.js and mam_sensor.js require a DHT11 or DHT22 humidity and temperature sensor

### Send DHT11 sensor data to the IOTA Tangle using Masked Authenticated Messaging (MAM) by [Robert Lie](https://github.com/robertlie)
* [Tutorial](https://www.youtube.com/watch?v=atJ-ZT7aKoA)
* [IOTA quick guides](https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html)
  * Demonstrated with Node.js v8.11.1 on Raspberry Pi 3B+ and v10.24.0 on Raspberry Pi 4B
* Send DHT11 sensor data to the IOTA Tangle using MAM and Raspberry Pi 3 [GitHub repo](https://github.com/robertlie/dht11-raspi3)
* [IOTA MAM demo](https://www.mobilefish.com/services/cryptocurrency/mam.html)

### Download and build the C library for BCM2835
* [C library for Broadcom BCM 2835 as used in Raspberry Pi](http://www.airspayce.com/mikem/bcm2835/index.html)
* [BCM 2835 error on Raspberry Pi 4](https://github.com/nRF24/RF24/issues/517)
* [BCM 2835 driver updated](https://groups.google.com/forum/#!topic/bcm2835/BwZXVsDRtwI)
```sh
$ wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
$ tar zxvf bcm2835-1.60.tar.gz
$ cd bcm2835-1.60
$ ./configure
$ make
$ sudo make check
$ sudo make install
$ cd
```
### Clone the code repository
```sh
$ git clone https://github.com/robertlie/dht11-raspi3.git
$ cd dht11-raspi3
$ npm install
```
### Change nodes.testnet.iota.org to [nodes.devnet.iota.org](https://docs.iota.org/docs/getting-started/0.1/network/iota-networks)
```sh
$ cd ~/dht11-raspi3
$ nano mam_publish.js
$ nano mam_receive.js
$ nano mam_sensor.js
```
### Transactions in the Devnet must use a [minimum weight magnitude](https://docs.iota.org/docs/getting-started/1.1/first-steps/sending-transactions#doing-proof-of-work) (MWM) of 9 to be valid
### Edit mam.client.js to search mwm and change it from 14 to 9 at the end of Line 23375
* In the [GNU nano](https://en.wikipedia.org/wiki/GNU_nano) text editor, Ctrl+W (shown as as ^W) goes to the search menu
```sh
$ cd ~/dht11-raspi3/lib
$ nano mam.client.js
```
### Terminal 1: Run mam_publish.js (Press Ctrl+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_publish.js
```
### Terminal 2 on the same or another Raspberry Pi: Run mam_receive.js (Press Ctrl+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_receive.js YOUR_ROOT
```

### Change sensor type from DHT11 to DHT22 and GPIO pin from 4 to 24 (The sensor is required)
```sh
$ cd ~/dht11-raspi3
$ nano sensor.js
$ nano mam_sensor.js
$ node sensor.js
```

![dht22_bb.png](https://github.com/kevinwlu/iot/blob/master/lesson10/dht22_bb.png)

### Terminal 1: Run mam_sensor.js (Press Ctrl+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_sensor.js
```
### Terminal 2 on the same or another Raspberry Pi: Run mam_receive.js (Press Ctrl+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_receive.js YOUR_ROOT
```
