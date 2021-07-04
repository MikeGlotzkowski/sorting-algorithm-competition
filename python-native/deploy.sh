#!/bin/bash
helm upgrade --install "${CICD_MICROSERVICE_NAME}" "./${CICD_MICROSERVICE_NAME}" \
        -f "./${CICD_MICROSERVICE_NAME}/values.yaml" \
        --namespace "${CICD_MICROSERVICE_NAMESPACE}" --create-namespace \
        --set image.repository=${CICD_BUILD_IMAGE_NAME} \
        --set image.tag=${CICD_BUILD_IMAGE_TAG}