build() {
	echo Removing existing docker containers
	docker rm -f `docker ps -aq`

	for script in */service/build.sh
	do
		parent=`dirname "${script}"`
		cd "${parent}"
		bash ./build.sh
		cd ../..
	done
}

build | tee gctf_docker_build.log
echo "IP address"
ifconfig eth0 | grep "inet "
docker ps --format 'table {{.Names}}\t{{.Ports}}'
