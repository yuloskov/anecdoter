docker-machine create --driver=vmware manager
docker-machine create --driver=vmware worker1
docker-machine create --driver=vmware worker2

docker-machine ssh manager

