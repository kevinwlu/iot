# Lesson 10: Blockchain
* [Distributed ledger](https://en.wikipedia.org/wiki/Distributed_ledger)
* [Blockchain](https://en.wikipedia.org/wiki/Blockchain)
* [Hash function](https://en.wikipedia.org/wiki/Hash_function)
* [SHA-2](https://en.wikipedia.org/wiki/SHA-2)
* [IOTA](https://en.wikipedia.org/wiki/IOTA_(technology))

## Lab 10A: Blockchain

### Hash function and SHA-2 Secure Hash Algorithm
```sh
$ python3
>>> import hashlib
>>> m=hashlib.sha256(b"hello, world")
>>> m.hexdigest()
>>> m.digest_size
>>> m.block_size
>>> exit()
$ cd ~/iot/lesson10
$ python3 hash_value.py
```

### [Build the tiniest blockchain](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b) in [less than 50 lines of Python](https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2) by [Gerald Nash](https://github.com/aunyks)
```sh
$ cd ~/iot/lesson10
$ python3 snakecoin.py
$ cd
```
### Python blockchain app by [Satwik Kansal](https://github.com/satwikkansal)
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

### [PyOTA](https://github.com/iotaledger/iota.py) (IOTA Python Client Library) and [IRI](https://docs.iota.org/docs/node-software/0.1/iri/introduction/overview) (IOTA Reference Implementation)

```sh
$ sudo pip3 install pyota[ccurl]
$ cd ~/iot/lesson10
$ python3 iri_node_info.py
$ cd
```

### Send DHT11 sensor data to the IOTA Tangle using MAM by [Robert Lie](https://github.com/robertlie)
* [Tutorial](https://www.youtube.com/watch?v=atJ-ZT7aKoA)
* [IOTA quick guides](https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html)
* [Send DHT11 sensor data to the IOTA Tangle using MAM and Raspberry Pi 3](https://github.com/robertlie/dht11-raspi3)
* [IOTA masked authenticated messaging demo](https://www.mobilefish.com/services/cryptocurrency/mam.html)

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
### Change nodes.testnet.iota.org to nodes.devnet.iota.org
```sh
$ cd ~/dht11-raspi3
$ nano mam_publish.js
$ nano mam_receive.js
$ nano mam_sensor.js
```
### Terminal 1: Run mam_publish.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_publish.js
```
### Terminal 2: Run mam_receive.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_receive.js YOUR_ROOT
```
### Change sensor type to DHT22 and GPIO pin to 24 (The sensor is required)
```sh
$ cd ~/dht11-raspi3
$ nano sensor.js
$ nano mam_sensor.js
$ node sensor.js
```
### Terminal 1: Run mam_sensor.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_sensor.js
```
### Terminal 2: Run mam_receive.js (Press CTRL+Z to stop)
```sh
$ cd ~/dht11-raspi3
$ node mam_receive.js YOUR_ROOT
```
