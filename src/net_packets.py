def run():
    size, num_packets = map(int, input().split())
    processing_time = [None] * num_packets
    buffer = []
    total_processing_time = 0
    for i in range(num_packets):
        arrival, duration = map(int, input().split())
        # start of current package processing
        start_time = total_processing_time if total_processing_time > arrival else arrival
        if buffer and arrival >= buffer[0][1]:
            buffer.pop(0)
        if len(buffer) == size:
            processing_time[i] = -1
        else:
            total_processing_time = start_time + duration
            buffer.append((i, total_processing_time))
            processing_time[i] = start_time

    if processing_time:
        for time in processing_time:
            print(time)


if __name__ == '__main__':
    run()
