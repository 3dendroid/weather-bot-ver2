#!/usr/bin/env bash
openssl genrsa -out webhook_pkey.pem 2048 &&\
openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
