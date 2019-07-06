# Introduction to Kubernetes

This hands on shows you how to create a local clueter using `minikube` and deploy your Docker containers to Kubernetes

## Create your Kubernetes Cluster

We will use Minikube to create a Kubernetes Cluster in your VM

```sh
  $ export CHANGE_MINIKUBE_NONE_USER=true
  $ sudo minikube start --vm-driver=none
```

Once the clueter is created we need to fix the permissions with the configuration files

```sh
  $ sudo chown -R $USER $HOME/.kube $HOME/.minikube
  $ sudo minikube addons enable ingress
```

You check that everything works with:

```sh
  kubectl get all
```
You should see something like:

```
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   3m44s
```

We are now ready to use Kubernetes.
