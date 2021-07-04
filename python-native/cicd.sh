#!/bin/bash
export CICD_BUILD_IMAGE_NAME="python-native"
export CICD_BUILD_IMAGE_TAG="20"
export CICD_MICROSERVICE_NAME="${CICD_BUILD_IMAGE_NAME}-microservice"
export CICD_MICROSERVICE_NAMESPACE="sorting-${CICD_BUILD_IMAGE_NAME}"
# export CICD_BUILD_IMAGE_TAG="$(date +%s)"
export CICD_BUILD_IMAGE="${CICD_BUILD_IMAGE_NAME}:${CICD_BUILD_IMAGE_TAG}"
chmod +x ./build.sh ./deploy.sh
docker inspect "${CICD_BUILD_IMAGE_NAME}:${CICD_BUILD_IMAGE_TAG}" > /dev/null 2>&1 || ./build.sh
./deploy.sh
SERVICE_IP=$(kubectl get svc --namespace "${CICD_MICROSERVICE_NAMESPACE}" "${CICD_MICROSERVICE_NAME}" --template "{{ range (index .status.loadBalancer.ingress 0) }}{{.}}{{ end }}")
# echo http://$SERVICE_IP:8001
sleep 15s
curl "http://${SERVICE_IP}:8001/startreceive" --max-time 1
kubectl --namespace "${CICD_MICROSERVICE_NAMESPACE}" logs $(kubectl --namespace "${CICD_MICROSERVICE_NAMESPACE}" get pods  --field-selector=status.phase=Running -o custom-columns=":metadata.name") -f