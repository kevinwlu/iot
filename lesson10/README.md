# <a href="https://goo.gl/RIzzfl">Lesson 10</a>: Blockchain

## Build the tiniest blockchain (by Gerald Nash)

https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b

https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2

cd ~/iot/lesson10

python3 hash_value.py

python3 snakecoin.py

## Send DHT11 sensor data to the IOTA Tangle using MAM (by Robert Lie)

https://www.youtube.com/watch?v=atJ-ZT7aKoA

https://www.mobilefish.com/developer/iota/iota_quickguide_raspi_mam.html

https://github.com/robertlie/dht11-raspi3

https://www.mobilefish.com/services/cryptocurrency/mam.html

http://www.airspayce.com/mikem/bcm2835/index.html

### Install library

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz

tar zxvf bcm2835-1.60.tar.gz

cd bcm2835-1.60

./configure

make

sudo make check

sudo make install

cd

### Clone repo

git clone https://github.com/robertlie/dht11-raspi3.git

cd dht11-raspi3

npm install

### Change nodes.testnet.iota.org to nodes.devnet.iota.org

nano mam_publish.js

nano mam_receive.js

nano mam_sensor.js

### Run mam_publish.js on one terminal and mam_receive.js on another

node mam_publish.js

node mam_receive.js YOUR_ROOT

### Publish sensor data on one terminal and receive on another

node sensor.js

node mam_sensor.js

node mam_receive.js YOUR_ROOT
