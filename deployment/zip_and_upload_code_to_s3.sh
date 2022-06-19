echo "Starting packaging..."

TIMESTAMP=$(date +%s)

mkdir -p $REPO_DIR/distr

# Zip Layers
cd $REPO_DIR/lambda/layers/sagesdk/; zip -r $REPO_DIR/distr/sagesdk.zip python/; cd $REPO_DIR;

# Upload Layers
aws s3 cp $REPO_DIR/distr/sagesdk.zip s3://$S3BUCKETNAME/sagesdk-py-code-$TIMESTAMP.zip

# Zip Functions
cd $REPO_DIR/lambda/incremental_sage_process/; zip -r $REPO_DIR/distr/incremental_sage_process.zip ./*; cd $REPO_DIR;

# Upload Functions
aws s3 cp $REPO_DIR/distr/incremental_sage_process.zip s3://$S3BUCKETNAME/incremental_sage_process-code-$TIMESTAMP.zip

echo "Current Version ${TIMESTAMP}"
