from test_input import raw

# BITS = bin(int(raw, 16))[2:]
BITS = "".join([bin(int(c, 16))[2:].zfill(4) for c in raw])


def parse_bits(bits):
    results = []
    while bits and bits != "0" * len(bits):
        print(f"Bits: {bits}")
        version = int(bits[0:3], 2)
        type_id = int(bits[3:6], 2)
        bits = bits[6:]
        print(version, type_id, bits)

        if type_id == 4:
            print("Type 4")
            acc = []
            while bits[0] == "1":
                acc.append(bits[1:5])
                bits = bits[5:]
            acc.append(bits[1:5])
            bits = bits[5:]
            results.append((version, type_id, int("".join(acc), 2)))
        else:
            print("Not type 4")
            length_type_id = bits[0]
            new_bits = bits[1:12 if length_type_id == "1" else 16]
            results.append((version, type_id, parse_bits(new_bits)))
            bits = bits[12 if length_type_id == "1" else 16:]
    return results


print(f"Part 1: {parse_bits(BITS)}")
