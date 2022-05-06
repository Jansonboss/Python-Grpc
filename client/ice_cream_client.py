import time
import grpc
from server import ice_cream_pb2, ice_cream_pb2_grpc


def main():
    with grpc.insecure_channel("0.0.0.0:50051") as channel:
        client_stub = ice_cream_pb2_grpc.IceCreamStub(channel=channel)
        request_payload = ice_cream_pb2.IceCreamRequest(scoops=1, flavor="vanilla")
        print("client: Ordering the ice cream")
        time.sleep(3)

        # Do remote methods calls (OrderIceCream) from grpc service
        ice_cream_message = client_stub.OrderIceCream(request_payload)
        message = f"{ice_cream_message.message} -> client: ice cream received"
        print(message)


if __name__ == "__main__":
    main()