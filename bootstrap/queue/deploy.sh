#!/bin/bash
export RABBITMQ_PASSWORD=$(kubectl get secret --namespace "sorting-queue" rabbitmq -o jsonpath="{.data.rabbitmq-password}" | base64 --decode)
export RABBITMQ_ERLANG_COOKIE=$(kubectl get secret --namespace "sorting-queue" rabbitmq -o jsonpath="{.data.rabbitmq-erlang-cookie}" | base64 --decode) 
helm repo add bitnami https://charts.bitnami.com/bitnami
helm upgrade --install rabbitmq bitnami/rabbitmq \
        --namespace "sorting-queue" --create-namespace \
        --set auth.password=$RABBITMQ_PASSWORD \
        --set auth.erlangCookie=$RABBITMQ_ERLANG_COOKIE
echo "Username      : user"
echo "Password      : $RABBITMQ_PASSWORD"
echo "ErLang Cookie : $RABBITMQ_ERLANG_COOKIE"