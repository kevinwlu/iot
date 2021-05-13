# Lesson 10: Blockchain

* [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
  * [Hyperledger](https://en.wikipedia.org/wiki/Hyperledger)
  * [Hash function](https://en.wikipedia.org/wiki/Hash_function)
  * [SHA-2](https://en.wikipedia.org/wiki/SHA-2) (Secure Hash Algorithm 2)
  * [Blockchain repositories](https://github.com/blockchain)
* [Bitcoin](https://en.wikipedia.org/wiki/Bitcoin)
  * [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto), "[Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)," [Oct. 31, 2008](https://archive.is/20121228025845/http://article.gmane.org/gmane.comp.encryption.general/12588/#selection-179.7-179.30)
  * [Double-spending problem](https://en.wikipedia.org/wiki/Double-spending)
  * [Proof of work](https://en.wikipedia.org/wiki/Proof_of_work)
  * [Bitcoin network](https://en.wikipedia.org/wiki/Bitcoin_network)
  * [Block list](https://btc.com/block) since [2009-01-03](https://btc.com/block?date=2009-01-03)
  * [Cambridge Bitcoin Electricity Consumption Index](https://cbeci.org/) (CBECI)
  * [Distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger)
* [Ethereum](https://en.wikipedia.org/wiki/Ethereum)
  * [Smart contract](https://en.wikipedia.org/wiki/Smart_contract)
  * [Blockchain oracle](https://en.wikipedia.org/wiki/Blockchain_oracle)
  * [Chainlink](https://en.wikipedia.org/wiki/Chainlink_(cryptocurrency))
* [Ripple](https://en.wikipedia.org/wiki/Ripple_(payment_protocol))
* [Diem](https://en.wikipedia.org/wiki/Diem_(digital_currency)) (rebraded from Libra in December 2020)
  * [Diem Blockchain](https://developers.diem.com/main)
  * [Proof of stake](https://en.wikipedia.org/wiki/Proof_of_stake)
  * [Byzantine fault](https://en.wikipedia.org/wiki/Byzantine_fault) tolerance (BFT)
* [Stablecoin](https://en.wikipedia.org/wiki/Stablecoin)
* [IOTA](https://en.wikipedia.org/wiki/IOTA_(technology))
  * [Directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG)
  * [IOTA Tangle Utilities](https://utils.iota.org/)
  * [IOTA Tangle MainNet](http://tangle.glumb.de/)
  * [IOTA Tangle Explorer](https://thetangle.org/) by [Peter Willemsen](https://github.com/peterwilli) and contributors

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
* SHA-256 hash values or digests are 256 bits or 32 bytes
* Each [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) digit represents four binary digits, a [nibble](https://en.wikipedia.org/wiki/Nibble), which is half a byte
```sh
$ python3
>>> import hashlib
>>> m=hashlib.sha256(b"hello, world")
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
```sh
$ cat snakecoin-server-full-code.py
$ python3 snakecoin-server-full-code.py
$ cd
```
* Running on http://127.0.0.1:5000/mine (Reload the page to mine and press CTRL+C to quit)

### [Python blockchain app](https://github.com/satwikkansal/python_blockchain_app) by [Satwik Kansal](https://github.com/satwikkansal)
#### Terminal 1: Run node_server.py (Press CTRL+C to quit)
```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
$ export FLASK_APP=node_server.py
$ cd ~/python_blockchain_app
$ flask run --port 8000
```
#### Terminal 2: Run run_app.py (Press CTRL+C to quit)
```sh
$ vncserver
$ cd ~/python_blockchain_app
$ python3 run_app.py
```
* Via VNC viewer, open a browser on Raspberry Pi and go to YourNet running at at http://127.0.0.1:5000/ 
* Enter content and post name, click "Request to mine" that generate "Block #1 is mined" at http://127.0.0.1:8000/mine
* At YourNet, click "Resync" to view Block #1

## Lab 10B: IOTA

* Only sensor.js and mam_sensor.js require a DHT11 or DHT22 humidity and temperature sensor

### [PyOTA](https://github.com/iotaledger/iota.py) (IOTA Python Client Library) and [IRI](https://docs.iota.org/docs/node-software/1.0/overview) (IOTA Reference Implementation)

```sh
$ sudo pip3 install pyota[ccurl]
$ cd ~/iot/lesson10
$ cat iri_node_info.py
$ python3 iri_node_info.py
$ cd
```

### Send DHT11 sensor data to the IOTA Tangle using Masked Authenticated Messaging (MAM) by [Robert Lie](https://github.com/robertlie)
* [Tutorial](https://www.youtube.com/watch?v=atJ-ZT7aKoA)
* [IOTA quick guides](https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html)
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
### Edit mam.client.js with ^W to search mwm and change it from 14 to 9 at the end of Line 23375
```sh
$ cd ~/dht11-raspi3/lib
$ nano mam.client.js
```
### Terminal 1: Run mam_publish.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_publish.js
```
### Terminal 2 on the same or another Raspberry Pi: Run mam_receive.js (Press CTRL+Z to stop)
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

### Terminal 1: Run mam_sensor.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_sensor.js
```
### Terminal 2 on the same or another Raspberry Pi: Run mam_receive.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_receive.js YOUR_ROOT
```
