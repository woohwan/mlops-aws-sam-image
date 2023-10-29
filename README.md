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
1. cd sam-app-image  
2. app/app.py, app/Dockerfile, app/requirements.txt, events/event.json 등 필요 파일 수정   
3. local test  
```  
(mlops)  ✘  ~/playground/mlops/aws-sam/sam-app-image  ↱ main ±
❯ sam local invoke "InferenceFunction" -e events/event.json
Invoking Container created from inferencefunction:python3.11-v1
Building image.................
Using local image: inferencefunction:rapid-x86_64.

START RequestId: a391c533-87a2-4563-9f2e-54be23e0c86b Version: $LATEST
2023-10-29 13:31:54.997518: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-10-29 13:31:55.121245: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2023-10-29 13:31:55.121335: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2023-10-29 13:31:55.121372: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2023-10-29 13:31:55.144634: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-10-29 13:31:55.145204: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-10-29 13:31:56.620821: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
END RequestId: a391c533-87a2-4563-9f2e-54be23e0c86b
REPORT RequestId: a391c533-87a2-4563-9f2e-54be23e0c86b  Init Duration: 0.41 ms  Duration: 4580.73 ms    Billed Duration: 4581 ms        Memory Size: 5000 MBMax Memory Used: 5000 MB
{"statusCode": 200, "body": "{\"message\": \"MPG: [8.184905052185059]\"}"}
```  
4. container test
```  
❯ sam local invoke
Invoking Container created from inferencefunction:python3.11-v1
Building image.................
Using local image: inferencefunction:rapid-x86_64.

START RequestId: c94da49a-7a7f-4d72-9852-bfe279bf68c4 Version: $LATEST
2023-10-29 13:34:49.086622: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-10-29 13:34:49.149790: E tensorflow/compiler/xla/stream_executor/cuda/cuda_dnn.cc:9342] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2023-10-29 13:34:49.149884: E tensorflow/compiler/xla/stream_executor/cuda/cuda_fft.cc:609] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2023-10-29 13:34:49.149932: E tensorflow/compiler/xla/stream_executor/cuda/cuda_blas.cc:1518] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2023-10-29 13:34:49.158897: I tensorflow/tsl/cuda/cudart_stub.cc:28] Could not find cuda drivers on your machine, GPU will not be used.
2023-10-29 13:34:49.159294: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-10-29 13:34:50.504960: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
END RequestId: c94da49a-7a7f-4d72-9852-bfe279bf68c4
REPORT RequestId: c94da49a-7a7f-4d72-9852-bfe279bf68c4  Init Duration: 0.29 ms  Duration: 3059.74 ms    Billed Duration: 3060 ms        Memory Size: 5000 MBMax Memory Used: 5000 MB
{"statusCode": 200, "body": "{\"message\": \"Incorrect event. event: {}\"}"}
```  

5. deploy  
```

```  

6. api gate url을 사용하여 요청