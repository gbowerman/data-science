# data-science - CLI
Azure CLI/bash scripts related to data science

_[create_ds_vm.sh](./create-ds-vm.sh)_

Example bash script which uses [Azure CLI 2.0](https://docs.microsoft.com/cli/azure/get-started-with-azure-cli?view=azure-cli-latest) to automate creation of Microsoft Windows 2016 [Data Science VM](https://docs.microsoft.com/azure/machine-learning/data-science-virtual-machine/overview). This script takes the following command line arguments: virtual machine name, resource group name, data center location, VM size (small, medium or large), user and password. The Azure resource group is created if does not already exist. This script can be run directly from the Azure Portal in an [Azure Cloud Shell](https://azure.microsoft.com/features/cloud-shell/).

Here's a short video (no audio) showing an example of running this script in the Azure Cloud Shell: [![Watch the video](./img/vid-thumbnail.PNG)](https://youtu.be/YssMXocBTgs)



