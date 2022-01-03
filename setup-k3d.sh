#!/bin/bash

echo "Please install K3D and make it available in your PATH"

echo "Then press ENTER: "
read dummy

mkdir -p local-persistent-data

k3d cluster create demo --volume `pwd`/local-persistent-data:/persistent-data --registry-create k3d-registry:38597
kubectl config use-context k3d-demo

echo ""
echo ""
echo ""
echo ""
echo "Add the following into your /etc/hosts :"
echo "127.0.0.1       k3d-registry"
echo ""
echo ""
