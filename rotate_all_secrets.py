import boto3

def rotate_secrets(secret_ids):
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')

    # Rotate each secret in the list
    for secret_id in secret_ids:
        client.batch_rotate_secret(SecretId=secret_id)

# Example usage: rotate a list of secrets
rotate_secrets(['secret1', 'secret2', 'secret3'])
