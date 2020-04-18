# <a href="https://goo.gl/RIzzfl">Lesson 10</a>: Blockchain

## Lab A: Blockchain

### Build the tiniest blockchain (by Gerald Nash)

https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2

```sh
$ cd ~/iot/lesson10
$ python3 hash_value.py
$ python3 snakecoin.py
$ python3
>>> import hashlib
>>> m=hashlib.sha256(b"hello, world")
>>> m.hexdigest()
>>> m.digest_size
>>> m.block_size
>>> exit()
$ cd
```
### Terminal 1: Run node_server.py (Press CTRL+C to quit)
```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
$ export FLASK_APP=node_server.py
$ cd ~/python_blockchain_app
$ flask run --port 8000
```

### Terminal 2: Run run_app.py (Press CTRL+C to quit)
```sh
$ vncserver
$ cd ~/python_blockchain_app
$ python3 run_app.py
```

Via VNC viewer, open a browser on Raspberry Pi and go to YourNet running at at http://127.0.0.1:5000/ 

Enter content and post name, click "Request to mine" that generate "Block #1 is mined" at http://127.0.0.1:8000/mine

At YourNet, click "Resync" to view Block #1

## Lab B: IOTA

### [PyOTA](https://github.com/iotaledger/iota.py) (IOTA Python Client Library) and [IRI](https://docs.iota.org/docs/node-software/0.1/iri/introduction/overview) (IOTA Reference Implementation)

```sh
$ sudo pip3 install pyota[ccurl]
$ cd ~/iot/lesson10
$ python3 iri_node_info.py
$ cd
```

### Send DHT11 sensor data to the IOTA Tangle using MAM (by Robert Lie)

https://www.youtube.com/watch?v=atJ-ZT7aKoA

https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html

https://github.com/robertlie/dht11-raspi3

https://www.mobilefish.com/services/cryptocurrency/mam.html

### Download and build the C library for BCM2835

http://www.airspayce.com/mikem/bcm2835/index.html

https://github.com/nRF24/RF24/issues/517

https://groups.google.com/forum/#!topic/bcm2835/BwZXVsDRtwI
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
