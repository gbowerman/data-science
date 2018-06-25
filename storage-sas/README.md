# storage-sas
Bash and Python tools to create Azure storage SAS keys and write storage blobs using write-only SAS keys

- [createstorage.sh](./createstorage.sh) - Bash script to create an Azure storage account, and two SAS keys, one with read-list permissions, and one with write-only permissions.
- [write-test.py](./write-test.py) - Python program to write text blobs using a write-only SAS URI.
