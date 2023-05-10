
### First: setup a blockchain etherum network

1 - setup project and deploy smart contract : 
https://github.com/Badro1859/EHR-SHARE-SYS.git

2 - copy smart contracts (HealthActor, Patient) :
    - from : EHR-SHARE-SYS/build/contract
    - to : HealTech/front-Vue/src/assets/smart-contract

### Second: setup the different service
you can setup this projects in different way :
#### 1. Docker
##### step 1: install docker
    sudo apt get install docker.io docker-compose -y
##### step 2: run docker-compose file
    sudo docker-compose up -d --build

#### 2. Developement envirenement
##### step1: Backend
    cd backend-Django
    python3 install -r requirement.txt
    python3 src\manage.py runserver

##### step2: Frontend
    cd frontend-Vue
    npm install
    npm run dev

##### step3: IPFS network
    sudo apt get install docker.io -y
    cd ipfs
    sudo docker build . -t ipfs
    sudo docker run -p 4001:4001 -p 5001:5001 ipfs

### Third: Use the application
##### http://localhost:8080
