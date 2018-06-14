#!/bin/bash
# script to create a Microsoft Windows 2016 data science VM in Azure
VMNAME=$1
RGNAME=$2
LOCATION=$3  # e.g. westus2
CONFIG=$4    # small|medium|large
USER=$5      # e.g. wpauser
PASS=$6      # must be 12 or more characters

PUB='microsoft-ads'
OFFER='windows-data-science-vm'
SKU='windows2016'
VERSION='latest'

# determine config size
case $CONFIG in
    small)
        SIZE='Standard_D1_v2'
        DATASIZEGB='32'
        ;;
    medium)
        SIZE='Standard_D2_v3'
        DATASIZEGB='256'
        ;;
    large)
        SIZE='Standard_D8_v3'
        DATASIZEGB='1024'
        ;;
esac

# create the resource group (keeps going if already exists)
az group create --name $RGNAME --location $LOCATION

# create the VM
az vm create \
    --name $VMNAME --resource-group $RGNAME --image $PUB\:$OFFER\:$SKU\:$VERSION \
    --plan-name $SKU --plan-product $OFFER --plan-publisher $PUB \
    --admin-username $USER --admin-password $PASS \
    --size $SIZE \
    --data-disk-sizes-gb $DATASIZEGB