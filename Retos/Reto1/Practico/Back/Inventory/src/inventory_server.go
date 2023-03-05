package main

import (
	pb "InventoryMod/ProductAvailability"
	"context"
	"log"
	"net"

	"google.golang.org/grpc"
)

const (
	port = ":50051"
)

type server struct {
	pb.UnimplementedProductAvailabilityServer
}

func (s *server) SearchProduct(ctx context.Context, in *pb.ProductToSearch) (*pb.ProductAvailabilityResponse, error) {
	if in.GetIdProduct() == 2 {
		return &pb.ProductAvailabilityResponse{StatusCode: false}, nil
	}
	return &pb.ProductAvailabilityResponse{StatusCode: true}, nil
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterProductAvailabilityServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
