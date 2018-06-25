'''write-test.py - test program to write an Azure block blob using a SAS URI'''
import argparse
from urllib import request, parse
import sys

from azure.storage.blob.baseblobservice import BaseBlobService


def put_blob(sa_uri, container, blob_name, sas_key, blob_text):
    '''Write blob data using a url PUT'''
    opener = request.build_opener(request.HTTPHandler)
    urlrequest = request.Request(
        sa_uri + container + '/' + blob_name + '?' + sas_key, data=blob_text)
    urlrequest.add_header('x-ms-blob-type', 'BlockBlob')
    urlrequest.get_method = lambda: 'PUT'
    opener.open(urlrequest)


def main():
    '''Main routine, start by parsing the URL argument'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--uri', '-u', required=True, action='store', help='SAS URI with write perms, in quotes')
    arg_parser.add_argument(
        '--blobname', '-n', action='store', help='Name of blob file to create')
    arg_parser.add_argument(
        '--text', '-t', action='store', help='blob file text to write')

    args = arg_parser.parse_args()
    uri = args.uri

    # write a default blob name and text if not specified
    blob_name = 'deleteme.txt' if args.blobname is None else args.blobname
    blob_text = b'Blob write test message.' if args.text is None else str.encode(
        args.text)

    # split the URI into components
    uri_tuple = parse.urlparse(uri)
    base_uri = 'https://' + uri_tuple.netloc
    container = uri_tuple.path
    sas_key = uri_tuple.query

    # write the blob
    put_blob(base_uri, container, blob_name, sas_key, blob_text)


if __name__ == "__main__":
    main()
