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
$
```
### Terminal 1
```sh
$ git clone https://github.com/satwikkansal/python_blockchain_app.git
$ export FLASK_APP=node_server.py
$ cd python_blockchain_app
$ flask run --port 8000
```
* Serving Flask app "node_server"
* Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)

### Terminal 2
```sh
$ cd python_blockchain_app
$ python3 run_app.py
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with inotify reloader
* Debugger is active!
* Debugger PIN: 184-619-943

## Lab B: IOTA

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
$ nano mam_publish.js
$ nano mam_receive.js
$ nano mam_sensor.js
```
### Terminal 1: Run mam_publish.js (Press CTRL+Z to stop)
```sh
$ node mam_publish.js
```
### Terminal 2: Run mam_receive.js (Press CTRL+Z to stop)
```sh
$ node mam_receive.js YOUR_ROOT
```
### Change sensor type to DHT22 and GPIO pin to 24
```sh
$ nano sensor.js
$ nano mam_sensor.js
$ node sensor.js
```
### Terminal 1: Run mam_sensor.js (Press CTRL+Z to stop)
```sh
$ node mam_sensor.js
```
### Terminal 2: Run mam_receive.js (Press CTRL+Z to stop)
```sh
$ node mam_receive.js YOUR_ROOT
```
