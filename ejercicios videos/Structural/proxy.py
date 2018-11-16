#proxy.py

import time

class Producer:
    '''Define the resoure-intesive object to instantiate'''
    def produce(self):
        print("Producer is working hard")

    def meet(self):
        print("Producer has time to meet you now")

class Proxy:
    '''Define the relatively less resource-intensive proxy to instantiate as a middleman'''
    def __init__(self):
        self.occupied = "NO"
        self.producer = None

    def produce(self):
        '''Check if Producer is available'''
        print("Artist checking if producer is available....")

        if self.occupied == "No":
            '''If the producer is available. create a producer object'''
            self.producer = Producer()
            time.sleep(2)

            '''Make the producer meet the guest!'''
            self.producer.meet()

        else:
            '''Otherwise, don't instantiate a producer'''
            time.sleep(2)
            print("Producer is busy")

'''Instantiate a Proxy'''
p = Proxy()
'''<Make the proxy: Artist produce until Producer is avilable'''
p.produce()
'''Change the state to occupied'''
p.occupied = "Yes"
'''Make the producer produce'''
p.produce()
