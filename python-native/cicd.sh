#!/bin/bash
export CICD_BUILD_IMAGE_NAME="python-native"
export CICD_BUILD_IMAGE_TAG="1"
export CICD_BUILD_IMAGE="${CICD_BUILD_IMAGE_NAME}:${CICD_BUILD_IMAGE_TAG}"
chmod +x ./build.sh ./deploy.sh
docker inspect "${CICD_BUILD_IMAGE_NAME}:${CICD_BUILD_IMAGE_TAG}" > /dev/null 2>&1 || ./build.sh
./deploy.sh
