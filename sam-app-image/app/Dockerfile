FROM public.ecr.aws/lambda/python:3.11

COPY app.py requirements.txt auto-mpg.csv myopslib.py ./
COPY mlp-model/ mlp-model/

RUN python3.11 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]
