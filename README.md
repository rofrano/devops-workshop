# DevOps Workshop

[![Build Status](https://travis-ci.org/showei/devops-workshop.svg?branch=master)](https://travis-ci.org/showei/devops-workshop)

DevOps Workshop Training that uses Vagrant, VirtualBox, Docker, and Minikube

This repository is part of a 4 Hour DevOps Workshop that gives attendees first hand experience in building a microservice and deploying it as a container on Kubernetes using DevOps practices and methods. It demonstrates how to create a simple RESTful service using Python Flask and SQLAlchemy to access a persistent resource. Its purpose is to show the correct API and return codes that should be used for a REST API. This repo also demonstrates the use of Test Driven Development which us required for setting on a Continuous Integrate and Continuous Delivery Pipeline (CI/CD).

During the workshop, attendees will build a simple Python Flask microservice using Test Driven Development techniques and run it locally. Then we will introduce the concepts of Docker and wrap that service in a Docker container and re-run our tests proving that the behavior has not changed. Using Jenkins and minikube, we will set up a CI/CD pipeline and deploy the microservice to a local minikube Kubernetes cluster. Finally we will add persistence to our microservice and deploy a PostgreSQL service in our Kubernetes cluster for our microservice to use showing how to use secrets for storing sensitive information like database credentials.

The workshop will switch between lecture and lab several times as new concepts are introduced and then quickly demonstrated and implemented in the hands-on exercise. Attendees will come away with a good understanding of how modern software is delivered using DevOps tools and practices with a programmable containerized infrastructure like Kubernetes.

## Prerequisite Installation

The first problem every software development team encounters is how to get developers productive quickly and keep them productive by giving them a consistent development environment that is easy to setup and maintain. Some developers might have Mac laptops while others prefer Windows, and still others prefer Linux; but these environments are very different and do not behave the same. To solve this problem, will we use **VirtualBox** and **Vagrant** to provide an _Infrastructure as Code_ environment on the developers desktop. If you don't have this software installed on your development computer, the first step is down download and install it.

### Mac installation

**Homebrew** is my preferred method of installing tools on the Mac. First because it is quick and easy, and second because maintaining the latest version is done for you with a simple `brew upgrade` command. If you are tired of downloading software and keeping it up to date, you want to use `brew` instead:

Install **Homebrew** if you don't have it already:

```sh
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install **VirtualBox** and **Vagrant** using the `brew` command

```sh
  brew cask install virtualbox
  brew cask install vagrant
```

That will install the necessary software for this workshop onto your Mac. If you don't want to use Homebrew, you can follow the Windows installation instructions and install VirtualBox and Vagrant manually.

### Windows installation

For Windows you must manually download and install the software. They can be obtained from the following links:

Download [VirtualBox](https://www.virtualbox.org/)

Download [Vagrant](https://www.vagrantup.com/)

Install both of these in that order. This will install the necessary software for this workshop onto your Windows PC. Windows users will also need a `git` client. If you don't have one, you can get it from [git-scm.com](https://git-scm.com/)

## Bring up the Ubuntu Linux Virtual Machine

Now you are ready to `clone` the project to your development folder and create your Vagrant vm. Open a terminal/shell window and change to a folder on your computer that you want to keep the source code for this workshop.

```sh
  git clone https://github.com/rofrano/devops-workshop.git
  cd devops-workshop
  vagrant up
```

This will bring up the VM and install a Python 3 development environment with `minikube` and the Kubernetes CLI (`kubectl`) for deploying to Kubernetes.

## Using the VM

Vagrant sets up private ssh so that you don't need a key. This VM should be treated just like a remote server in the cloud. To get into it use:

```sh
  vagrant ssh
```

You should now be inside the VM and ready to follow alone with the workshop.

## Exiting the VM and shutting it down

Just like a remote server, you logout of the VM using the `exit` command. You can also shutdown the virtual machine using the `vagrant halt` command:

```sh
  exit
  vagrant halt
```

This will shutdown the VM. When are are ready to use it again, just `cd` into the `devops-workshop` folder and use `vagrant up` to bring it back up.

## Removing the Virtual Machine

You can remove the vagrant VM to free up space on your computer or to recreate it again because something has gone horribly wrong. If we keep all of our work under the `/vagrant` folder, it will be safely stored on our computer and the VM can be destroyed and recreated at any time with:

```sh
  vagrant destroy
```

This will delete the virtual machine from your computer.

## Global Status

As you use Vagrant you will want to know if you left any virtual machines running. This can be easily seen using the `vagrant global-status` command:

```sh
  vagrant global-status
```

The results on my Mac were:

```sh
  $ vagrant global-status
  id       name    provider   state    directory
  ---------------------------------------------------------------------------
  33160a7  default virtualbox poweroff /Users/rofrano/GitHub/devops-workshop

  The above shows information about all known Vagrant environments
  on this machine. This data is cached and may not be completely
  up-to-date (use "vagrant global-status --prune" to prune invalid
  entries). To interact with any of the machines, you can go to that
  directory and run Vagrant, or you can use the ID directly with
  Vagrant commands from any directory. For example:
  "vagrant destroy 1a2b3c4d"
```

This shows that I have a vagrant VM defined under `/Users/rofrano/GitHub/devops-workshop` and that it is currently in the `poweroff` state. _Hint: If your laptop batter is excessively draining and you don't know why, it's always a good idea to check and see if you left any virtual machines running in the background!_

## Copyright
(c) 2019 John Rofrano, All Rights Reserved
