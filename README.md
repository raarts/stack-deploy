Stack Deploy
============

Deploy a docker stack file to a docker swarm. For use in a GitLab 
CI environment. Can also create docker networks, but in a specific
naming convention.

Includes [ansible-lookup-gitlab-ci-env](https://github.com/raarts/ansible-lookup-gitlab-ci-env)

Requirements
------------

None

Role Variables
--------------

* stack: basename of the stack .yml file, expected in the ./stacks directory
* docker_networks: array of docker network names to create
* docker_registry: name of the registry to download images from
* debug: if true leaves info on env variables in /tmp


Dependencies
------------

none

Example Playbook
----------------

	- name: "Deploy the API"
	  hosts: all
	  become: true
	  roles:
	    - { role: stack-deploy }

License
-------

BSD



