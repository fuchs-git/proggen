all = open('firmware.bin', 'rb').read()

data = all[0x2000:0x2590]
key = all[0x1aa1c:0x1a1c+16]

var1 = 0xC6EF3720
var2 = 0x9E3779B9
key = []
for i in range(4):
    key.append((((((key[i+3]<<8) | key[i+2]) <<8) | key[i+1]) <<8 ) | key[i+1])

def decrypt(data, offset, key):
    local_c = (((((data[offset+3]<<8) | data[offset+2]) <<8) | data[offset+1]) <<8 ) | data[offset+0]
    local_10 = (((((data[offset+7]<<8) | data[offset+6]) <<8) | data[offset+5]) <<8 ) | data[offset+4]

    local_14 = var1
    for _ in range(32):
        local_10 = local_10 - ((key[3] + (local_c >>5)) ^ ((local_c * 0x10) + key[2])^(local_14+local_c))
        local_c = local_c - ((key[1] + (local_10 >> 5))^(local_10 * 0x10 + key[0] ^(local_14+ local_10)))

    return [local_c, local_10]

stack = [0 for _ in range(500)]

auStack_18 = 0x28
auStack_20 = 0x20
auStack_30 = 0x10


for i in range(100):
    for j in range(16):
        stack[j+auStack_20] = data[i*16]
        decrypt(stack, auStack_20, key)

        if i != 0:
            for j in range(16):
                stack[j + auStack_30] = data[i * 16]

            for k in range(8):
                stack[auStack_20 + k *4] = stack[auStack_20 + k*4] ^ stack[auStack_30 + k*4 +8]

        decrypt(stack, auStack_18, key)
        for j in range(16):
            stack[j + auStack_30] = data[i * 16]

        for k in range(8):
            stack[auStack_20 + k +8] = stack[auStack_30 + k] ^ stack[auStack_30 + k + 8]

