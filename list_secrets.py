import boto3

# Create a client for the Secrets Manager service
client = boto3.client('secretsmanager')

# Set the parameters for the list_secrets operation
params = {
    'MaxResults': 10
}

# Set a flag to indicate whether there are more secrets to list
more_secrets = True

# Set a list to store the secrets
secrets = []

# Loop until there are no more secrets to list
while more_secrets:
    # List the secrets
    response = client.list_secrets(**params)
    
    # Add the secrets to the list
    secrets.extend(response['SecretList'])
    
    # Set the flag to False if there are no more secrets to list
    if 'NextToken' not in response:
        more_secrets = False
    else:
        # Set the next token for the next iteration
        params['NextToken'] = response['NextToken']

# Print the names of the secrets
for secret in secrets:
    print(secret['Name'])
