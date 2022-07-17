from functools import reduce


class Packet:
    def __init__(self, version, type_id, payload):
        self.version = version
        self.type_id = type_id
        self.payload = payload

    def __repr__(self):
        repr = (
            f"(version: {self.version} type_id: {self.type_id} payload: {self.payload})"
        )
        return repr

    def value(self):
        match self.type_id:
            case 0:
                return sum([p.value() for p in self.payload])
            case 1:
                return reduce(lambda x, y: x * y, [p.value() for p in self.payload])
            case 2:
                return min([p.value() for p in self.payload])
            case 3:
                return max([p.value() for p in self.payload])
            case 4:
                return self.payload
            case 5:
                lis = [p.value() for p in self.payload]
                return int(lis[0] > lis[1])
            case 6:
                lis = [p.value() for p in self.payload]
                return int(lis[0] < lis[1])
            case 7:
                lis = [p.value() for p in self.payload]
                return int(lis[0] == lis[1])

    @classmethod
    def from_data(self, data):
        version = int(data[:3], 2)
        type_id = int(data[3:6], 2)
        if type_id == 4:
            payload = ""
            cursor = 6
            while True:
                value = data[cursor : cursor + 5]
                payload += value[-4:]
                cursor += 5
                if int(value[0]) == 0:
                    break
            payload = int(payload, 2)
        else:
            payload = []
            length_type_id = int(data[6])
            cursor = 7
            if length_type_id == 0:
                length = int(data[cursor : cursor + 15], 2)
                cursor += 15
                r = data[cursor : cursor + length]
                while r and int(r, 2) != 0:
                    p, r_cursor = Packet.from_data(r)
                    payload.append(p)
                    r = r[r_cursor:]
                cursor += length
            elif length_type_id == 1:
                number = int(data[cursor : cursor + 11], 2)
                cursor += 11
                r = data[cursor:]
                for _ in range(number):
                    p, r_cursor = Packet.from_data(r)
                    payload.append(p)
                    cursor += r_cursor
                    r = r[r_cursor:]
            else:
                raise RuntimeError("unreachable")
        return Packet(version, type_id, payload), cursor

    def versionsum(self):
        match self.payload:
            case list():
                return self.version + sum([p.versionsum() for p in self.payload])
            case int():
                return self.version


with open("input") as f:
    hex_data = f.read().strip()
    packet = format(int(hex_data, 16), f"0{len(hex_data*4)}b")

p, cursor = Packet.from_data(packet)

print(repr(p))

print(p.versionsum())

print(p.value())
