#!/bin/bash
helm upgrade --install python-playg ./python-playg -f ./python-playg/values.yaml --set image.repository=${CICD_BUILD_IMAGE_NAME} --set image.tag=${CICD_BUILD_IMAGE_TAG}