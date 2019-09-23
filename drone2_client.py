# -*- coding: utf-8 -*-

import socket, time
import json, threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('165.246.45.45', 2000))  # base center
print("Base center connected")

def function_BaseCenter():
    global sock

    while True:
        data = sock.recv(65535).decode()  # 한 타임씩 데이터 받기기
        if (data == "Finish"):
            print("disconnected")
            break
        print("Received data: " + data)
        f = open("received.json", 'w+')
        f.write(data)
        f.close()

        time.sleep(3)  # 조종기로 이동

        # Sensor1.start()
        # Sensor2.start()
        # Sensor3.start()
        #
        # Sensor1.join()
        # Sensor2.join()
        # Sensor3.join()
        #
        function_sensor1()
        function_sensor2()
        function_sensor3()

    sock.close()


def function_sensor1():
    global data1
    try:
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock1.connect(('165.246.45.45', 200))  # sensor1

        data1 = sock1.recv(65535).decode()
        print("Received data by sensor1: " + data1)

        sock.send(data1.encode())  # 수집 센서 값을 base center에게 전송
        print("Deliver sensor1 data to base center: " + data1)

        sock1.close()

    except ConnectionRefusedError:
        print("ConnectionRefusedError-1")


def function_sensor2():
    global data2
    try:
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.connect(('165.246.45.45', 400))  # sensor2

        data2 = sock2.recv(65535).decode()
        print("Received data by sensor2: " + data2)

        sock2.close()

    except ConnectionRefusedError:
        print("ConnectionRefusedError-2")


def function_sensor3():
    global data3
    try:
        sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock3.connect(('165.246.45.45', 600))  # sensor3

        data3 = sock2.recv(65535).decode()
        print("Received data by sensor2: " + data3)

        sock3.close()

    except ConnectionRefusedError:
        print("ConnectionRefusedError-3")


# 스레딩 방식
FunctionBaseCenter = threading.Thread(target=function_BaseCenter)
# Sensor1 = threading.Thread(target=function_sensor1())
# Sensor2 = threading.Thread(target=function_sensor2())
# Sensor3 = threading.Thread(target=function_sensor3())

FunctionBaseCenter.start()
# Sensor1.start()
# Sensor2.start()
# Sensor3.start()

FunctionBaseCenter.join()
# Sensor1.join()
# Sensor2.join()
# Sensor3.join()
