### Machine Learning using SAM
```  
sam init --name sam-app-image --package-type Image --architecture x86_64
Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
        1 - Hello World Example
        2 - Machine Learning
Template: 2

Which runtime would you like to use?
        1 - python3.9
        2 - python3.8
        3 - python3.11
        4 - python3.10
Runtime: 3

Based on your selections, the only dependency manager available is pip.
We will proceed copying the template using pip.

Select your starter template
        1 - PyTorch Machine Learning Inference API
        2 - Scikit-learn Machine Learning Inference API
        3 - Tensorflow Machine Learning Inference API
        4 - XGBoost Machine Learning Inference API
Template: 3

Would you like to enable X-Ray tracing on the function(s) in your application?  [y/N]: n

Would you like to enable monitoring using CloudWatch Application Insights?
For more info, please view https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html [y/N]: n

    -----------------------
    Generating application:
    -----------------------
    Name: sam-app-image
    Base Image: amazon/python3.11-base
    Architectures: x86_64
    Dependency Manager: pip
    Output Directory: .
    Configuration file: sam-app-image/samconfig.toml

    Next steps can be found in the README file at sam-app-image/README.md


Commands you can use next
=========================
[*] Create pipeline: cd sam-app-image && sam pipeline init --bootstrap
[*] Validate SAM template: cd sam-app-image && sam validate
[*] Test Function in the Cloud: cd sam-app-image && sam sync --stack-name {stack-name} --watch
```