#Write a program that will display the account id from the arn below 
#Display on the screen: the aws account id is: account_id.

arn = "arn:aws:iam::123456789012:user/Development/product_1234/*"

split_arn = arn.split(":")

print(split_arn)

split_account_id = split_arn[4]

print(f'The aws account id is {split_account_id}')
