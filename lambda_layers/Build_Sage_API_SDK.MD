```
python3 -m pip install -r requirements.txt -t ./python/lib/python3.8/site-packages
python3 setup.py install --root ./python/lib/python3.8/site-packages

# !! since fedora 35 is python 3.10 need to move some things around
mv ./python/lib/python3.8/site-packages/usr/local/lib/python3.10/site-packages/sageintacctsdk ./python/lib/python3.8/site-packages

zip -r sageintacct_layer.zip ./python
ls -lah ./sageintacct_layer.zip   # 1.1MB

unzip -l ./sageintacct_layer.zip 
    python/lib/python3.8/site-packages/urllib3/response.py
    python/lib/python3.8/site-packages/usr/local/lib/python3.10/site-packages/sageintacctsdk/apis/bills.py

aws lambda publish-layer-version --layer-name sageintacct-layer --description "fylein sageintacct-sdk-py library" --zip-file fileb://./sageintacct_layer.zip --compatible-runtimes  python3.8

    "LayerArn": "arn:aws:lambda:us-west-1:979255393896:layer:sageintacct-layer",
    "LayerVersionArn": "arn:aws:lambda:us-west-1:979255393896:layer:sageintacct-layer:3",

aws lambda list-layer-versions --layer-name sageintacct-layer


```