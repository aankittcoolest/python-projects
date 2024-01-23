
### Steps

1. Set up aws-ses

```sh
cd send-email-using-aws-ses
git clone https://github.com/aankittcoolest/terraform.git
cd terraform/05-deploy-ses
terraform init
terraform plan -var="admin_email=aankittcoolest@gmail.com" -var="iam_policy=ses-policy" 
terraform apply -var="admin_email=aankittcoolest@gmail.com" -var="iam_policy=ses-policy" 
terraform output smtp_password
```

2. Verify the email.

3. Update `.env` with the required information.

4. Test email is working properly.

```sh
pip3 install -r requirements.txt
python3 main.py
```

5. Destroy terraform resources.

```sh
terraform destroy -var="admin_email=admin@mail.com" -var="iam_policy=ses-policy" 
```