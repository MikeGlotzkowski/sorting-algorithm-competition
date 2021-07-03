#!/bin/bash
MICROSERVICE_NAME="${CICD_BUILD_IMAGE_NAME}-microservice"
helm upgrade --install "${MICROSERVICE_NAME}" "./${MICROSERVICE_NAME}" \
        -f "./${MICROSERVICE_NAME}/values.yaml" \
        --namespace "sorting-${CICD_BUILD_IMAGE_NAME}" --create-namespace \
        --set image.repository=${CICD_BUILD_IMAGE_NAME} \
        --set image.tag=${CICD_BUILD_IMAGE_TAG}