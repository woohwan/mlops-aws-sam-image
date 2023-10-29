#!/usr/bin/env bash

# restapiid 값을 가져옵니다. https://us-east-1.console.aws.amazon.com/apigateway/main/apis?region=us-east-1 에서 확인할 수 있습니다.
restapiid=579m475jth

curl -d '{
   "Cylinders":8,
   "Displacement":307,
   "Horsepower":165,
   "Weight":3693,
   "Acceleration":11,
   "ModelYear":70,
   "Country":"Japan"
}'\
   -H "Content-Type: application/json" \
   -X POST  https://g2l28bsdkh.execute-api.ap-northeast-2.amazonaws.com/Prod/predict/
   # -X POST http://localhost:3000/predict
