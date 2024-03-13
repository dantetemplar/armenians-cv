def print_cuda_status():
    import torch

    cuda_available = torch.cuda.is_available()
    if cuda_available:
        print("CUDA is available")
        count = torch.cuda.device_count()
        print(f"Number of CUDA devices: {count}")
        for i in range(count):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available")
