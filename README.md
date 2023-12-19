# Python-Grpc
Simple Example for python GRPC service

## Tutorial:
- https://realpython.com/python-microservices-grpc/
- https://www.youtube.com/watch?v=psYAhc9JUyo&t=761s&ab_channel=Jbang
- https://www.youtube.com/watch?v=-Mcvbz5J9kQ&ab_channel=evanugarte


## Code Generation
```
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/***.proto
```
