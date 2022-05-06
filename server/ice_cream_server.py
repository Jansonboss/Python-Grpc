import time
import grpc
import concurrent
import concurrent.futures as futures

import ice_cream_pb2
import ice_cream_pb2_grpc


######################################################################
#  service IceCream {
#  rpc OrderIceCream(IceCreamRequest) returns (IceCreamResponse);
#  }
#
#  
# For the server.py, we need to implement function, following template above
# - take the input: IceCreamRequest
# - output: IceCreamResponse
# 
#######################################################################

PORT_NUMBER = "50051"

class IceCreamServicer(ice_cream_pb2_grpc.IceCreamServicer):
    def OrderIceCream(self, request, context):
        print("server: We got ice cream requests from customer....")
        print(f"server: Number of Scoops: {request.scoops}")
        print(f"server: Flavor Name: {request.flavor}")
        print(f"server: Making the ice cream ....")
        time.sleep(1)
        print(f"server: Sending the ice cream ....", "\n")
        message = "Ice Cream Finished!"
        return ice_cream_pb2.IceCreamResponse(message=message)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ice_cream_pb2_grpc.add_IceCreamServicer_to_server(IceCreamServicer(), server)

    print(f"Server Started. listening on port {PORT_NUMBER}...")
    server.add_insecure_port(f"[::]:{PORT_NUMBER}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()