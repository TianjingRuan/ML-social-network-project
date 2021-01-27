import numpy as np
import pandas as pd
import random
import csv


def generate_dictionary():
    # all source
    follow = dict()
    # all nodes
    follower = dict()
    # We can find that all the nodes are in the sink, but not in the source (some edges are unknown)
    with open('train.txt') as file:
        for i in file:
            splited = i.strip().split()
            source = splited[0]
            sinks = splited[1:]
            for sink in sinks:
                follow[source] = follow.get(source, set())
                follow[source].add(sink)
                follower[sink] = follower.get(sink, set())
                follower[sink].add(source)
    # print(follow["1000106"])
    print("number of all nodes:")
    print(len(follower))
    print("number of source:")
    print(len(follow))
    return follow, follower


# generate dataset and save to csv file
def generate_data(follow, follower, csvfilename):
    filename = csvfilename
    # writing to csv file
    with open(filename, 'w') as csvfile:
        csvfile.truncate()  # clear csv
        csvwriter = csv.writer(csvfile)
        header = ["source", "sink", "probability"]
        csvwriter.writerow(header)
        for source in follow.keys():
            random_node = random.choice(list(follower.keys()))
            # for a random node in all nodes, if it is followed by source, set probability to 1, otherwise, 0
            if random_node in follow[source]:
                lst = [source, random_node, 1]
            else:
                lst = [source, random_node, 0]
            csvwriter.writerow(lst)

            # add connected node
            random_follow = random.sample(follow[source], k=1)[0]
            lst1 = [source, random_follow, 1]
            csvwriter.writerow(lst1)
    print("data generation done!")


if __name__ == '__main__':
    follow, follower = generate_dictionary()
    generate_data(follow, follower, "data/data1.csv")
