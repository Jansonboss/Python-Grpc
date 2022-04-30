from unittest import result
from grpc import server
import square_root_pb2
from square_root_pb2_grpc import SquareRootServiceServicer, SquareRootServiceStub, add_SquareRootServiceServicer_to_server
from square_root_pb2 import Result
from concurrent.futures import ThreadPoolExecutor


class SquareRootServicer(SquareRootServiceServicer):
	def squareRoot(self, request, context):
		resulta = request.input ** 2
		return Result(resulta = resulta)


def main():
	server = server(ThreadPoolExecutor(max_workers=5))
	add_SquareRootServiceServicer_to_server(SquareRootServicer(), server=server)
	print(f"Logger: Server Listening")

	server.add_insecure_port("[::]50552")
	server.start()
	server.wait_for_termination()

main()