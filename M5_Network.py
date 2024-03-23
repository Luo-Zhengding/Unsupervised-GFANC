import torch

class ResBlock(torch.nn.Module):
    
    def __init__(self, prev_channel, channel, conv_kernel, conv_stride, conv_pad):
        super(ResBlock, self).__init__()
        self.res = torch.nn.Sequential(
            torch.nn.Conv1d(in_channels = prev_channel, out_channels=channel, kernel_size=conv_kernel, stride=conv_stride, padding=conv_pad),
            torch.nn.BatchNorm1d(channel),
            torch.nn.ReLU(),
            torch.nn.Conv1d(in_channels=channel, out_channels=channel, kernel_size=conv_kernel, stride=conv_stride, padding=conv_pad),
            torch.nn.BatchNorm1d(channel),
        )
        self.bn = torch.nn.BatchNorm1d(channel)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        identity = x
        x = self.res(x)
        if x.shape[1] == identity.shape[1]:
            x += identity
        # repeat the smaller block till it reaches the size of the bigger block
        elif x.shape[1] > identity.shape[1]:
            if x.shape[1] % identity.shape[1] == 0:
                x += identity.repeat(1, x.shape[1]//identity.shape[1], 1)
            else:
                raise RuntimeError("Dims in ResBlock needs to be divisible on the previous dims!!")
        else:
            if identity.shape[1] % x.shape[1] == 0:
                identity += x.repeat(1, identity.shape[1]//x.shape[1], 1)
            else:
                raise RuntimeError("Dims in ResBlock needs to be divisible on the previous dims!!")
            x = identity
        x = self.bn(x)
        x = self.relu(x)
        return x
    
class CNNRes(torch.nn.Module):       
        
    def __init__(self, channels, conv_kernels, conv_strides, conv_padding, pool_padding, num_classes=15):
        assert len(conv_kernels) == len(channels) == len(conv_strides) == len(conv_padding)
        super(CNNRes, self).__init__()
        
        # create conv block
        prev_channel = 1
        self.conv_block = torch.nn.Sequential(
            torch.nn.Conv1d(in_channels=prev_channel, out_channels=channels[0][0], kernel_size=conv_kernels[0], stride=conv_strides[0], padding=conv_padding[0]),
            # add batch norm layer
            torch.nn.BatchNorm1d(channels[0][0]),
            # adding ReLU
            torch.nn.ReLU(),
            # adding max pool
            torch.nn.MaxPool1d(kernel_size = 4, stride = 4, padding = pool_padding[0]),
        )
        
        # create res
        prev_channel = channels[0][0]
        self.res_blocks = torch.nn.ModuleList()
        for i in range(1, len(channels)):
            # add stacked res layer
            block = []
            for j, conv_channel in enumerate(channels[i]):
                block.append(ResBlock(prev_channel, conv_channel, conv_kernels[i], conv_strides[i], conv_padding[i]))
                prev_channel = conv_channel
            self.res_blocks.append(torch.nn.Sequential(*block))

        # create pool blocks
        self.pool_blocks = torch.nn.ModuleList()
        for i in range(1, len(pool_padding)):
            # adding Max Pool (drops dims by a factor of 4)
            self.pool_blocks.append( torch.nn.MaxPool1d(kernel_size = 4, stride = 4, padding = pool_padding[i]) )

        # global pooling
        self.global_pool = torch.nn.AdaptiveAvgPool1d(1)

        self.linear = torch.nn.Sequential(
            torch.nn.Linear(prev_channel, num_classes),
            torch.nn.Sigmoid()) # !!! add Sigmoid


    def forward(self, inwav):
        inwav = self.conv_block(inwav)
        for i in range(len(self.res_blocks)):
            # apply conv layer
            inwav = self.res_blocks[i](inwav)
            # apply max_pool
            if i < len(self.pool_blocks): inwav = self.pool_blocks[i](inwav)
        # apply global pooling
        out = self.global_pool(inwav).squeeze()
        out = self.linear(out)
        return out


m6_res = CNNRes(channels = [[128], [128]*2],
         conv_kernels = [80, 3],
         conv_strides = [4, 1],
         conv_padding = [38, 1],
         pool_padding = [0, 0])